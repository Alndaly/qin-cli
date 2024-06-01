import os
import ffmpeg
import typer
import time
import yt_dlp
from rich import print
from typing import Annotated

media_app = typer.Typer()

@media_app.command("convert")
def convert(input_file: Annotated[str, typer.Option("--input-file", "-i")], output_file: Annotated[str, typer.Option("--output-file", "-o")]):
    if not os.path.exists(input_file):
        print(f"文件[bold]{input_file}[/bold]不存在")
        raise typer.Abort()
    ffmpeg.input(input_file).output(output_file).run()

@media_app.command("download")
def download(url: Annotated[str, typer.Option("--url", "-u")], format: Annotated[str, typer.Option("--format", "-f")]):
    download_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    # 定义下载选项
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': f'{download_time} - %(title)s.%(ext)s',  # 自定义文件名和文件夹结构
    }
    if format == 'mp3':
        ydl_opts.update({
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '0',
            }],
        })
    elif format == 'mp4':
        ydl_opts.update({
            'postprocessors': [
                {
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4'
                },
                {
                    'key': 'EmbedThumbnail',  # 嵌入缩略图
                },
            ]
        })

    # 使用yt_dlp下载视频并提取音频
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])