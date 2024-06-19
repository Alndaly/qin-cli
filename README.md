# Interesting Toolset Script

[中文说明文档](./README/zh-CN.md)

Given the frequent need for various small tools, I plan to create a script library. Currently, it only supports CLI.

> [!warning]
> Since I use a Mac, this project is currently only usable on Mac. Other platforms have not been tested yet. If you encounter any issues, please submit an issue.

> [!note]
> This project relies on ffmpeg. Please ensure ffmpeg is installed locally.

## Some Project Configurations

- The default configuration file is `~/.qin/config.json`.
- The default temporary trash folder is `~/.qin/trash`.

If you need the image upload function of this project, please make sure to configure the `oss` related fields in the `config.json` file.

## Download

### Method1: Download from pip (Recommended)

```shell
pip install qin
```

### Method2: Clone the Project

```shell
git clone git@github.com:Alndaly/qin-cli.git
cd qin-cli
python setup.py sdist
pip install .
```

## Media File Conversion

```shell
qin media convert -i /usr/test.flac -o /usr/test.mp3
```

- `-i` Source file
- `-o` Converted file

## Download Some Media Files

```shell
qin media download -u https://www.bilibili.com/video/BV117411J719 -f mp3
```

- `-u` Video URL
- `-f` Video format supports mp3/mp4

> If the media file is a video, it will be automatically converted to mp3 format.

## Video to Gif

```shell
qin media 2gif -i /usr/test.mp4 -o /usr/test.gif
```

- `-i` path of the source video file
- `-o` the path to the gif

## Media Cutting

```shell
qin media cut -i /usr/test.mp4 -s 10 -e 20 -o /output.mp4
```

- `-i` The path to the file you want to cut 
- `-s` The start time of the clip (in seconds)
- `-e` The end time of the clip (in seconds)
- `-o` The path of the cutted file

## File Deletion

```shell
qin file delete -p path/to/dir -i test -r
```

- `-p` Parent root directory of the files to be deleted
- `-r` Whether to recursively delete subfolders
- `-i` The character that must be included in the name of the file to be deleted
- `-f` Whether to delete files directly (default is False, files will be moved to the trash folder)

## Upload Files to Aliyun OSS

```shell
qin file upload -p path/to/your/file
```

- `-p` Path of the file to be uploaded

## Convert PDF to PNG

```shell
qin file pdf2png -p path/to/your/file
```

- `-p` Path to the PDF file to be converted

## Get Model Information from Model File (CivitAI)

```shell
qin ai model -p path/to/your/file
```

- `-p`: The path to the file for which you want to retrieve information

## Get Hash of Model File

```shell
qin ai hash -p path/to/your/file
```

- `-p`: The path to the file for which you want to retrieve the hash

## Update all git repositories in a directory

```shell
qin git pull -p path/to/the/dir -r
```

- `-p` The root directory of the git repositories to be updated (if `-p path/to/the/dir` is not specified, the default is the current directory)
- `-r` Whether to recursively update subfolders, default is `False`