`readline()` is an R function used to **read a single line of text typed by the user** from the **keyboard**.

> Think of it as: “Pause the program and wait for the user to type something.”


---
## Basic syntax

`readline(prompt = "something")`

- It **always returns a character string**
    
- It reads **one line only**
    

---

## Simple example

`name <- readline("Enter your name: ")`

User types:

`Milad`

Result:
```
name
# output: [1] "Milad"
```

---

## Important thing to remember

Even if the user types a number:

`age <- readline("Enter your age: ")`

User types:

`22`

R stores it as:

`age`
`[1] "25"`
`class(age) # [1] "character"`

- `readline()` **does NOT convert types**

---

## Converting input to numbers

You must convert it yourself:

`age <- as.numeric(readline("Enter your age: "))`

---

## Why use `readline()`?

Use `readline()` when:

- You want **interactive input**
    
- You are writing **scripts that ask the user questions**
    
- You want simple input during program execution
    

---

## `readline()` vs `scan()`

|Feature|`readline()`|`scan()`|
|---|---|---|
|Reads|One line|Many values|
|Input|Keyboard|File or keyboard|
|Output|Character string|Atomic vector|
|Type conversion|No|Yes|
|Interactive|Yes|Yes|

---

## Example comparison

### Using `readline()`

`x <- readline("Enter a value: ")`

### Using `scan()`

`x <- scan(n = 1)`

---

## Common use case
```
name <- readline("What is your name? ") 
age  <- as.numeric(readline("How old are you? "))

cat("Hello", name, "- you are", age, "years old\n")
```

---

## Limitations of `readline()`

❌ Can only read **one line**  
❌ Always returns **character**  
❌ Not suitable for reading files or datasets

---

## Summary (one sentence)

> **`readline()` reads a single line of user input from the keyboard and returns it as a character string.**