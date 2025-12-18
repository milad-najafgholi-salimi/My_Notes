The **`patch`** command is a Unix/Linux tool used to **apply changes (diffs) to files**.  
If `diff` shows _what changed_, **`patch` applies those changes**.

---

## What is a patch?

A **patch file** is usually the output of `diff` or `git diff`, saved to a file.

Example (`change.patch`):
```
--- hello.txt
+++ hello.txt
@@ -1 +1 @@
-Hello
+Hello, world
```

---

## Basic usage

### Apply a patch

`patch original_file < modified_file`

This updates the target files automatically.

---

### Apply a patch to a specific directory
```
patch -p1 < change.patch
```

`-p` controls how many directory levels to strip from file paths.

---

## Most common options

### `-pN` (VERY important)

Controls path stripping:
```
patch -p0   # use paths exactly as written
patch -p1   # strip first directory (most common)
patch -p2   # strip two directories
```

Example paths in patch:
```
--- a/src/main.c
+++ b/src/main.c
```

Apply with:

`patch -p1 < change.patch`

---

### Dry run (safe test)
```
patch --dry-run < change.patch
```

Shows what _would_ happen without changing files.

---

### Reverse a patch (undo)

`patch -R < change.patch`

---

### Apply patch to a specific file

`patch file.txt < change.patch`

---

## Creating a patch

### Using `diff`
```
diff -u old.txt new.txt > change.patch
```

### Using Git (recommended)

`git diff > change.patch`

---

## Common errors & fixes

### ❌ “Hunk FAILED”

- File changed since patch was created
    
- Wrong directory
    
- Wrong `-p` value
    

Fix:

`patch --dry-run -p1 < change.patch`

Try different `-p` values.

---

### ❌ “File to patch not found”

Paths don’t match.

Fix:

- Change directory
    
- Adjust `-p` option
    

---

## When to use `patch`

- Applying fixes emailed as `.patch` files
    
- Working without Git
    
- Applying changes to vendor code
    
- Reproducing changes across machines
    

---

## `patch` vs `git apply`

If you’re in a Git repo:

|Tool|Use when|
|---|---|
|`patch`|General Unix tool|
|`git apply`|Git-aware (preferred for Git patches)|

---
## Summary
- **`diff`** → creates a patch
    
- **`patch`** → applies a patch
    
- Use `-p1` most of the time
    
- Use `--dry-run` before applying