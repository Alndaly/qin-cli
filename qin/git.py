import os
import typer
import subprocess
from rich import print
from typing import Annotated

git_app = typer.Typer(help="Git related commands")

@git_app.command("pull", help="Git Pull operate for all files in current directory")
def git_pull(path: Annotated[str, typer.Option("--path", "-p", help="The path to the directory")] = os.getcwd(),
             recursion: Annotated[bool, typer.Option("--recursion", "-r", help="If you want to git pull for the sub folder")] = False):
    for dirpath, dirnames, filenames in os.walk(path):
        if '.git' in dirnames:
            print(f'Updating repository in {dirpath}')
            subprocess.run(['git', 'pull'], cwd=dirpath)
            if not recursion:
                dirnames[:] = []  # Skip subdirectories in this git repository