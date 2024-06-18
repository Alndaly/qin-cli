import typer
from pathlib import Path
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