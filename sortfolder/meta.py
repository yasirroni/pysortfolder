import os


class MetaSortFolders:
    def __init__(self, dir_path):
        self.dir_path = dir_path

    def dir_size(self):
        return self._dir_size(path=self.dir_path)

    @staticmethod
    def _dir_size(path=None):
        """Get size in bytes

        Args:
            path (str): path in str compatible by os.path()

        Returns:
            int: size in bytes
        """
        total_size = 0
        for dirpath, _, filenames in os.walk(path):
            for i in filenames:
                f = os.path.join(dirpath, i)
                total_size += os.path.getsize(f)
        return total_size

class SortFolders(MetaSortFolders):
    def sort_by_size(self, reverse=False):
        dirlist = os.listdir(self.dir_path)
        folders = []
        for e in dirlist:
            filepath = os.path.join(self.dir_path, e)
            if os.path.isdir(filepath):
                folders.append({"foldername":e, "filepath":filepath, "size":self._dir_size(filepath)})
        folders.sort(key=lambda foldername: foldername['size'], reverse=reverse)
        return folders


class SortFoldersAndFiles(MetaSortFolders):
    def sort_by_size(self, reverse=False):
        dirlist = os.listdir(self.dir_path)
        folders = []
        files = []
        for e in dirlist:
            filepath = os.path.join(self.dir_path, e)
            if os.path.isdir(filepath):
                folders.append({"foldername":e, "filepath":filepath, "size":self._dir_size(filepath)})
            else:
                files.append({"filename":e, "filepath":filepath, "size":os.path.getsize(filepath)})
        folders.sort(key=lambda foldername: foldername['size'], reverse=reverse)
        files.sort(key=lambda filename: filename['size'], reverse=reverse)
        return folders, files
