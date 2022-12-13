import pysortfolder
from pysortfolder import PySortFolder, dir_size

path = "tests/data"


"""Test using pytest
pytest --lf -rA -c pyproject.toml --cov-report term --cov=pysortfolder tests/
"""


def test_get_tree():
    sf = PySortFolder(path=path)
    tree = sf.get_tree()
    assert isinstance(sf._tree, dict)
    assert isinstance(tree, dict)


def test_print_tree():
    PySortFolder(path=path).print_tree()


def test_check_current_folder_size():
    size = dir_size(path=path)
    # TODO: os based size
    # assert size == 82 # ubuntu
    # assert size == 87 # ubuntu
    assert isinstance(size, int)


def test_version():
    assert isinstance(pysortfolder.__version__, str)
