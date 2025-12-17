`diff` is a classic Unix command.
**`diff`** compares **two files or directories** and reports **how they differ**.
## Basic usage

### Compare two files

`diff file1.txt file2.txt`

If they are identical → **no output**

---

## How to read `diff` output

Example:
```
3c3
< Hello
---
> Hello, world
```

Meaning:

- Line 3 was **changed**
    
- `<` = content from first file
    
- `>` = content from second file
    

---

## Common and important options

### Unified diff (most used)

`diff -u file1 file2`

Output:
```
--- file1
+++ file2
@@ -1 +1 @@
-Hello
+Hello, world
```
This format is:

- easier to read
    
- used by **Git**
    
- used by **patch**
    

---

### Side-by-side view

`diff -y file1 file2`

---

### Compare directories

`diff -r dir1 dir2`

---

## What `diff` works best with

- Text files
    
- Source code
    
- Config files
    
- Logs
    

❌ Not useful for binary files (images, videos)

---

## Is `diff` related to Git?

- `diff` existed **long before Git**
    
- Git **adopted the same idea and format**
    
- `git diff` is **Git-aware**
    
- `diff` is **version-control unaware**
    

---

## Where `diff` comes from

- Originated in **early Unix (1970s)**
    
- Standardized by **POSIX**
    
- Available on:
    
    - Linux
        
    - macOS
        
    - BSD
        
    - Windows (via WSL, Git Bash, Cygwin)
        

---

## Summary

- ✅ `diff` is a **Unix command**
    
- Compares **files/directories**
    
- Outputs **line-based differences**
    
- Foundation for tools like Git and patch