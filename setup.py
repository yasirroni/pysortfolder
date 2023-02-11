import os
import re

from setuptools import setup

PACKAGE_NAME = "pysortfolder"

current_path = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(current_path, PACKAGE_NAME, 'version.py'), "rt") as f:
    version_line = f.read()

m = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_line, re.M)
__version__ = m.group(1)

setup(
    version=__version__,
    license="MIT license",
)
