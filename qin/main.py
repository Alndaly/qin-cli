import typer
import json
import os

from .config.base import ROOT_PATH, TRASH_PATH, CONFIG_PATH
from .common.file import create_file

def create_root():
    if not os.path.exists(ROOT_PATH):
        os.mkdir(ROOT_PATH)
    if not os.path.exists(TRASH_PATH):
        os.mkdir(TRASH_PATH)
    if not os.path.exists(CONFIG_PATH):
        config_template = {
            "ImgBed": {
                "AccessKeyId": "",
                "AccessKeySecret": "",
                "BucketName": "",
                "EndPoint": "",
                "Folder": ""
            }
        }
        create_file(CONFIG_PATH, json.dumps(config_template))

create_root()

from .media import media_app
from .file import file_app
from .ai import ai_app

app = typer.Typer()
app.add_typer(file_app, name='file')
app.add_typer(media_app, name='media')
app.add_typer(ai_app, name='ai')
