Find the largest and smallest value of the variable `hp` (horsepower):
```
max(mtcars$hp)
min(mtcars$hp)
```
we can use the `which.max()` and `which.min()` functions to find the index position of the max and min value in the table:
```
which.max(mtcars$hp)
which.min(mtcars$hp)
```
Or even better, combine `which.max()` and `which.min()` with the `rownames()` function to get the name of the car with the largest and smallest horsepower:
```
rownames(mtcars)[which.max(mtcars$hp)]
rownames(mtcars)[which.min(mtcars$hp)]
```
---
#### Outliers
Max and min can also be used to detect **outliers**. An outlier is a data point that differs from rest of the observations.

Example of data points that could have been outliers in the **mtcars** data set:
- If maximum of forward gears of a car was 11
- If minimum of horsepower of a car was 0
- If maximum weight of a car was 50 000 lbs