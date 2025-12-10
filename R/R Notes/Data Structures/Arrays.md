- Compared to matrices, arrays can have more than two dimensions.
	We can use the array() function to create an array, and the dim parameter to specify the dimensions - Example:
```
# An array with one dimension with values ranging from 1 to 24
thisarray <- c(1:24)
thisarray

# An array with more than one dimension
multiarray <- array(thisarray, dim = c(4, 3, 2))
multiarray
```
Example Explained
In the example above we create an array with the values 1 to 24.

How does dim=c(4,3,2) work?
The first and second number in the bracket specifies the amount of rows and columns.
The last number in the bracket specifies how many dimensions we want.

Note: Arrays can only have one data type.

---
#### Access Array Items
- You can access the array elements by referring to the index position. You can use the [] brackets to access the desired elements from an array - Example:
```
thisarray <- c(1:24)
multiarray <- array(thisarray, dim = c(4, 3, 2))

multiarray[2, 3, 2]

# output:
	[1] 22
```
The syntax is as follow: array[row position, column position, matrix level]
You can also access the whole row or column from a matrix in an array, by using the c() function - Example:
```
thisarray <- c(1:24)

# Access all the items from the first row from matrix one
multiarray <- array(thisarray, dim = c(4, 3, 2))
multiarray[c(1),,1]

# Access all the items from the first column from matrix one
multiarray <- array(thisarray, dim = c(4, 3, 2))
multiarray[,c(1),1]
```
A comma (,) before c() means that we want to access the column.
A comma (,) after c() means that we want to access the row.

---
#### Check if an Item Exists
- To find out if a specified item is present in an array, use the %in% operator - Example:
```
thisarray <- c(1:24)
multiarray <- array(thisarray, dim = c(4, 3, 2))

2 %in% multiarray

# output:
	[1] TRUE
```
---
#### Amount of Rows and Columns
- Use the dim() function to find the amount of rows and columns in an array - Example:
```
thisarray <- c(1:24)
multiarray <- array(thisarray, dim = c(4, 3, 2))

dim(multiarray)
```
---
#### Array Length
- Use the length() function to find the dimension of an array - Example:
```
thisarray <- c(1:24)
multiarray <- array(thisarray, dim = c(4, 3, 2))

length(multiarray)
```
---
#### Loop Through an Array
- You can loop through the array items by using a for loop - Example:
```
thisarray <- c(1:24)
multiarray <- array(thisarray, dim = c(4, 3, 2))

for(x in multiarray){
	print(x)
}
