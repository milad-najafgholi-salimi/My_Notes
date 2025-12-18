In **R**, `is.na()` is used to **identify missing values (`NA`)**.

---

## Basic Syntax

`is.na(x)`

---

## What It Does

- Returns **TRUE** where the value is `NA`
    
- Returns **FALSE** otherwise
    
- Works on vectors, matrices, data frames, and lists
    

---

## Examples

### Vector
```
x <- c(1, NA, 3)
is.na(x)
# [1] FALSE  TRUE FALSE
```
### Count missing values
```
sum(is.na(x))
# [1] 1
```

---
### Data Frame
```
df <- data.frame(
  a = c(1, NA, 3),
  b = c(NA, 5, 6)
)

is.na(df)

# output:
         a     b
[1,] FALSE  TRUE
[2,]  TRUE FALSE
[3,] FALSE FALSE
```
To count `NA`s per column:
```
colSums(is.na(df))

# output:
a b 
1 1
```
---

### Subset rows with missing values
```
df[is.na(df$a), ]
```
Remove rows with any `NA`:
```
df[!is.na(df$a), ]
```
---

## `is.na()` vs `== NA`

❌ **Incorrect**

`x == NA`

✔ **Correct**

`is.na(x)`

Reason: `NA` is not a value—it represents _missingness_, so comparisons with `==` don’t work.

---

## Related Functions

|Function|Purpose|
|---|---|
|`na.omit()`|Remove rows with `NA`|
|`complete.cases()`|Identify rows without any `NA`|
|`anyNA()`|Check if any `NA` exists|
|`replace()`|Replace `NA` values|

Example:
```
x[is.na(x)] <- 0
```

### Removing NA from result
In the following example we want to take **mean** but there are NA in values that we don't want them to count. So we need to remove them with `na.rm = T` option:
```
mean(data$Time, na.rm = T)
```
If contain NA, the output will be NA and doesn't. So we have to remove NA from values.