# pysortfolder

Sort folders and files by size and display it in folder tree format.

## Usage

```python
from pysortfolder import PySortFolder


sf = PySortFolder(path='PATH/TO/ROOT/FOLDER')
sf.make_tree(reverse=True)  # True for descend, False for ascend
sf.print_tree(prefix='',
              level=2,
              only_directories=False,
              print_current=True,
              unit='byte')

# data, size: 82 byte
# ├── subfolder3, size: 0 byte
# │   └── subsubfolder2, size: 0 byte
# │       └── subsubsubfolder1, size: 0 byte
# │           ├── subsubsubsubfolder1, size: 0 byte
# │           └── subsubsubfolder1_text1.txt, size: 0 byte
# ├── subfolder2, size: 17 byte
# │   └── subfolder2_text1.txt, size: 17 byte
# ├── subfolder1, size: 54 byte
# │   ├── subsubfolder1, size: 20 byte
# │   │   └── subsubfolder1_text1.txt, size: 20 byte
# │   ├── subfolder1_text1.txt, size: 17 byte
# │   └── subfolder1_text2.txt, size: 17 byte
# └── root_text1.txt, size: 11 byte
```

```python
from pysortfolder import dir_size

print(dir_size(path='PATH/TO/ROOT/FOLDER')) # print the size of the root

# 82
```
