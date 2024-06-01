import os
import ffmpeg
import typer
import time
import yt_dlp
from rich import print
from typing import Annotated
from pathlib import Path
from pydub import AudioSegment
from moviepy.editor import VideoFileClip, AudioFileClip

media_app = typer.Typer(help="Media related commands")

def is_video_file(filepath: str):
    try:
        # 尝试加载文件作为视频文件
        video = VideoFileClip(filepath)
        video.close()
        return True
    except Exception as e:
        return False

def is_audio_file(filepath: str):
    try:
        # 尝试加载文件作为音频文件
        audio = AudioSegment.from_file(filepath)
        return True
    except Exception as e:
        return False

@media_app.command("2gif", help="Convert video to gif")
def to_gif(input_file: Annotated[str, typer.Option("--input-file", "-i", help="The path to your file you wang to convert to gif")], output_file: Annotated[str, typer.Option("--output-file", "-o", help="The path to the gif file")]):
    video = VideoFileClip(input_file)
    video.write_gif(output_file)
    
@media_app.command("cut", help="Cut video or audio file")
def cut(input_file: Annotated[str, typer.Option("--input-file", "-i", help="The path to the file you want to cut")], start_time: Annotated[str, typer.Option("--start-time", "-s", help="The start time of the clip (in seconds)")], end_time: Annotated[str, typer.Option("--end-time", "-e", help="The end time of the clip (in seconds)")], output_file: Annotated[str, typer.Option("--output-file", "-o",  help="The path of the cutted file")] = None):
    file_item = Path(input_file)
    if output_file is None:
        output_file = f"{file_item.stem} cutted{file_item.suffix}"
    if is_video_file(input_file):
        # 视频文件
        video = VideoFileClip(input_file)
        # 剪切视频
        video_cut = video.subclip(start_time, end_time)
        # 保存剪切后的视频
        video_cut.write_videofile(output_file, codec="libx264")
    elif is_audio_file(input_file):
        # 音频文件
        audio = AudioFileClip(input_file)
        # 剪切视频
        audio_cut = audio.subclip(start_time, end_time)
        # 保存剪切后的视频
        audio_cut.write_audiofile(output_file)

@media_app.command("convert", help="Convert video or audio file to another format")
def convert(input_file: Annotated[str, typer.Option("--input-file", "-i", help="The path to the file you want to convert")], output_file: Annotated[str, typer.Option("--output-file", "-o", help="The path to the file converted")]):
    if not os.path.exists(input_file):
        print(f"文件[bold]{input_file}[/bold]不存在")
        raise typer.Abort()
    ffmpeg.input(input_file).output(output_file).run()

@media_app.command("download", help="Download media from url")
def download(url: Annotated[str, typer.Option("--url", "-u", help="The url of the media you want to download")], format: Annotated[str, typer.Option("--format", "-f", help="The format of the media you want to get. (now only support mp4 or mp3)")]):
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