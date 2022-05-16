from sortfolder import SortFolders, SortFoldersAndFiles

import os


class TestSort:
    def test_sort_folders(self):
        print(SortFolders(dir_path="tests/data", reverse=True).sort_by_size)

    def test_sort_folders_and_files(self):
        print(SortFoldersAndFiles(dir_path="tests/data", reverse=True).sort_by_size)
