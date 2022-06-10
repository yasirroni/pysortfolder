import os


class PySortFolder:
    def __init__(self, path):
        self.path = path
        # TODO: check if path is folder
        self._tree = None
        # self._root = None

    # def print_root()
    #     pass

    # def get_root(self, reverse=False):
    #     self._root = None
    #     return self._root

    def print_tree(self, reverse=False):
        import json

        if self._tree is None:
            self.get_tree(reverse=reverse)
        print(json.dumps(self._tree, sort_keys=False, indent=4))

    def get_tree(self, reverse=False):
        """Sort folders and files by size in tree like dict

        # folder = {
        #     'name':,
        #     'path':,
        #     'size':,
        #     'childrens':
        # }

        # files = {
        #     'name':,
        #     'path':,
        #     'size':,
        #     'childrens':
        # }

        Args:
            reverse (bool, optional):
                Descend if True, ascend if false. Defaults to False.

        Returns:
            dict: Folder tree in dict
        """
        dirpaths_buffer = {}
        for dirpath, dirs, files in os.walk(self.path, topdown=False):
            folder_node = {
                'name': os.path.basename(dirpath),
                'path': dirpath,
                'size': 0,
                'childrens': [dirpaths_buffer[os.path.join(dirpath, dir)]
                              for dir in dirs]
            }

            # ?: should we delete the key in dirpaths_buffer dict after the pick?

            folder_node['childrens'].sort(
                key=lambda x: x['size'], reverse=reverse
            )

            file_node = []
            for file_name in files:
                file_path = os.path.join(dirpath, file_name)

                file_node.append({
                    'name': file_name,
                    'path': file_path,
                    'size': os.path.getsize(file_path),
                })

            file_node.sort(
                key=lambda x: x['size'], reverse=reverse
            )

            folder_node['childrens'].extend(file_node)
            folder_node['size'] = sum(i['size'] for i in folder_node['childrens'])

            dirpaths_buffer[dirpath] = folder_node

        self._tree = folder_node
        return self._tree
