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
