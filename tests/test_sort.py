import sortfolder
from sortfolder import SortFolders, SortFoldersAndFiles

import os


class TestSort:
    """Test using pytest
    pytest --lf -rA -c pyproject.toml --cov-report term --cov=sortfolder tests/
    """
    def test_sort_folders(self):
        sf = SortFolders(dir_path="tests/data")
        print(sf.sort_by_size())
        print(SortFolders(dir_path="tests/data").sort_by_size())

    def test_sort_folders_and_files(self):
        sf = SortFoldersAndFiles(dir_path="tests/data")
        print(sf.sort_by_size())
        print(SortFoldersAndFiles(dir_path="tests/data").sort_by_size())

    def test_check_current_folder_size(self):
        sf = SortFolders(dir_path="tests/data")
        print(sf.dir_size())
        assert sf.dir_size() == 77 
        assert type(sf.dir_size()) == int

    def test_version(self):
        assert type(sortfolder.__version__) == str
