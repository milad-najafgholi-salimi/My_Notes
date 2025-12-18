`head()` and `tail()` are **utility functions** in R used to **quickly look at parts of an object**.

- **`head()`** → shows the **first elements**
    
- **`tail()`** → shows the **last elements**
---
## Basic syntax

`head(x, n = 6)` 
`tail(x, n = 6)`

- `x` → any R object (vector, data frame, matrix, etc.)
    
- `n` → number of elements to show (default is 6)
    

---

## Example with a vector

`x <- 1:20`

### `head()`

`head(x)`
`# [1] 1 2 3 4 5 6`

### `tail()`

`tail(x)`
`# [1] 15 16 17 18 19 20`

### Specify `n`

`head(x, 3)` 
`# [1] 1 2 3`

`tail(x, 4)` 
`# [1] 17 18 19 20`

---

## Example with a data frame

`df <- data.frame(   name = c("A", "B", "C", "D", "E"),   score = c(90, 85, 88, 92, 80) )`

### `head(df)`

Shows first rows:
```
  name score
1    A    90
2    B    85
3    C    88
4    D    92
5    E    80

```

### `tail(df, 2)`
```
  name score
4    D    92
5    E    80

```

---

## Works on many R objects

### Matrix
```
m <- matrix(1:12, nrow = 4)
head(m)
```
### List
```
lst <- list(1, 2, 3, 4, 5, 6, 7)
head(lst, 3)
```
---

## Why are `head()` and `tail()` useful?

✔ Quickly inspect large datasets  
✔ Check if data loaded correctly  
✔ See column names and values  
✔ Debug code without printing everything

---

## A very common workflow
```
df <- read.csv("data.csv")
head(df)
tail(df)
```

This lets you:

- See the **structure**
    
- Check for **missing or strange values**
    
- Confirm **column order**
    

---

## Summary

> **`head()` shows the beginning of an object, and `tail()` shows the end.**