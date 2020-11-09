# -*- coding: utf-8 -*- 

import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="example-pkg-jingwoo4710", # pip 으로 설치한 패키지 이름입니다
    version="0.0.1",
    author="Jaywoo Lee",
    author_email="jaewoo4710@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jingwoo4710/example-day1",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)