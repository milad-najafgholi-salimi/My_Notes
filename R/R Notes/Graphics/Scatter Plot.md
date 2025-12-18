- A "scatter plot" is a type of plot used to display the relationship between two numerical variables, and plots one dot for each observation.
It needs two vectors of same length, one for the x-axis (horizontal) and one for the y-axis (vertical):
```
x <- c(5,7,8,7,2,2,9,4,11,12,9,6)  
y <- c(99,86,87,88,111,103,87,94,78,77,85,86)  
  
plot(x, y)
```
The observation in the example above should show the result of 12 cars passing by.

That might not be clear for someone who sees the graph for the first time, so let's add a header and different labels to describe the scatter plot better:
```
x <- c(5,7,8,7,2,2,9,4,11,12,9,6)  
y <- c(99,86,87,88,111,103,87,94,78,77,85,86)  
  
plot(x, y, main="Observation of Cars", xlab="Car age", ylab="Car speed")
```
`xlab == x-axis lable` and `ylab == y-axis lable`.

---
#### Compare Plots
- To compare the plot with another plot, use the `points()` function - Draw two plots on the same figure:
```
# day one, the age and speed of 12 cars:  
x1 <- c(5,7,8,7,2,2,9,4,11,12,9,6)  
y1 <- c(99,86,87,88,111,103,87,94,78,77,85,86)  
  
# day two, the age and speed of 15 cars:  
x2 <- c(2,2,8,1,15,8,12,9,7,3,11,4,7,14,12)  
y2 <- c(100,105,84,105,90,99,90,95,94,100,79,112,91,80,85)  
  
plot(x1, y1, main="Observation of Cars", xlab="Car age", ylab="Car speed", col="red", cex=2)  
points(x2, y2, col="blue", cex=2)
```
You can compare as many as plots you need.
