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

## Download

### Download from pip (Recommended)

```shell
pip install qin
```

### Clone the Project

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

If the media file is a video, it will be automatically converted to mp3 format.

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





