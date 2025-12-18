### Sign
You can return the sign of the number which is positive [`1`] or negative [`-1`]. 
```
a <- 2.143
b <- -5.63
sign(a)
sign(b)

#output: 1  , -1
```

### Round
If use `round()` function as it is, it takes a number(doesn't matter integer or floating number), and bring back an integer number. But if you give it a number as second parameter, it will return the number in that floating points:
```
a <- 2.143
round(a) # output: 2
round(a, 2) # output: 2.14
```
[پارامتر دوم یعنی اینکه تا فلان رقم اعشار گرد کن.]

### exp
`exp()` stands for exponential. e to the power of something:
```
exp(0) # output: 1
```

### log
`log()` function takes two parameters, one for calculating the giving number, and the second parameter is **base**:
[پارامتر دوم یعنی لگاریتم در پایه چند باشه].
```
log(100, 10) # output: 2
```
If you don't use **base** option, by default base will be `e`.

### Sin - cos - tan - cot
Just use `sin()`, `cos()`, `tan()` and `cot()` functions.

### Factorial
Use `factorial()` function:
```
factorial(5) # output: 120
```

### standard deviation
Use `sd()` function:
[standard deviation == انحراف معیار]
```
numbers <- c(1, 4, 5, 7, 9, 13)
sd(numbers) 
# output: 3.367492
```
