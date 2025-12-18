A **config** (short for **configuration**) is **settings that tell a program how to behave**.

Instead of changing the program’s code, you change its **config**.

---

## Everyday analogy

Think of a TV:

- Brightness, volume, language → **config**
    
- The TV’s electronics → **code**
    

You don’t rewrite the TV to change the volume — you change the settings.

---

## Examples

### 1. Config file

A file that stores settings.

Examples:

- `.gitconfig`
    
- `config.yaml`
    
- `settings.json`
    
- `.env`
    

Example:
```
user.name = Milad
user.email = milad.najafgholi.salimi@gmail.com
```

---

### 2. Config in Git

Git’s config tells Git who you are and how to behave.
```
git config --global user.name "Milad Salimi"
git config --global user.email "milad.najafgholi.salimi@gmail.com"
```

---

### 3. Config in apps

- Language
    
- Theme
    
- File paths
    
- Ports
    
- Debug mode (on/off)
    

Example:
```
{
  "port": 3000,
  "debug": true
}
```

---

## Where configs live

- Files (most common)
    
- Environment variables
    
- Command-line flags
    
- Databases (sometimes)
    

---

## Why configs exist

- Change behavior **without editing code**
    
- Different settings for dev / test / prod
    
- Easier maintenance
    
- Customization per user or machine
    

---

## What a config is NOT

- Not the program itself
    
- Not data the program processes
    
- Not temporary output
    

---

## Summary

**A config is a collection of settings that control how software behaves.**
