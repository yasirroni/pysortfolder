import os


class SortFolders():
    def __init__(self, dir_path, reverse=True):
        self.dir_path = dir_path
        self.reverse = reverse

    def dir_size(self, path):
        total_size = 0
        for dirpath, _, filenames in os.walk(path):
            for i in filenames:
                f = os.path.join(dirpath, i)
                total_size += os.path.getsize(f)
        return total_size

    @property
    def sort_by_size(self):
        dirlist = os.listdir(self.dir_path)
        folders = []
        for e in dirlist:
            filepath = os.path.join(self.dir_path, e)
            if os.path.isdir(filepath):
                folders.append({"foldername":e, "filepath":filepath, "size":self.dir_size(filepath)})
        folders.sort(key=lambda foldername: foldername['size'], reverse=self.reverse)
        return folders


class SortFoldersAndFiles():
    def __init__(self, dir_path, reverse=True):
        self.dir_path = dir_path
        self.reverse = reverse

    def dir_size(self, path):
        total_size = 0
        for dirpath, _, filenames in os.walk(path):
            for i in filenames:
                f = os.path.join(dirpath, i)
                total_size += os.path.getsize(f)
        return total_size

    @property
    def sort_by_size(self):
        dirlist = os.listdir(self.dir_path)
        folders = []
        files = []
        for e in dirlist:
            filepath = os.path.join(self.dir_path, e)
            if os.path.isdir(filepath):
                folders.append({"foldername":e, "filepath":filepath, "size":self.dir_size(filepath)})
            else:
                files.append({"filename":e, "filepath":filepath, "size":os.path.getsize(filepath)})
        folders.sort(key=lambda foldername: foldername['size'], reverse=self.reverse)
        files.sort(key=lambda filename: filename['size'], reverse=self.reverse)
        return folders, files
