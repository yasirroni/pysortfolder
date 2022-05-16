from sortfolder import SortFolders

import os


class TestSort:
    def test_sort(self):
        print(SortFolders(dir_path="tests/data", reverse=True).sort_by_size)
