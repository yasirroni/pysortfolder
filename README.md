# sortfolder

## Usage

Checking current root size in bytes

```python
from sortfolder import SortFolders

sf = SortFolders(dir_path="PATH/TO/ROOT/FOLDER")
sf.dir_size()
```

Sort all folder in root by size in bytes

```python
from sortfolder import SortFolders

sf = SortFolders(dir_path="PATH/TO/ROOT/FOLDER")
print(sf.sort_by_size())
```

## Akcnowledgement

Source: https://pytutorial.com/python-sort-folders-by-size
