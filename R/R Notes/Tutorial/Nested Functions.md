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
