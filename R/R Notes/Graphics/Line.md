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
when you use 1-dimensional vector, those parameters consider as y-axis and default x-axis will be `c <- (1, 2, 3, 4, ...)` 
