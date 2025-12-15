`scan()` is a **basic R function used to read data into R**.  
It reads **values** (like numbers or words) from a file, keyboard input, or other connections and stores them as a **vector**.

`scan()` is a **low-level, fast** way to load such data when:

- The data is simple
    
- You don’t need a full table or data frame
    

---

## Simple example (numbers)

Suppose a file `data.txt` contains:

`10 20 30 40`

```
x <- scan("data.txt")
x

# output: [1] 10 20 30 40
```
R automatically recognized these as numbers 
Output is a **numeric vector**

---
## Reading character data

If your data is text, you must tell R what type to expect:

`apple banana orange`

```
fruits <- scan("fruits.txt", what = character())
fruits

# output: [1] "apple" "banana" "orange"
```
---
## Reading from the keyboard

You can even type data directly:
```
x <- scan()
# will directly save in x variable as you input from keyboard.
```
### For characters
```
x <- scan(what = character())
```
---
## Important arguments

### `what`

Specifies **what type of data** to read.

`scan("file.txt", what = numeric())` 
`scan("file.txt", what = character())`

---

### `sep`

Tells R how values are separated.

`scan("data.csv", sep = ",")`

---

### `skip`

Skips lines at the beginning (useful for headers).

`scan("data.txt", skip = 1)`

---

### `quiet`

Suppresses messages.

`scan("data.txt", quiet = TRUE)`

---

## What does `scan()` return?

Always an **[[atomic vector]]**:

- numeric
    
- character
    
- logical
    
- complex
    
```
class(scan("data.txt")) # "numeric"
```
---

## What `scan()` is NOT good for

❌ Reading tables with rows and columns  
❌ Reading complex datasets with headers  
❌ Text processing line-by-line

For those, use:

- `read.table()`
    
- `read.csv()`
    
- `readLines()`
    

---

## Summary (one sentence)

> **`scan()` reads simple, structured data into a vector quickly and efficiently.**