#!/usr/bin/env python
# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="qin",
    version="0.0.2",
    keywords=("pip", "tools"),
    description="cli tool",
    entry_points={
        'console_scripts': [
            'qin = qin.main:app'
        ]
    },
    python_requires='>=3.7',
    long_description="有趣的工具集",
    license="MIT Licence",
    url="https://github.com/Alndaly/qin-cli",
    author="Kinda Hall",
    maintainer="Kinda Hall",
    maintainer_email="1142704468@qq.com",
    author_email="1142704468@qq.com",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=['typer', 'ffmpeg-python']
)
