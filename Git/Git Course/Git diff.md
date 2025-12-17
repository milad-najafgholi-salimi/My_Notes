In Git, **`diff`** is used to **show changes between files, commits, or states of your repository**. It answers the question: _“What changed, and how?”_

---

## What `git diff` shows

`git diff` displays **line-by-line differences**:

- **Added lines** → start with `+`
    
- **Removed lines** → start with `-`
    
- **Unchanged context** → no prefix
    

Example output:
```
- console.log("Hello");
+ console.log("Hello, world!");
```
---

## Common `git diff` uses

### 1. See unstaged changes (working directory vs staging area)
```
git diff
```
Shows changes you made **but haven’t staged yet**.

---

### 2. See staged changes (staging area vs last commit)
```
git diff --staged
# or
git diff --cached
```

Shows what will be included in the **next commit**.

---

### 3. Compare two commits
```
git diff commit1 commit2
```

Example:
```
git diff HEAD~1 HEAD
```

Shows what changed in the last commit.

---

### 4. Compare a file between commits
```
git diff commit1 commit2 -- path/to/file
```

---

### 5. See changes since last commit (staged + unstaged)
```
git diff HEAD
```

---

### 6. Word-level diff (useful for text/docs)
```
git diff --word-diff
```

Highlights individual word changes instead of whole lines.

---

### 7. Summary of changes (no content)
```
git diff --stat
```

Example output:
```
 file1.js | 4 ++--
 file2.py | 10 +++++-----
```

---

## Diff in branches

Compare branches:
```
git diff main feature-branch
```

Shows what `feature-branch` changes compared to `main`.

---

## How to read a diff header
```
diff --git a/app.js b/app.js
index e69de29..4b825dc 100644
```

- `a/` → old version
    
- `b/` → new version
    
- `index` → internal Git hash info
    

---

## When `git diff` is most useful

- Before committing → **review changes**
    
- During code reviews
    
- Debugging regressions
    
- Understanding what changed between releases

# Point
`diff` alone is a unix command that can be used in terminal; There is useful package called **kdiff3** that show you differences in a beautiful graphical panel. 
Working with **diff** and **patch** is really useful to learn.