- Can make a sequence with your ideal steps by `seq()` function. Begin number in sequence always included but end number may or may not included.
```
# seq stands for: sequence
numbers <- seq(1, 10, by = 2)

numbers

# output:
	1 3 5 7 9
```
You can also allowed to use floating numbers as steps.

Also can use in another way with `length` option that keep numbers in the constant distance:
```
numbers <- seq(1, 10, length = 6)

numbers

output:
	1.0  2.8  4.6  6.4  8.2 10.0
	# All numbers above have 1.8 distance away from each         other.
```
Explain: option `length` says that must choose 4 numbers that have same distance. Doesn't matter numbers will be integer or floating numbers; Always first and last numbers in the sequence will include.
