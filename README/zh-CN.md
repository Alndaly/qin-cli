# 有趣的工具集脚本

鉴于平时有较多的零碎工具需求，打算自己做一个脚本库。目前暂时仅支持cli。

> [!warning]
> 因我电脑用的mac，故本项目目前仅在mac上使用，其他平台暂时未经测试，如果遇到问题，请提issue。

> [!note]
> 本项目依赖于ffmpeg，请确保本地安装了ffmpeg。

## 关于项目的一些配置

- 默认配置文件为`~/.qin/config.json`。
- 默认临时垃圾文件夹为`~/.qin/trash`。

如果需要本项目的图片上传功能，请务必配置好config.json中的`oss`相关字段。

## 安装

## 下载

### 方式1：从pip下载（推荐方式）

```shell
pip install qin
```

### 方式2：克隆本项目

```shell
git clone git@github.com:Alndaly/qin-cli.git
cd qin-cli
python setup.py sdist
pip install .
```

## 媒体文件转格式

```shell
qin media convert -i /usr/test.flac -o /usr/test.mp3
```

- `-i` 源文件
- `-o` 转码后的文件

## 下载一些媒体文件

```shell
qin media download -u https://www.bilibili.com/video/BV117411J719 -f mp3
```

- `-u` 视频链接
- `-f` 视频格式 支持mp3/mp4

> 如果媒体文件是视频类型，则会自动转为mp3格式。

## 视频转gif

```shell
qin media 2gif -i /usr/test.mp4 -o /usr/test.gif
```

- `-i` 源文件
- `-o` 转好的文件

## 媒体剪切

```shell
qin media cut -i /usr/test.mp4 -s 10 -e 20 -o /output.mp4
```

- `-i` 被剪切的文件路径
- `-s` 开始时间（单位秒）
- `-e` 结束时间（单位秒）
- `-o` 输出的文件

## 文件删除

```shell
qin file delete -p path/to/dir -i test -r
```

- `-p` 要删除的文件的父级根目录
- `-r` 是否递归子文件夹
- `-i` 要删除的文件的名称中必须包含的字符
- `-f` 是否直接删除文件（默认False，将会将文件转到垃圾文件夹）

## 上传文件到aliyun oss

```shell
qin file upload -p path/to/your/file
```

- `-p` 要上传的文件的路径

## 转换pdf为png

```shell
qin file pdf2png -p path/to/your/file
```

- `p` 要转换的pdf文件路径