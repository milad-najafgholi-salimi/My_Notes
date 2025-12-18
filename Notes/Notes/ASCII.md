**ASCII** stands for **American Standard Code for Information Interchange**.

It’s a **character encoding standard**—a system that maps characters to numbers so computers can store and exchange text consistently.

---

## What ASCII Does

ASCII assigns a **numeric value** to letters, digits, punctuation, and control characters.

For example:

- `A` → **65**
    
- `a` → **97**
    
- `0` → **48**
    
- Space → **32**
    
- Newline (line break) → **10**
    

Computers store these numbers in binary, but we humans see the characters.

---

## ASCII Character Set

ASCII uses **7 bits**, allowing **128 total characters (0–127)**.

### 1. Control Characters (0–31, 127)

These don’t display as symbols; they control text or devices.  
Examples:

- `0` → NUL (null)
    
- `9` → TAB
    
- `10` → LF (line feed / newline)
    
- `13` → CR (carriage return)
    
- `127` → DEL
    

### 2. Printable Characters (32–126)

These are visible characters:

- **32** → Space
    
- **48–57** → Digits (`0–9`)
    
- **65–90** → Uppercase letters (`A–Z`)
    
- **97–122** → Lowercase letters (`a–z`)
    
- **33–47, 58–64, 91–96, 123–126** → Punctuation and symbols
    

---

## Example

The word **"Hi"** in ASCII:

- `H` → 72 → `01001000`
    
- `i` → 105 → `01101001`
    

So computers store `"Hi"` as a sequence of numbers (and ultimately bits).

---

## Why ASCII Matters

- It was one of the **first universal text standards**
    
- Enabled **text sharing across different computers**
    
- Still forms the **foundation of modern encodings**
    

---

## ASCII vs Unicode

- **ASCII**: 128 characters, English-focused
    
- **Unicode**: Supports **hundreds of thousands** of characters (emojis, Chinese, Arabic, accents, symbols, etc.)
    
- **UTF-8** (a Unicode encoding) is backward-compatible with ASCII, meaning:
    
    - ASCII text is valid UTF-8
        

---

## In Short

ASCII is:

- A way to represent text as numbers
    
- Simple, old, and extremely influential
    
- Still relevant today as the core of modern text systems