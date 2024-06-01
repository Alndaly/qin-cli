#!/usr/bin/env python
# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

with open("./README.md", "r", encoding="utf-8") as fp:
    long_description = fp.read()

with open("./LICENSE", "r", encoding="utf-8") as fp:
    license = fp.read()
    
setup(
    name="qin",
    version="0.0.1",
    keywords=["pip", "tools"],
    description="Interesting toolset",
    entry_points={
        'console_scripts': [
            'qin = qin.main:app'
        ]
    },
    python_requires='>=3.10',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license=license,
    url="https://github.com/Alndaly/qin-cli",
    author="Kinda Hall",
    maintainer="Kinda Hall",
    maintainer_email="1142704468@qq.com",
    author_email="1142704468@qq.com",
    packages=find_packages(),
    include_package_data=True,
    platforms="macOS",
    install_requires=['typer', 'ffmpeg-python', 'oss2', 'gradio', 'yt-dlp', 'fastapi', 'moviepy']
)
