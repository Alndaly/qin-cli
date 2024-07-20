import typer
import os
import httpx
from pathlib import Path
from tqdm import tqdm
from rich import print
from .common.ai import get_civitai_model_info_by_hash, calculate_file_hash
from typing import Annotated

ai_app = typer.Typer(help="AI utility")

@ai_app.command('model', help='Get model info.')
def get_model_info(path: Annotated[str, typer.Option("--path", "-p", help="Path to the model file")]):
    file_item = Path(path)
    model_info = get_civitai_model_info_by_hash(calculate_file_hash(file_item))
    print(model_info)
    
@ai_app.command('hash', help='Calculate model hash.')
def get_model_hash(path: Annotated[str, typer.Option("--path", "-p", help="Path to the model file")]):
    file_item = Path(path)
    model_hash = calculate_file_hash(file_item)
    print(model_hash)
    
@ai_app.command('preview', help='Get model preview image.')
def preview_model(path: Annotated[str, typer.Option("--path", "-p", help="The path to the directory")] = os.getcwd(),
                  recursion: Annotated[bool, typer.Option("--recursion", "-r", help="If you want to git pull for the sub folder")] = False):
    
    total = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for item in filenames:
            file_item = Path(dirpath) / item
            if(file_item.suffix == '.safetensors' or file_item.suffix == '.ckpt'):
                total += 1
        if not recursion:
            dirnames[:] = []  # Skip subdirectories in this git repository
    print(f"获取预览图中，总计 {total} 个模型。")
    
    progress_bar = tqdm(total=total)
    for dirpath, dirnames, filenames in os.walk(path):
        for item in filenames:
            file_item = Path(dirpath) / item
            if(file_item.suffix == '.safetensors' or file_item.suffix == '.ckpt'):
                model_hash = calculate_file_hash(file_item)
                model_info = get_civitai_model_info_by_hash(model_hash)
                if model_info == None:
                    print(f'模型{item}在c站上无法找到预览图，可能是对应hash值仍未存储入c站模型hash库')
                    progress_bar.update(1)
                    continue
                # get the preview image of model
                model_preview_image_url = model_info['images'][0]['url']
                response = httpx.get(model_preview_image_url)
                preview_path = file_item.with_suffix(".preview.png")
                if response.status_code == 200:
                    with open(preview_path, "wb") as f:
                        f.write(response.content)
                progress_bar.update(1)
        if not recursion:
            dirnames[:] = []  # Skip subdirectories in this git repository