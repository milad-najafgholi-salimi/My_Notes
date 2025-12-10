#### If Statement
- An "if statement" is written with the if keyword, and it is used to specify a block of code to be executed if a condition is TRUE - Example:
```
a <- 33
b <- 200 

if (b > a) {
	print("b is greater than a")
}
```
- R uses curly brackets { } to define the scope in the code.
---
#### Else If 
- The else if keyword is R's way of saying "if the previous conditions were not true, then try this condition" - Example:
```
a <- 33
b <- 33

if (b > a) {
	print("b is greater than a")
} else if (a == b) {
	print("a and b are equal")
}
```
- You can use as many else if statements as you want in R.
---
#### Else
- The else keyword catches anything which isn't caught by the preceding conditions - Example:
```
a <- 200
b <- 33

if (b > a) {
	print("b is greater than a")
} else if (a == b) {
	print("a and b are equal")
} else {
	print("a is greater than b")
}
```
You can also use else without else if - Example:
```
a <- 200
b <- 33

if (b > a) {
	print("b is greater than a")
} else {
	print(" b is not greather than a")
}
```
You can also have if statements inside if statements, this is called nested if statements.
