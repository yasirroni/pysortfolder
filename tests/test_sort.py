import pysortfolder
from pysortfolder import SortFolders, SortFoldersAndFiles


class TestSort:
    """Test using pytest
    pytest --lf -rA -c pyproject.toml --cov-report term --cov=pysortfolder tests/
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
        # TODO: os based size
        # assert sf.dir_size() == 82 # ubuntu
        # assert sf.dir_size() == 87 # ubuntu
        assert isinstance(sf.dir_size(), int)

    def test_version(self):
        assert isinstance(pysortfolder.__version__, str)
