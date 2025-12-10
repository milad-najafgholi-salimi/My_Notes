# Booleans / Logical Values
- You can evaluate any expression in R, and get one of two answers, TRUE or FALSE.
---
---
# Operations
---
#### Arithmetic Operators

| Operator | Name                              | Example |
| -------- | --------------------------------- | ------- |
| +        | Addition                          | x + y   |
| -        | Subtratcion                       | x - y   |
| *        | Multiplication                    | x * y   |
| /        | Division                          | x / y   |
| ^        | Exponent                          | x ^ y   |
| %%       | Modulus (Remainder from division) | x %% y  |
| %/%      | Integer Division                  | x %/% y |
- Note: <<- is a global assigner.
It is also possible to turn the direction of the assignment operator.
x <- 3 is equal to 3 -> x .

---
#### Comparison Operators
- Comparison operators are used to compare two values:

| Operator | Name                     | Example |
| -------- | ------------------------ | ------- |
| ==       | Equal                    | x == y  |
| !=       | Not Equal                | x != y  |
| >        | Greater Than             | x > y   |
| <        | Less Than                | x < y   |
| >=       | Greater Than or Equal to | x >= y  |
| <=       | Less Than or Equal to    | x <= y  |

---
#### Logical Operators 
- Logical operators are used to combine conditional statements:

| Operator | Desctiption                                                                    |
| -------- | ------------------------------------------------------------------------------ |
| &        | Element-wise Logical AND operator. Returns TRUE if both elements are TRUE      |
| &&       | Logical AND operator - Returns TRUE if both statements are TRUE                |
| \|       | Elementwise-Logical OR operator. Returns TRUE if one of the statements is TRUE |
| \|\|     | Logical OR operator. Returns TRUE if one of the statements is TRUE             |
| !        | Logical NOT - Returns FALSE if statement is TRUE                               |

---
---
# AND OR Operator
- The & symbol (and) is a logical operator, and is used to combine conditional statements - Example:
```
a <- 200
b <- 33
c <- 500

if (a > b & c > a) {
	print("Both conditions are true")
}
```
---
#### OR
- The | symbol (or) is a logical operator, and is used to combine conditional statements - Example:
```
a <- 200
b <- 33
c <- 500

if (a > b | a > c) {
	print("At least one of the conditions is true")
}
```

# Page
|
|
|

Next ---> [[Note_6]]

Previous ---> [[Note_4]]
