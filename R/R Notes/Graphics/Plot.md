- The `plot()` function is used to draw points (markers) in a diagram.
The function takes parameters for specifying points in the diagram.
Parameter 1 specifies points on the **x-axis**.
Parameter 2 specifies points on the **y-axis**.
At its simplest, you can use the `plot()` function to plot two numbers against each other:
- Example - Draw one point in the diagram, at position (1) and position (3):
```
plot(1, 3)
```
To draw more points, use vectors:
```
plot(c(1, 8), c(3, 10))
```
---
#### Multiple Points
- You can plot as many points as you like, just make sure you have the same number of points in both axis:
```
plot(c(1, 2, 3, 4, 5), c(3, 7, 8, 9, 12))
```

Explaining example above: It's really easy. The points on diagram are:
- (1, 3)
- (2, 7)
- (3, 8)
- (4, 9)
- (5, 12)
For better organization, when you have many values, it is better to use variables:
```
x <- c(1, 2, 3, 4, 5)  
y <- c(3, 7, 8, 9, 12)  
  
plot(x, y)
```
---
#### Sequences of Points
- If you want to draw dots in a sequence, on both the **x-axis** and the **y-axis**, use the `:` operator:
```
plot(1:10)
```
Explaining example above: It's just like y = x function. Like:
- (1, 1)
- (2, 2)
- (3, 3)
.
.
.
- (n, n)
---
#### Draw a Line
- The `plot()` function also takes a `type` parameter with the value `l` to draw a line to connect all the points in the diagram:
```
plot(1:10, type="l")
```
---
#### Plot Labels
- The `plot()` function also accept other parameters, such as `main`, `xlab` and `ylab` if you want to customize the graph with a main title and different labels for the x and y-axis:
```
plot(1:10, main="My Graph", xlab="The x-axis", ylab="The y axis")
```
---
#### Graph Appearance
- There are many other parameters you can use to change the appearance of the points.
###### Colors
- Use `col="_color_"` to add a color to the points:
```
plot(1:10, col="red")
```
###### Size
- Use `cex=_number_` to change the size of the points (`1` is default, while `0.5` means 50% smaller, and `2` means 100% larger):
```
plot(1:10, cex=2)
```
###### Point Shape
- Use `pch` with a value from 0 to 25 to change the point shape format:
```
plot(1:10, pch=25, cex=2)
```
The values of the `pch` parameter ranges from 0 to 25, which means that we can choose up to 26 different types of point shapes
