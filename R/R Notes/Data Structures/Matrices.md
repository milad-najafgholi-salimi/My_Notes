- A matrix is a two dimensional data set with columns and rows.
	A column is a vertical representation of data, while a row is a horizontal representation of data.
	A matrix can be created with the matrix() function. Specify the nrow and ncol parameters to get the amount of rows and columns - Example:
```
# Create a matrix
thismatrix <- matrix(c(1,2,3,4,5,6), nrow = 3, ncol = 2)

# Print the matrix
thismatrix
```
Note: Remember the c() function is used to concatenate items together.

You can also create a matrix with strings - Example:
```
thismatrix <- matrix(c("apple", "banana", "cherry", "orange"), nrow = 2, ncol = 2)
thismatrix
```
---
#### Access Matrix Items
- You can access the items by using [ ] brackets. The first number "1" in the bracket specifies the row-position, 
while the second number "2" specifies the column-position - Example:
```
thismatrix <- matrix(c("apple", "banana", "cherry", "orange"), nrow = 2, ncol = 2)
thismatrix[1, 2]

# output:
[1] "cherry"
```
The whole row can be accessed if you specify a comma after the number in the bracket - Example:
```
thismatrix <- matrix(c("apple", "banana", "cherry", "orange"), nrow = 2, ncol = 2)
thismatrix[2,]
```
The whole column can be accessed if you specify a comma before the number in the bracket - Example:
```
thismatrix <- matrix(c("apple", "banana", "cherry", "orange"), nrow = 2, ncol = 2)
thismatrix[,2]
```
---
#### Access More Than One Row
- More than one row can be accessed if you use the c() function - Example:
```
thismatrix <- matrix(c("apple", "banana", "cherry", "orange","grape", "pineapple", "pear", "melon", "fig"), nrow = 3, ncol = 3)
thismatrix[c(1,2),]
```
---
#### Access More Than One Column
- More than one column can be accessed if you use the c() function - Example:
```
thismatrix <- matrix(c("apple", "banana", "cherry", "orange","grape", "pineapple", "pear", "melon", "fig"), nrow = 3, ncol = 3)
thismatrix[, c(1,2)]
```
---
#### Add Rows and Columns
- Use the cbind() function to add additional columns in a Matrix - Example:
```
thismatrix <- matrix(c("apple", "banana", "cherry", "orange","grape", "pineapple", "pear", "melon", "fig"), nrow = 3, ncol = 3)
newmatrix <- cbind(thismatrix, c("strawberry", "blueberry", "raspberry"))

# Print the new matrix
newmatrix
```
Note: The cells in the new column must be of the same length as the existing matrix.

- Use the rbind() function to add additional rows in a Matrix - Example:
```
thismatrix <- matrix(c("apple", "banana", "cherry", "orange","grape", "pineapple", "pear", "melon", "fig"), nrow = 3, ncol = 3)
newmatrix <- rbind(thismatrix, c("strawberry", "blueberry", "raspberry"))

# Print the new matrix
newmatrix
```
Note: The cells in the new row must be of the same length as the existing matrix.

---
#### Remove Rows and Columns
- Use the c() function to remove rows and columns in a Matrix- Example:
```
thismatrix <- matrix(c("apple", "banana", "cherry", "orange", "mango", "pineapple"), nrow = 3, ncol = 2)

#Remove the first row and the first column
thismatrix <- thismatrix[-c(1), -c(1)]

print(thismatrix)
```
#### Check if an Item Exists
- To find out if a specified item is present in a matrix, use the %in% operator - Example:
```
thismatrix <- matrix(c("apple", "banana", "cherry", "orange"), nrow = 2, ncol = 2)

"apple" %in% thismatrix

# output:
	TRUE
```
---
#### Number of Rows and Columns
- Use the dim() function to find the number of rows and columns in a Matrix - Example:
```
thismatrix <- matrix(c("apple", "banana", "cherry", "orange"), nrow = 2, ncol = 2)
dim(thismatrix)

# output:
	[1] 2 2
```
---
#### Matrix Length
- Use the length() function to find the dimension of a Matrix - Example:
```
thismatrix <- matrix(c("apple", "banana", "cherry", "orange"), nrow = 2, ncol = 2)
length(thismatrix)

# output:
	[1] 4
```
Total cells in the matrix is the number of rows multiplied by number of columns.
In the example above: Dimension = 2*2 = 4.

---
#### Loop Through a Matrix
- You can loop through a Matrix using a for loop. The loop will start at the first row, moving right - Example:
```
thismatrix <- matrix(c("apple", "banana", "cherry", "orange"), nrow = 2, ncol = 2)

for (rows in 1:nrow(thismatrix)) {
	for (columns in 1:ncol(thismatrix)) {
	  print(thismatrix[rows, columns])
	}
}
```
---
#### Combine Two Matrices
- Again, you can use the rbind() or cbind() function to combine two or more matrices together - Example:
```
# Combine matrices
Matrix1 <- matrix(c("apple", "banana", "cherry", "grape"), nrow = 2, ncol = 2)
Matrix2 <- matrix(c("orange", "mango", "pineapple", "watermelon"), nrow = 2, ncol = 2)

# Adding it as a rows
Matrix_Combined <- rbind(Matrix1, Matrix2)
Matrix_Combined

# Adding it as a columns
Matrix_Combined <- cbind(Matrix1, Matrix2)
Matrix_Combined
