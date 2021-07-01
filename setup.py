from setuptools import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='rule34-api-wrapper',
    version='1.0.0',
    description="Interact with rule34.xxx via python",
    packages=["r34 api wrapper"],
    install_requires = ['bs4'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)