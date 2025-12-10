# Statistics
- Statistics is the science of analyzing, reviewing and conclude data.
- Some basic statistical numbers include:
	- Mean, median and mode
	- Minimum and maximum value
	- Percentiles
	- Variance and Standard Deviation
	- Covariance and Correlation
	- Probability distributions

The R language was developed by two statisticians. It has many built-in functionalities, in addition to libraries for the exact purpose of statistical analysis.

---
---
# Data Set
- A data set is a collection of data, often presented in a table.
[table --> جدول]
In the examples below , we will use the `mtcars` data set, for statistical purposes:
```
# Print the mtcars data set
mtcars
```
---
#### Information About the Data Set
- You can use the question mark (`?`) to get information about the `mtcars` data set:
```
# Use the question mark to get information about the data set  
  
?mtcars
```
Tip: To see the list of pre-loaded data, type the function `data()`:
```
data()
```
---
#### Get Information
- Use the `dim()` function to find the dimensions of the data set, and the `names()` function to view the names of the variables:
```
Data_Cars <- mtcars # create a variable of the mtcars data set for better organization  
  
# Use dim() to find the dimension of the data set  
dim(Data_Cars)  
  
# Use names() to find the names of the variables from the data set  
names(Data_Cars)
```
- Use the `rownames()` function to get the name of each row in the first column, which is the name of each car:
```
rownames(mtcars)
```
--- 
#### Print Variable Values
- If you want to print all values that belong to a variable, access the data frame by using the `$` sign, and the name of the variable (for example `cyl` (cylinders)):
```
mtcars$cyl
```
---
#### Sort Variable Values
- To sort the values, use the `sort()` function:
```
sort(mtcars$cyl)
```
---
#### Analyzing the Data
- Now that we have some information about the data set, we can start to analyze it with some statistical numbers.
For example, we can use the `summary()` function to get a statistical summary of the data:
```
summary(mtcars)
```
---
---
# Max and Min
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
---
---
# Mean Median Mode
- In statistics, there are often three values that interests us:
	- **Mean** - The average value
	- **Median** - The middle value
	- **Mode** - The most common value
---
#### Mode
- To calculate the average value (mean) of a variable from the `mtcars` data set, find the sum of all values, and divide the sum by the number of values.
Luckily for us, the `mean()` function in R can do it for you:
Example - Find the average weight (`wt`) of a car
```
mean(mtcars$wt)
```
---
#### Median
- The median value is the value in the middle, after you have sorted all the values.

**Note:** If there are two numbers in the middle, you must divide the sum of those numbers by two, to find the median.

Luckily, R has a function that does all of that for you: Just use the `median()` function to find the middle value:
Example - Find the mid point value of weight (`wt`):
```
median(mtcars$wt)
```
---
#### Mode
- The mode value is the value that appears the most number of times.
R does not have a function to calculate the mode. However, we can create our own function to find it.

Instead of counting it ourselves, we can use the following code to find the mode:
```
names(sort(-table(mtcars$wt)))[1]
```
---
---
# Percentiles
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

---
---
Page
|
|
|

Previous ---> [[Note_10]]
