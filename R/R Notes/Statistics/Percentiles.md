- Percentiles are used in statistics to give you a number that describes the value that a given percent of the values are lower than.
```
# c() specifies which percentile you want  
quantile(mtcars$wt, c(0.75))
```
If you run the `quantile()` function without specifying the `c()` parameter, you will get the percentiles of 0, 25, 50, 75 and 100:
```
quantile(mtcars$wt)
```
---
#### Quartile
- Quartiles are data divided into four parts, when sorted in an ascending order:
1. 1. The value of the first quartile cuts off the first 25% of the data
2. The value of the second quartile cuts off the first 50% of the data
3. The value of the third quartile cuts off the first 75% of the data
4. The value of the fourth quartile cuts off the 100% of the data

Use the `quantile()` function to get the quartiles.
