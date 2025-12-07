# Data Structures
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
```
---
---
# Vectors
- A vector is simply a list of items that are of the same type. To combine the list of items to a vector, use the c() function and separate the items by a comma. - Example:
```
# vector of strings 
fruits <- c("banana", "apple", "orange")

# print fruits
fruits
```
To create a vector with numerical values in a sequence, use the : operator - Example:
```
# vector with numerical values in a sequence
numbers <- 1:10
numbers
```
You can also create numerical values with decimals in a sequence, but note that if the last element does not 
belong to the sequence, it is not used - Example:
```
# vector with numerical decimals in a sequence
numbers1 <- 1.5: 6.5
numbers1

# vector with numerical decimals in a sequence where the #last element is not used
numbers2 <- 1.5:6.3
numbers2

output:
	[1] 1.5 2.5 3.5 4.5 5.5 6.5
	[1] 1.5 2.5 3.5 4.5 5.5
```
In the example below, we create a vector of logical values - Example:
```
# vector of logical values
log_values <- c(TRUE, FALSE, TRUE, FALSE)

log_values
```
---
#### Vector Length
- To find out how many items a vector has, use the length() function - Example:
```
fruits <- c("banana", "apple", "orange")
length(fruits)
```
---
#### Sort a Vector
- To sort items in a vector alphabetically or numerically, use the sort() function - Example:
```
fruits <- c("banana", "apple", "orange", "mango", "lemon")
numbers <- c(13, 3, 5, 7, 20, 2)

sort(fruits)   # sort a string
sort(numbers)  # sort numbers
```
---
#### Access Vectors
You can access the vector items by referring to its index number inside brackets []. The first item has index 1, the second item has index 2, and so on - Example:
```
fruits <- ("banana", "apple", "orange")

# Access the first item (banana)
fruits[1]
```
You can also access multiple elements by referring to different index positions with the c() function - Example:
```
fruits <- c("banana", "apple", "orange", "mango", "lemon")

# Access the first and third item (banana and orange)
fruits[c(1, 3)]

# output:
	[1] "banana" "orange"
```
You can also use negative index numbers to access all items except the ones specified - Example:
```
fruits <- c("banana", "apple", "orange", "mango", "lemon")

# Access all items except for the first item
fruits[c(-1)]

# output:
	"apple" "orange" "mango" "lemon"
```
---
#### Change an Item
- To change the value of a specific item, refer to the index number - Example:
```
fruits <- c("banana", "apple", "orange", "mango", "lemon")

# Change "banana" to "pear"
fruits[1] <- "pear"

# Print fruits
fruits
```
---
#### Repeat Vectors
- To repeat vectors, use the rep() function - Example:
```
repeat_each <- rep(c(1, 2, 3), each = 3)
repeat_each

# output:
	[1] 1 1 1 2 2 2 3 3 3
```
Repeat the sequence of the vector -Example:
```
repeat_times <- rep(c(1, 2, 3), times = 3)
repeat_times

# output:
	[1] 1 2 3 1 2 3 1 2 3
```
Repeat each value independently - Example:
```
repeat_indepent <- rep(c(1, 2, 3), times = c(5, 2, 1))
repeat_indepent

# output:
	[1] 1 1 1 1 1 2 2 3
```
---
#### Generating Sequenced Vectors
One of the examples on top, showed you how to create a vector with numerical values in a sequence with the : operator - Example:
```
numbers <- 1:10
numbers
```
To make bigger or smaller steps in a sequence, use the seq() function - Example:
```
numbers <- seq(from = 0, to = 100, by = 20)
numbers
```
Note: The seq() function has three parameters: from is where the sequence starts, to is where the sequence stops, 
and by is the interval of the sequence.

---
---
# Lists
- A list in R can contain many different data types inside it. A list is a collection of data which is ordered and changeable.
To create a list, use the list() function - Example:
```
# List of strings
this_list <- list("apple", "banana", "cherry")

# print the list
this_list
```
---
#### Access Lists
- You can access the list items by referring to its index number, inside brackets. The first item has index 1, 
the second item has index 2, and so on:
    Example:
```
thislist <- list("apple", "banana", "cherry")
thislist[1]
```
---
#### Change Item Value
- To change the value of a specific item, refer to the index number - Example:
```
thislist <- list("apple", "banana", "cherry")
thislist[1] <- "blackcurrant"

# Print the updated list
thislist
```
---
#### List Length
- To find out how many items a list has, use the length() function - Example:
```
thislist <- list("apple", "banana", "cherry")
length(thislist)
```
---
#### Check if Item Exists
- To find out if a specified item is present in a list, use the %in% operator - Example:
```
thislist <- list("apple", "banana", "cherry")
"apple" %in% thislist

# output:
	[1] TRUE
```
---
#### Add List Items
- To add an item to the end of the list, use the append() function - Example:
```
thislist <- list("apple", "banana", "cherry")
append(thislist, "orange")
```
To add an item to the right of a specified index, add "after=index number" in the append() function - Example:
```
thislist <- list("apple", "banana", "cherry")
append(thislist, "orange", after = 2)
```
---
#### Remove List Items
- You can also remove list items. The following example creates a new, updated list without an "apple" item - Example:
```
thislist <- list("apple", "banana", "cherry")
newlist <- thislist[-1]

# Print the new list
newlist
```
---
#### Range of Indexes
- You can specify a range of indexes by specifying where to start and where to end the range, by using the : operator - Example:
```
thislist <- list("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
(thislist)[2:5]
```
Note: The search will start at index 2 (included) and end at index 5 (included).
Remember that the first item has index 1.

---
#### Loop Through a List
- You can loop through the list items by using a for loop - Example:
```
thislist <- list("apple", "banana", "cherry")

for (x in thislist) {
	print(x)
}
```
---
#### Join Two Lists
- There are several ways to join, or concatenate, two or more lists in R.
	The most common way is to use the c() function, which combines two elements together - Example:
```
list1 <- list("a", "b", "c")
list2 <- list(1, 2, 3)
list3 <- c(list1,list2)

list3
```
---
---
# Matrices
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
```
---
---
# Arrays
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
```
---
---
# Data Frames
- Data Frames are data displayed in a format as a table.
	Data Frames can have different types of data inside it. While the first column can be character, the second and 
	third can be numeric or logical. However, each column should have the same type of data.
	Use the data.frame() function to create a data frame - Example:
```
Data_Frame <- data.frame (
	  Training = c("Strength", "Stamina", "Other"),
	  Pulse = c(100, 150, 120),
	  Duration = c(60, 30, 45)
)

# Print the data frame
Data_Frame
```
---
#### Summarize the Data
- Use the summary() function to summarize the data from a Data Frame - Example:
```
Data_Frame <- data.frame (
  Training = c("Strength", "Stamina", "Other"),
  Pulse = c(100, 150, 120),
  Duration = c(60, 30, 45)
)

Data_Frame

summary(Data_Frame)
```
---
#### Access Items
- We can use single brackets [ ], double brackets [[ ]] or $ to access columns from a data frame - Example:
```
Data_Frame <- data.frame (
  Training = c("Strength", "Stamina", "Other"),
  Pulse = c(100, 150, 120),
  Duration = c(60, 30, 45)
)

Data_Frame[1]

Data_Frame[["Training"]]

Data_Frame$Training
```
---
#### Add Rows
- Use the rbind() function to add new rows in a Data Frame - Example:
```
Data_Frame <- data.frame (
  Training = c("Strength", "Stamina", "Other"),
  Pulse = c(100, 150, 120),
  Duration = c(60, 30, 45)
)

# Add a new row
New_row_DF <- rbind(Data_Frame, c("Strength", 110, 110))

# Print the new row
New_row_DF
```
---
#### Add Columns
- Use the cbind() function to add new columns in a Data Frame - Example:
```
Data_Frame <- data.frame (
  Training = c("Strength", "Stamina", "Other"),
  Pulse = c(100, 150, 120),
  Duration = c(60, 30, 45)
)

# Add a new column
New_col_DF <- cbind(Data_Frame, Steps = c(1000, 6000, 2000))

# Print the new column
New_col_DF
```
---
#### Remove Rows and Columns
- Use the c() function to remove rows and columns in a Data Frame - Example:
```
Data_Frame <- data.frame (
  Training = c("Strength", "Stamina", "Other"),
  Pulse = c(100, 150, 120),
  Duration = c(60, 30, 45)
)

# Remove the first row and column
Data_Frame_New <- Data_Frame[-c(1), -c(1)]

# Print the new data frame
Data_Frame_New
```
---
#### Amount of Rows and Columns
- Use the dim() function to find the amount of rows and columns in a Data Frame - Example:
```
Data_Frame <- data.frame (
  Training = c("Strength", "Stamina", "Other"),
  Pulse = c(100, 150, 120),
  Duration = c(60, 30, 45)
)

dim(Data_Frame)

# output:
	[1] 3 3
```
You can also use the ncol() function to find the number of columns and nrow() to find the number of rows - Example:
```
Data_Frame <- data.frame (
  Training = c("Strength", "Stamina", "Other"),
  Pulse = c(100, 150, 120),
  Duration = c(60, 30, 45)
)

ncol(Data_Frame)
nrow(Data_Frame)

# output:
	[1] 3
	[1] 3
```
---
#### Data Frame Length
Use the length() function to find the number of columns in a Data Frame (similar to ncol()) - Example:
```
Data_Frame <- data.frame (
  Training = c("Strength", "Stamina", "Other"),
  Pulse = c(100, 150, 120),
  Duration = c(60, 30, 45)
)

length(Data_Frame)

# output:
	[1] 3
```
---
#### Combining Data Frames
- Use the rbind() function to combine two or more data frames in R vertically - Example:
```
Data_Frame1 <- data.frame (
  Training = c("Strength", "Stamina", "Other"),
  Pulse = c(100, 150, 120),
  Duration = c(60, 30, 45)
)

Data_Frame2 <- data.frame (
  Training = c("Stamina", "Stamina", "Strength"),
  Pulse = c(140, 150, 160),
  Duration = c(30, 30, 20)
)

New_Data_Frame <- rbind(Data_Frame1, Data_Frame2)
New_Data_Frame
```
And use the cbind() function to combine two or more data frames in R horizontally - Example:
```
Data_Frame3 <- data.frame (
  Training = c("Strength", "Stamina", "Other"),
  Pulse = c(100, 150, 120),
  Duration = c(60, 30, 45)
)

Data_Frame4 <- data.frame (
  Steps = c(3000, 6000, 2000),
  Calories = c(300, 400, 300)
)

New_Data_Frame1 <- cbind(Data_Frame3, Data_Frame4)
New_Data_Frame1
```
---
---
# Factors
- Factors are used to categorize data. Examples of factors are:
    * Demography: Male/Female
    * Music: Rock, Pop, Classic, Jazz
    * Training: Strength, Stamina
- To create a factor, use the factor() function and add a vector as argument - Example:
```
music_genre <- factor(c("Jazz", "Rock", "Classic", "Classic", "Pop", "Jazz", "Rock", "Jazz"))
music_genre
```
You can see from the example above that that the factor has four levels (categories): Classic, Jazz, Pop and Rock.
To only print the levels, use the levels() function - Example:
```
music_genre <- factor(c("Jazz", "Rock", "Classic", "Classic", "Pop", "Jazz", "Rock", "Jazz"))
levels(music_genre)
```
You can also set the levels, by adding the levels argument inside the factor() function - Example:
```
music_genre <- factor(c("Jazz", "Rock", "Classic", "Classic", "Pop", "Jazz", "Rock", "Jazz"), levels = c("Classic", "Jazz", "Pop", "Rock", "Other"))

levels(music_genre)
```
---
#### Factor Length
- Use the length() function to find out how many items there are in the factor - Example:
```
music_genre <- factor(c("Jazz", "Rock", "Classic", "Classic", "Pop", "Jazz", "Rock", "Jazz"))
length(music_genre)

# output:
	[1] 8
```
---
#### Access Factors
- To access the items in a factor, refer to the index number, using [] brackets - Example:
```
music_genre <- factor(c("Jazz", "Rock", "Classic", "Classic", "Pop", "Jazz", "Rock", "Jazz"))

music_genre[3]
```
---
#### Change Item Value
- To change the value of a specific item, refer to the index number - Example:
```
music_genre <- factor(c("Jazz", "Rock", "Classic", "Classic", "Pop", "Jazz", "Rock", "Jazz"))

music_genre[3] <- "Pop"
music_genre[3]
```
Note that you cannot change the value of a specific item if it is not already specified in the factor. The following example will produce an error - Example:
```
music_genre <- factor(c("Jazz", "Rock", "Classic", "Classic", "Pop", "Jazz", "Rock", "Jazz"))
music_genre[3] <- "Opera"
music_genre[3]

# output:
	Error
```
However, if you have already specified it inside the levels argument, it will work - Example:
```
music_genre <- factor(c("Jazz", "Rock", "Classic", "Classic", "Pop", "Jazz", "Rock", "Jazz"), levels = c("Classic", "Jazz", "Pop", "Rock", "Opera"))

music_genre[3] <- "Opera"
music_genre[3]
```

|
|
|

Next ---> [[Note_10]]

Previous ---> [[Note_8]]
