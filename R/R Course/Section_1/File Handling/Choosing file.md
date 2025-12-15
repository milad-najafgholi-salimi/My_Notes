`file.choose()` function will let you choose file in graphical environment and *only returns file's path* - Can be used like this:
```
f <- file.choose()
txt <- readLines(f)
txt
```
