`git show` is a Git command used to **display detailed information about a specific Git object**, usually a commit. It’s very handy to quickly see **what changed, who changed it, and when**.

---

### Basic Usage

`git show <commit>`

- `<commit>` can be a commit hash, branch name, or HEAD.
    
- By default, it shows:
    
    1. **Commit hash**
        
    2. **Author and date**
        
    3. **Commit message**
        
    4. **Diff of changes** introduced by that commit
        

---

### Examples

1. **Show the latest commit**
    

`git show`

Equivalent to `git show HEAD`.

2. **Show a specific commit**
    

`git show 1a2b3c4d`

3. **Show only the commit message**
    

`git show --no-patch 1a2b3c4d`

4. **Show in a simplified format**
    

`git show --stat 1a2b3c4d`

- Shows **which files changed** and **number of insertions/deletions** without full diff.
    

5. **Show changes with color or word-level diff**
    

`git show --color-words 1a2b3c4d`

---

### Quick Summary

- **Purpose:** Inspect commits or objects in detail.
    
- **Default:** Shows commit info + diff.
    
- **Useful options:**
    
    - `--stat` → summary of file changes
        
    - `--name-only` → list only changed files
        
    - `--patch` or default → full changes