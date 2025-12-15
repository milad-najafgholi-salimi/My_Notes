- `system.file()` provides path for library files and packages:
```
system.file()

# For example in Linux output will be like: "/usr/lib/R/library/base"
```
You can change directory via setting a parameter. Example:
```
system.file(package = "class")
```
It won't change your current working directory.
