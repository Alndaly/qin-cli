import os
import typer
from typing import Annotated
from rich import print
from .config import config

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