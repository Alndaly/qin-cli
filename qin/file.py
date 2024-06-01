import os
import typer
import oss2
import time
import pymupdf
from typing import Annotated
from tqdm import tqdm
from rich import print
from .config.config import config

file_app = typer.Typer()

def delete_file(path: str, temp: bool = True):
    file_name = path.split('/')[-1]
    if temp:
        os.rename(path, os.path.join(config.TRASH_PATH, file_name))
    else:
        os.remove(path=path)
    print(f"{path} 删除成功")
        
def get_top_files_in_directory(path):
    all_files = []  # 用于保存所有文件的全路径
    # 列出当前文件夹中的所有文件和子文件夹
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            all_files.append(file_path)
    return all_files

def get_all_files_in_directory(path):
    all_files = []  # 用于保存所有文件的路径
    # 递归遍历文件夹
    for foldername, subfolders, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)  # 构建文件的完整路径
            all_files.append(file_path)
    return all_files
    
@file_app.command("pdf2png")
def pdf2png(path: Annotated[str, typer.Option("--path", "-p")]):
    doc = pymupdf.open(path) # open a document
    with tqdm(total=len(doc), unit='张', desc='转换中') as progress_bar:
        for page in doc: # iterate the document pages
            image = page.get_pixmap(matrix=pymupdf.Matrix(2, 2)) # get plain text encoded as UTF-8
            image.pil_save("page-%i.png" % page.number)
            progress_bar.update(1)
    print('转换完成')

@file_app.command("upload")
def upload(path: Annotated[str, typer.Option("--path", "-p")]):
    auth = oss2.Auth(config.get('ImgBed').get('AccessKeyId'), config.get('ImgBed').get('AccessKeySecret'))
    bucket = oss2.Bucket(auth, config.get('ImgBed').get('EndPoint'), config.get('ImgBed').get('BucketName'))
    file_suffix = path.split('.')[-1]
    total_bytes = os.path.getsize(path)
    file_name = f"{config.get('ImgBed').get('Folder')}/{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}.{file_suffix}"
    # 使用tqdm包装上传过程，显示进度条
    with tqdm(total=total_bytes, unit='B', unit_scale=True, desc='上传中') as progress_bar:
        def callback_wrapper(consumed_bytes, total_bytes):
            progress_bar.update(consumed_bytes - progress_bar.n)
            return consumed_bytes
        # 执行上传
        oss2.resumable_upload(
            bucket=bucket,
            key=f"{file_name}",
            filename=path,
            progress_callback=callback_wrapper
        )
    print(f'文件上传成功，重命名为{file_name}')

@file_app.command("delete")
def delete(path: Annotated[str, typer.Option("--path", "-p")], include: Annotated[str, typer.Option("--include", "-i")], recursion: Annotated[bool, typer.Option("--recursion", "-r")] = False, force: Annotated[bool, typer.Option("--force", "-f")] = False):
    if recursion:
        file_path_list = get_all_files_in_directory(path=path)
    else: 
        file_path_list = get_top_files_in_directory(path=path)
    file_path_list = list(filter(lambda file_path: include in file_path, file_path_list))
    print(f"要删除的文件如下:")
    for file_path in file_path_list:
        print(f'{file_path}')
    print(f'共计 [bold red]{len(file_path_list)}[/bold red] 个')
    if len(file_path_list) == 0:
        print('程序结束')
        return
    print(f"确认删除吗?[bold red]{'注意，你已经选择-f，此项行为将会直接从磁盘删除文件不可恢复！' if force else ''}[/bold red]")
    user_ans = typer.prompt("yes(y)/no(n)", default='n')
    if user_ans == 'yes' or user_ans == 'y':
        for file_path in file_path_list:
            if force:
                delete_file(file_path, temp=False)
            else:
                delete_file(file_path)
    else:
        print('程序结束')