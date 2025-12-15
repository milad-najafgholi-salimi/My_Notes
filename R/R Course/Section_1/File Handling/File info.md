to take information about a file, use `file.info("file_name")`. If your file isn't in current working directory, give **path** first, then add **file name**.
```
file.info("testing.txt")
```
In all of the R program, using `$` sign will return the specific thing you are seeking:
```
file.info("testing.txt")$isdir
# output: FALSE
```
