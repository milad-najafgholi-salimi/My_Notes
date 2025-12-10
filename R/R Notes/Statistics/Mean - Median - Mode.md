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