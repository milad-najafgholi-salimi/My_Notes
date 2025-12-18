An **atomic vector** is the **simplest data structure in R**.

> It is a **one-dimensional collection of values where every element is the same type**.

---

## Why “atomic”?

“Atomic” means **indivisible**:

- Each element is a **single value**
    
- You cannot break elements into smaller R objects
    

---

## The 6 atomic vector types in R

R has **six** atomic vector types:

|Type|Example|
|---|---|
|`logical`|`TRUE FALSE TRUE`|
|`integer`|`1L 2L 3L`|
|`numeric` (double)|`1.5 2.3 10`|
|`character`|`"a" "b" "hello"`|
|`complex`|`1+2i`|
|`raw`|Rare, low-level|

---

## Example of atomic vectors

### Numeric vector

`x <- c(1, 2, 3)`

All elements are numeric → atomic vector.

---

### Character vector

`y <- c("apple", "banana", "orange")`

All elements are character → atomic vector.

---

### Logical vector

`z <- c(TRUE, FALSE, TRUE)`

---

## Key rule: one type only

An atomic vector **can only contain one type**.

If you mix types, R **coerces** them:

`c(1, "a", 3) # [1] "1" "a" "3"`

Everything becomes **character**.

---

## Atomic vector vs list (very important)

### Atomic vector

`v <- c(1, 2, 3)`

- One type
    
- Simple values
    

### List (not atomic)

`l <- list(1, "a", TRUE)`

- Different types allowed
    
- Each element can be anything
    

---

## Why does `scan()` return an atomic vector?

Because:

- `scan()` reads **values**
    
- It assumes the data is **simple and uniform**
    
- So it returns the **simplest structure possible**
    

Example:
```
scan("numbers.txt") # numeric atomic vector
```
---
## Summary (exam-friendly)

> An **atomic vector** is a one-dimensional R object that contains elements of **only one data type**.