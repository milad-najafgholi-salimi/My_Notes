## Short answer

`sudo apt update`

**updates the list of available software**, **not** the software itself.

---

## What it actually updates

APT keeps a **local database (index)** of:

- what packages exist
    
- what versions are available
    
- where to download them from
    

`apt update` **refreshes this database** by talking to the repositories.

Think of it like **updating an app store catalog**, not installing updates.

---

## What it does step by step

1. Reads repository URLs from:
    
    - `/etc/apt/sources.list`
        
    - `/etc/apt/sources.list.d/*.list`
        
2. Connects to those servers
    
3. Downloads **package lists** (metadata), such as:
    
    - package names
        
    - versions
        
    - dependencies
        
    - checksums
        
4. Stores them locally in:
    
    `/var/lib/apt/lists/`
    

---

## What it does NOT do ❌

- Does NOT upgrade installed software
    
- Does NOT install anything
    
- Does NOT remove anything
    

---

## Then how do I actually update software?

### Upgrade installed packages

`sudo apt upgrade`

### Full upgrade (handles dependency changes)

`sudo apt full-upgrade`

---

## Why you should run `apt update` first

If you don’t:

- APT doesn’t know about new versions
    
- You may install **outdated packages**
    
- You may miss **security updates**
    

That’s why you often see:

`sudo apt update && sudo apt upgrade`

---

## Summary

- `apt update` → **refreshes the package list**
    
- `apt upgrade` → **updates the software**
    
- `apt install` → **installs software**