- Variables that are created outside of a function are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.
---
#### The Global Assignment Operator
- Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
- To create a global variable inside a function, you can use the global assignment operator <<-
Example:
```
my_function <- function() {
txt <<- "fantastic"
	paste("R is", txt)
}

my_function()
print(txt)

# output:
	"R is fantastic"
	"fantastic"
```
- Also, use the global assignment operator if you want to change a global variable inside a function:
    Example - To change the value of a global variable inside a function, refer to the variable by using the 
    global assignment operator <<-:
```
txt <- "awesome"
my_function <- function() {
	txt <<- "fantastic"
	paste("R is", txt)
}

my_function()
paste("R is", txt)

# output:
	"R is fantastic"
	"R is fantastic"
```
