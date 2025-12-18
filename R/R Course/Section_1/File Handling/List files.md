To listing files in your current working directory, use `list.files()`:
```
list.files()
```

Also you can see other directories with absolute path:
```
last.files("enter path here")
```
You can list files with specific patterns by using `pattern = "your pattern"` option:
```
list.files(pattern = "my")
```
This will returns all files and directories contains that pattern. Doesn't matter the pattern is at the beginning, at the end or is at the middle.
