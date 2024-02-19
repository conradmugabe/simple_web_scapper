import os
from setuptools import setup


setup(
    name="simple_web_scrapper",
    version="1.0.0",
    description="web scrapper to get company emails on facebook",
    long_description=open(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md")
    ).read(),
    long_description_content_type="text/markdown",
    author="Conrad Mugabe",
    packages=["scrapper"],
)
