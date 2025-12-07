# Intro
- R is a programming language.
- R is often used for statistical computing and graphical presentation to analyze and visualize data.
- Unlike many other programming languages, you can output code in R without using a print function. - Example:
```
"Hello World!"
```
- Also for numbers, keep it simple like previous one. - Example:
```
4
2
```
- To do simple calculations - Example:
```
2 + 5
7 * 2
```
- However, R does have a print() function available if you want to use it. - Example:
```
print("Hello, World!")
```
- And there are times you must use the print() function to output code. - Example:
```
for (x in 1:10) {
	print(x)
}
```
- Conclusion: It is up to you whether you want to use the print() function to output code. 
However, when your code is inside an R expression (e.g. inside curly braces {} like in the example above), 
use the print() function to output the result.

---
---
# Variables
- To assign a value to a variable, use the <- sign. To output (or print) the variable value, just type the variable name. - Example:
```
name <- "Milad"
age <- 22

name    # output: "Milad"
age     # output: 22
```
- In other programming language, it is common to use = as an assignment operator. 
In R, we can use both = and <- as assignment operators.
However, <- is preferred in most cases because the = operator can be forbidden in some contexts in R.

---
#### Concatenate Elements
- You can also concatenate, or join, two or more elements, by using the paste() function. - Example:
```
text <- "good"
paste("R is", text)
```
Example:
```
txt_1 <- "R is"
txt_2 <- "good"
paste(txt_1, txt_2)
```
- For numbers, the + character works as a mathematical operator. - Example:
```
num1 <- 3
num2 <- 5

num1 + num2
```
If you try to combine a string (text) and a number, R will give you an error.
Also combine two strings, R will give you an error. - Example:
```
txt <- "good"
txt_1 <- "R is"
paste(txt_1 + txt)

# """ This will give you and error """
```
---
#### Multiple Variables
- R allows you to assign the same value to multiple variables in one line. - Example:
```
var1 <- var2 <- var3 <- "Milad"
var1
var2
var3

# output:
	"Milad"
	"Milad"
	"Milad"
```

|
|
|

**Next** ---> [[Note_2]]
