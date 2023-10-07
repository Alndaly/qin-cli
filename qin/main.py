import typer
import os
from rich import print
from .file import file_app
from .config import config
from .media import media_app

app = typer.Typer()
app.add_typer(file_app, name='file')
app.add_typer(media_app, name='media')


def create_root():
    if not os.path.exists(config.ROOT_PATH):
        os.mkdir(config.ROOT_PATH)
    if not os.path.exists(config.TRASH_PATH):
        os.mkdir(config.TRASH_PATH)
    if not os.path.exists(config.CONFIG_PATH):
        with open(config.CONFIG_PATH, 'w') as fp:
            # 在这里可以写入文件内容（如果需要）
            fp.write('{}')
    print('命令配置初始化成功')


@app.command()
def init():
    create_root()
    
   
if __name__ == "__main__":
    app()
