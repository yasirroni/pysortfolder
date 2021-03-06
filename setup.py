import os
import re

from setuptools import find_packages, setup

PACKAGE_NAME = 'pysortfolder'
DESCRIPTION = "Sort folder by size"
AUTHOR = "Muhammad Yasirroni",
EMAIL = "muhammadyasirroni@gmail.com",
URL = "https://github.com/yasirroni/pysortfolder",
KEYWORDS = ['sort', 'folder', 'size']

with open("README.md", "r") as f:
    long_description = f.read()

current_path = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(current_path, PACKAGE_NAME, 'version.py'), "rt") as f:
    version_line = f.read()

m = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_line, re.M)
__version__ = m.group(1)

setup(
    name=PACKAGE_NAME,
    version=__version__,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(),
    license="MIT license",
    keywords="psst",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    python_requires='>3.6',
    install_requires=[],
    extras_require={},
)
