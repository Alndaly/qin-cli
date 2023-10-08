# 有趣的工具集脚本

> 开发中

## 下载

### 从pip下载

```shell
pip install qin
```

### 克隆本项目

```shell
git clone git@github.com:Alndaly/qin-cli.git
cd qin-cli
python setup.py sdist
pip install .
```

## 脚本相关文件初始化

> 下载之后必须做这一步，涉及到垃圾箱暂存文件夹和脚本配置文件的初始化

```shell
qin init
```

## 媒体文件转格式

```shell
qin media convert -i /usr/test.flac -o /usr/test.mp3
```

- `-i` 源文件
- `-o` 转码后的文件

## 文件删除

```shell
qin file delete -p path/to/dir -i test -r
```

- `-p` 要删除的文件的父级根目录
- `-r` 是否递归子文件夹
- `-i` 要删除的文件的名称中必须包含的字符
- `-f` 是否直接删除文件（默认False，将会将文件转到垃圾文件夹）
