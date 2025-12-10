- A function is a block of code which only runs when it is called.
- You can pass data, known as parameters, into a function.
- A function can return data as a result.
---
#### Creating a Function
- To create a function, use the function() keyword - Example:
```
my_function <- function() {
	print("Hello World!)
 }
```
---
#### Call a Function
- To call a function, use the function name followed by parenthesis, like my_function() - Example:
```
my_function <- function() {
	print("Hello World!)
}

my_function()   # call the function named my_function
```
---
#### Arguments
- Information can be passed into functions as arguments.
	Arguments are specified after the function name, inside the parentheses. 
	You can add as many arguments as you want, just separate them with a comma.

- Point: 
	- Parameters or Arguments?
	    The terms "parameter" and "argument" can be used for the same thing: information that are passed into a function.
	- From a function's perspective:
	- A parameter is the variable listed inside the parentheses in the function definition.
	- An argument is the value that is sent to the function when it is called.
---
#### Return Values
- To let a function return a result, use the return() function - Example:
```
my_function <- function(x) {
	return (5 * x)
}

print(my_function(3))