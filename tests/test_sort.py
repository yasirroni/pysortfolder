from sortfolder import SortFolders, SortFoldersAndFiles

import os


class TestSort:
    def test_sort_folders(self):
        print(SortFolders(dir_path="tests/data").sort_by_size())

    def test_sort_folders_and_files(self):
        print(SortFoldersAndFiles(dir_path="tests/data").sort_by_size())

    def test_check_current_folder_size(self):
        sf = SortFolders(dir_path="tests/data")
        sf.dir_size()
