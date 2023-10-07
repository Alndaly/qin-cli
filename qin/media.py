import os
import ffmpeg
import typer
from rich import print
from typing import Annotated, Optional

media_app = typer.Typer()

@media_app.command("convert")
def convert(input_file: Annotated[str, typer.Option("--input-file", "-i")], output_file: Annotated[str, typer.Option("--output-file", "-o")]):
    if not os.path.exists(input_file):
        print(f"文件[bold]{input_file}[/bold]不存在")
        raise typer.Abort()
    ffmpeg.input(input_file).output(output_file).run()
    print(f"转换成功")