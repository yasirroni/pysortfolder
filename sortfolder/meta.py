import os


class SortFolders():
    def __init__(self, dir_path, reverse=True):
        self.dir_path = dir_path
        self.reverse = reverse

    def dir_size(self, path):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for i in filenames:
                f = os.path.join(dirpath, i)
                total_size += os.path.getsize(f)
        return total_size

    @property
    def sort_by_size(self):
        files = os.listdir(self.dir_path)
        folders = []
        for e in files:
            filepath = os.path.join(self.dir_path, e)
            if os.path.isdir(filepath):
                folders.append({"filename":e, "filepath":filepath, "size":self.dir_size(filepath)})
        folders.sort(key=lambda filename: filename['size'], reverse=self.reverse)
        return folders
