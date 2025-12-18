- Data structures are used to store and organize values.
- R provides many built-in data structures. Each is used to handle data in different ways:
    * Vectors
    * Lists
    * Matrices
    * Arrays
    * Data Frames
---
#### Vectors
- A vector is the most basic data structure in R. It contains a list of items of the same type - Example:
```
# vectors of strings
fruits <- c("banana", "apple", "orange")

# print fruits
fruits
```
---
#### Lists
- A list can hold different types of data in one structure. You can combine numbers, strings, vectors, and even other lists - Example:
```
# Lists of strings
this_list <- list("apple", "banana", 50, 100)

# print the list
this_list
```
---
#### Matrices
- A matrix is a 2D data structure where all elements are of the same type. It is like a table with rows and columns - Example:
```
# create a matrix
this_matrix <- matrix(c(1, 2, 3, 4, 5, 6), nrow=3, ncol=2)

# print the matrix
this_matrix
```
Use nrow and ncol to control the size of the matrix.

---
#### Arrays
An array is like a matrix but can have more than two dimensions. It stores elements of the same type in multiple dimensions. - Example:
```
# An array with one dimension with values ranging from 1 to 24
this_array <- c(1:24)
this_array

# An array with more than one dimension
multi_array <- array(this_array, dim = c(4, 3, 2))
multi_array
```
Arrays are useful for working with 3D or higher-dimensional data.

---
#### Data Frames
- A data frame is like a table in a spreadsheet. It can hold different types of data across multiple columns. - Example:
```
# create a data frame
data_frame <- data.frame (
	Training <- c("Strength", "Stamina", "Other"),
	Pulse <- c(100, 150, 120),
	Duration <- c(60, 30, 45)
)

# print the data frame
data_frame