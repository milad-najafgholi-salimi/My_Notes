# Function
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
```
---
---
# Nested Functions
- There are two ways to create a nested function:
    * Call a function within another function.
    * Write a function within a function.
* Call a function within another function - Example:
```
Nested_function <- function(x, y) {
a <- x + y
return(a)
}

Nested_function(Nested_function(2, 2),Nested_function(3,3)) 

# output: 10
```
- Write a function within a function - Example:
```
Outer_func <- function(x) {
	Inner_func <- function(y) {
		a <- x + y
		return(a)
	}
	return (Inner_func)
}
output <- Outer_func(3) # To call the Outer_func
output(5)
```
Example Explain:
    You cannot directly call the function because the Inner_func has been defined (nested) inside the Outer_func.
    We need to call Outer_func first in order to call Inner_func as a second step.
    We need to create a new variable called output and give it a value, which is 3 here.
    We then print the output with the desired value of "y", which in this case is 5.
    The output is therefore 8 (3 + 5).

---
---
# Recursion
- R also accepts function recursion, which means a defined function can call itself.

- Recursion is a common mathematical and programming concept. It means that a function calls itself. 
	This has the benefit of meaning that you can loop through data to reach a result.

- The developer should be very careful with recursion as it can be quite easy to slip into writing a 
	function which never terminates, or one that uses excess amounts of memory or processor power. 
	However, when written correctly, recursion can be a very efficient and mathematically-elegant approach to programming.
Example:
```
tri_recursion <- function(k) {
	if (k > 0) {
		result <- k + tri_recursion(k - 1)
		print(result)
	} else {
	result = 0
	return(result)
	}
}
tri_recursion(6)

# Output: 
	1
	3
	6
	10
	15
	21
```
Explain:
```
this part of code [result <- k + tri_recursion(k - 1)] works like this:
        6 + tri_recursion(5)
            5 + tri_recursion(4)
                4 + tri_recursion(3)
                    3 + tri_recursion(2)
                        2 + tri_recursion(1)
                            1 + tri_recursion(0)

After "going down" [up to down], then returns from down to up. So now, we have all we need. So the program starts and prints the results from down to up [in other words from inner to outer]
```
---
---
# Global Variable
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

|
|
|

Next ---> [[Note_9]]

Previous ---> [[Note_7]]
