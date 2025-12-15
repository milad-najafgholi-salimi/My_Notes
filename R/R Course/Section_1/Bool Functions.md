If you compare a number with a vector, that number will iterate on vector and compare number with each vector's element and return TRUE or FALSE:
```
numbers <- c(1, 4, 5, 7, 9, 13)
numbers == 5

# output: FALSE FALSE  TRUE FALSE FALSE FALSE
```
You can ask which one is, with `which()` function. It will return the index; In R indexes starts from .
Example above:
```
which(numbers == 5)  # output: 3
```

### Any
`any()` function checks at least one condition is correct of not.
```
numbers <- c(1, 4, 5, 7, 9, 13)
any(numbers > 7) # output: TRUE
```

### All
To check if all conditions are TRUE or not:
```
numbers <- c(1, 4, 5, 7, 9, 13)
all(numbers > 7) # output: FALSE
```
### ! 
`!` symbol will contradict the conditions:
```
numbers <- c(1, 4, 5, 7, 9, 13)
!numbers == 5
# output: TRUE  TRUE FALSE  TRUE  TRUE  TRUE
```

### & |
`&` means **And**, `|` means **Or**:
```
numbers <- c(1, 4, 5, 7, 9, 13)

any(numbers > 7) & any(numbers <= 10)  # output: TRUE
any(numbers > 7) & any(numbers <= 10)  # output: TRUE
```
