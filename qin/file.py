import os
import typer
from typing import Annotated
from rich import print
from .config import config

file_app = typer.Typer()

def delete_file(path: str, log: bool = True, temp: bool = True):
    file_name = path.split('/')[-1]
    if temp:
        os.rename(path, os.path.join(config.TRASH_DIR_PATH, file_name))
    else:
        os.remove(path=path)
    if log:
        print(f"{path}已删除")
        
def get_all_files_in_directory(path):
    all_files = []  # 用于保存所有文件的路径
    # 递归遍历文件夹
    for foldername, subfolders, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)  # 构建文件的完整路径
            all_files.append(file_path)
    return all_files

@file_app.command("delete")
def delete(path: Annotated[str, typer.Option("--path", "-p")], include: Annotated[str, typer.Option("--include", "-i")], recursion: Annotated[bool, typer.Option("--recursion", "-r")] = False, log: Annotated[bool, typer.Option("--log", "-l")] = False):
    if recursion:
        file_path_list = get_all_files_in_directory(path=path)
        file_path_list = list(filter(lambda file_path: include in file_path, file_path_list))
        print(f"要删除的文件如下:")
        for file_path in file_path_list:
            print(f'{file_path}')
        print(f'共计 [bold red]{len(file_path_list)}[/bold red] 个')
        if len(file_path_list) == 0:
            print('程序结束')
            return
        print('确认删除吗?')
        user_ans = typer.prompt("yes(y)/no(n) 默认n")
        if user_ans == 'yes' or user_ans == 'y':
            for file_path in file_path_list:
                delete_file(file_path)
        else:
            print('程序结束')