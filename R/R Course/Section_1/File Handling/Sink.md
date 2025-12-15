In **R**, the `sink()` function **redirects R output away from the console** to a file (or another connection):
```
sink("data.txt")
mtcars
sink()
```
Explain: 
- first line will create `data.txt` and get ready to take data.
- `sink("file.txt")`  :
    Starts redirecting **printed output**
- `sink()`  :
    Stops redirection and restores normal console output
#### Important details 
#### `sink()` does NOT capture:

- Plots
    
- Messages (`message()`)
    
- Warnings (`warning()`), unless specified
    

To capture messages too:
```
sink("output.txt", type = "message")
```

## Nested sinks

You can stack sinks:
```
sink("a.txt")
sink("b.txt") 
summary(iris)

sink()
sink()
```
Each `sink()` closes the **most recent** redirection.

## Check sink status
To check sink status, use the following code:
```
sink.number()
```

### Sink append
append option if equals to T/TRUE , will append to file. Otherwise it will overwrite on the file. By default append option is FALSE:
```
sink("data.txt", append=T)
datasets::airquality
sink()
```
- Point: `datasets::` will show you all built-in R datasets and you can choose.
