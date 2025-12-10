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