- You should close the file after using with `close("file_name")`.
```
close(file("testing.txt", open = "rw"))
```
To work better and easier, take help from variables like below:
```
file <- file("testing.txt", open="rw")
close(file)
```
