# Plot
- There are other things that need to learn to use, but for now, *focus on understanding the subject*.
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

---
---
# Line
#### Line Graphs
- A line graph has a line that connects all the points in a diagram.
[diagram --> نمودار]
To create a line, use the `plot()` function and add the `type` parameter with a value of `"l"`:
```
plot(1:10, type="l")
```
---
#### Line Color
- The line color is black by default. To change the color, use the `col` parameter:
```
plot(1:10, type="l", col="blue")
```
---
#### Line Width
- To change the width of the line, use the `lwd` parameter (`1` is default, while `0.5` means 50% smaller, and `2` means 100% larger):
```
plot(1:10, type="l", lwd=2)
```
---
#### Line Styles
- The line is solid by default. Use the `lty` parameter with a value from **0 to 6** to specify the line format.
```
plot(1:10, type="l", lwd=5, lty=3)
```
- Available parameter values for `lty`:
	- `0` removes the line
	- `1` displays a solid line
	- `2` displays a dashed line
	- `3` displays a dotted line
	- `4` displays a "dot dashed" line
	- `5` displays a "long dashed" line
	- `6` displays a "two dashed" line
---
#### Multiple Lines
- To display more than one line in a graph, use the `plot()` function together with the `lines()` function:
```
line_1 <- c(1, 2, 3, 4, 5, 10)
line_2 <- c(2, 5, 7, 8, 9, 10)

plot(line_1, type = "l", col = "blue")
lines(line_2, type="l", col = "red")
```
when you use 1-dimentional vector, those parameters consider as y-axis and default x-axis will be `c <- (1, 2, 3, 4, ...)` 

---
---
# Scatter Plot
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

---
---
# Pie Charts
- A pie chart is a circular graphical view of data.
- Use the `pie()` function to draw pie charts:
```
# Create a vector of pies  
x <- c(10,20,30,40)  
  
# Display the pie chart  
pie(x)
```
 Example Explained:
As you can see the pie chart draws one pie for each value in the vector (in this case 10, 20, 30, 40).

By default, the plotting of the first pie starts from the x-axis and move **counterclockwise**.

**Note:** The size of each pie is determined by comparing the value with all the other values, by using this formula:
The value divided by the sum of all values: `x/sum(x)`

---
#### Start Angle
- You can change the start angle of the pie chart with the `init.angle` parameter.
The value of `init.angle` is defined with angle in degrees, where default angle is 0.
Example - Start the first pie at 90 degrees:
```
# Create a vector of pies  
x <- c(10,20,30,40)  
  
# Display the pie chart and start the first pie at 90 degrees  
pie(x, init.angle = 90)
```
---
#### Labels and Header
- Use the `label` parameter to add a label to the pie chart, and use the `main` parameter to add a header:
```
# Create a vector of pies  
x <- c(10,20,30,40)  
  
# Create a vector of labels  
mylabel <- c("Apples", "Bananas", "Cherries", "Dates")  
  
# Display the pie chart with labels  
pie(x, label = mylabel, main = "Fruits")
```
---
#### Colors
- You can add a color to each pie with the `col` parameter:
```
x <- c(10,20,30,40) 
mylabel <- c("Apples", "Bananas", "Cherries", "Dates") 
 
# Create a vector of colors  
colors <- c("blue", "yellow", "green", "black")  
  
# Display the pie chart with colors  
pie(x, label = mylabel, main = "Fruits", col = colors)
```
---
#### Legend
- To add a list of explanation for each pie, use the `legend()` function:
```
x <- c(10,20,30,40) 

# Create a vector of labels  
mylabel <- c("Apples", "Bananas", "Cherries", "Dates")  
  
# Create a vector of colors  
colors <- c("blue", "yellow", "green", "black")  
  
# Display the pie chart with colors  
pie(x, label = mylabel, main = "Pie Chart", col = colors)  
  
# Display the explanation box  
legend("bottomright", mylabel, fill = colors)
```
The legend can be positioned as either:

`bottomright`, `bottom`, `bottomleft`, `left`, `topleft`, `top`, `topright`, `right`, `center`

---
---
# Bars
- A bar chart uses rectangular bars to visualize data. Bar charts can be displayed horizontally or vertically. The height or length of the bars are proportional to the values they represent.
Use the `barplot()` function to draw a vertical bar chart:
[vertical --> عمودی]
```
# x-axis values  
x <- c("A", "B", "C", "D")  
  
# y-axis values  
y <- c(2, 4, 6, 8)  
  
barplot(y, names.arg = x)
```
---
#### Bar Color
- Use the `col` parameter to change the color of the bars:
```
x <- c("A", "B", "C", "D")  
y <- c(2, 4, 6, 8)  
  
barplot(y, names.arg = x, col = "red")
```
---
#### Density / Bar Texture
- To change the bar texture, use the `density` parameter:
```
x <- c("A", "B", "C", "D")  
y <- c(2, 4, 6, 8)  
  
barplot(y, names.arg = x, density = 10)
```
---
#### Bar Width
- Use the `width` parameter to change the width of the bars:
```
x <- c("A", "B", "C", "D")  
y <- c(2, 4, 6, 8)  
  
barplot(y, names.arg = x, width = c(1,2,3,4))
```
---
#### Horizontal Bars
- If you want the bars to be displayed horizontally instead of vertically, use `horiz=TRUE`:
```
x <- c("A", "B", "C", "D")  
y <- c(2, 4, 6, 8)  
  
barplot(y, names.arg = x, horiz = TRUE)
```
---
---
# Page
|
|
|

Next ---> [[Note_11]]

Previous ---> [[Note_9]]
