The **`readxl`** package in R is used to **read Excel files (`.xls` and `.xlsx`) directly into R**—no Excel or Java required.

---
## What `readxl` Is Good For

- Reads **`.xls` and `.xlsx`**
    
- Works cross-platform (Windows / macOS / Linux)
    
- No need to convert Excel files to CSV
    
- Part of the **tidyverse ecosystem** (but works standalone)
    

---

## Installation & Loading
```
install.packages("readxl")   # once
library(readxl)
```
---

## Main Functions

|Function|Purpose|
|---|---|
|`read_excel()`|Read an Excel file|
|`excel_sheets()`|List sheet names|

---

## Basic Usage

### Read the first sheet
```
data <- read_excel("data.xlsx")
```
---

### Read a specific sheet
```
data <- read_excel("data.xlsx", sheet = "Sheet1")
```
or by index:
```
data <- read_excel("data.xlsx", sheet = 2)
```

---

## Inspect Sheets
```
excel_sheets("data.xlsx")
```

---

## Common Arguments
```
read_excel(
  path,
  sheet = 1,
  range = NULL,
  col_names = TRUE,
  col_types = NULL,
  na = c("", "NA"),
  skip = 0
)
```

### Key arguments explained

|Argument|Meaning|
|---|---|
|`path`|File path to Excel file|
|`sheet`|Sheet name or number|
|`range`|Cell range (e.g. `"A1:D20"`)|
|`col_names`|First row as column names|
|`col_types`|Force column types|
|`skip`|Skip top rows|
|`na`|Strings treated as `NA`|

---

## Examples

### Read a cell range
```
data <- read_excel("data.xlsx", range = "A1:C10")
```

---

### Skip rows
```
data <- read_excel("data.xlsx", skip = 2)
```

---

### Specify column types
```
data <- read_excel(
  "data.xlsx",
  col_types = c("text", "numeric", "date")
)
```

Common `col_types`:

- `"text"`
    
- `"numeric"`
    
- `"date"`
    
- `"logical"`
    
- `"skip"`
    

---

### Handle missing values
```
data <- read_excel("data.xlsx", na = c("", "NA", "N/A"))
```

---

## Output Type

`read_excel()` returns a **tibble** (a modern data frame).

To convert to a base data frame:

`df <- as.data.frame(data)`

---

## Common Issues

### Column types guessed incorrectly

Fix by specifying `col_types`.

---

### Dates look wrong

Excel dates depend on the **1900 / 1904 date system**. `readxl` handles this automatically, but mixed date/text columns may need `"text"`.

---

## Compare with Other Packages

|Package|Reads Excel|Writes Excel|
|---|---|---|
|`readxl`|✅|❌|
|`openxlsx`|✅|✅|
|`xlsx`|✅|✅ (Java required)|

---

## Typical Workflow
```
library(readxl)
library(dplyr)

data <- read_excel("survey.xlsx", sheet = "Responses") |>
  filter(!is.na(age)) |>
  mutate(score = as.numeric(score))
```