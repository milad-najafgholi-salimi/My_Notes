# While Loop
- R has two loop commands:
    * while loops
    * for loops
---
#### While Loops
- With the while loop we can execute a set of statements as long as a condition is TRUE - Example:
```
i <- 1
while (i < 6) {
	print(i)
	i <- i + 1
}
```
- Note: remember to increment i, or else the loop will continue forever.
---
#### Break
- With the break statement, we can stop the loop even if the while condition is TRUE - Example:
```
i <- 1
while (i < 6) {
	print(i)
	i <- i + 1
	if (i == 4) {
		break
	}
}
```
---
#### Next
- With the next statement, we can skip an iteration without terminating the loop - Example:
```
i <- 0
while (i < 6) {
	i <- i + 1
	if (i == 3) {
		next
	}
	print(i)
}
```
---
---
# For Loops
- A for loop is used for iterating over a sequence -Example:
```
for (x in 1:10) {
	print(x)
}
```
This is less like the for keyword in other programming languages, and works more like an iterator method 
as found in other object-oriented programming languages.

---
#### Nested Loops
- It is also possible to place a loop inside another loop. This is called a nested loop.

# Page
|
|
|

Next ---> [[Note_8]]

Previous ---> [[Note_6]]
