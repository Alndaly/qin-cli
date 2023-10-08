# 有趣的工具集脚本

> 开发中

## 下载

```shell
pip install qin
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
