`unlink("my_folder", recursive=T)` will delete a non-empty directory. If don't use `recursive` option, this function will only remove empty directories:
```
unlink("my_folder", recursive=T)
```
Also can use to delete files:
```
unlink("my_file.txt")
```