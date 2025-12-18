# What Vim Is (Mental Model First)

Vim is a **modal editor**.

That means:

- You don’t just “type”
    
- You **switch modes** depending on what you want to do
    

This is the single most important idea in Vim.

---

## The 4 Main Modes You Must Know

### 1. **Normal mode** (default)

- For **navigation and commands**
    
- You are _not typing text_
    
- This is where you spend most of your time
    

Press `Esc` → you are always safe in Normal mode.

---

### 2. **Insert mode**

- For **typing text**
    
- Like a regular editor
    

Enter Insert mode with:

`i`

Exit Insert mode:

`Esc`

---

### 3. **Visual mode**

- For **selecting text**
    
- Similar to click-and-drag selection
    

Enter Visual mode:
```
v        (character-wise)
V        (line-wise)
Ctrl+v   (block-wise)
```
---

### 4. **Command-line mode**

- For **saving, quitting, searching, settings**
    

Enter it from Normal mode:

`:`

---

# Starting Vim

`vim filename.txt`

You start in **Normal mode**.

---

# Movement (Learn This First)

Forget arrow keys. Vim is built around **home-row movement**.
```
h  ←  left
j  ↓  down
k  ↑  up
l  →  right
```

### Word movement
```
w   next word
b   previous word
e   end of word
```
### Line movement
```
0   start of line
^   first non-space
$   end of line
```

### Screen movement
```
gg   top of file
G    bottom of file
```

---

# Insert Mode (Typing Text)

From Normal mode:
```
i   insert before cursor
a   append after cursor
o   open new line below
O   open new line above
```

Exit:

`Esc`

---

# Saving & Quitting (Essential Survival)

From Normal mode:
```
:w        save
:q        quit
:wq       save and quit
:q!       quit without saving
```
---

# Editing Text (The Power of Vim)

This is where Vim becomes special.

### Delete
```
x    delete character
dd   delete line
dw   delete word
```

### Change (delete + insert)
```
cw   change word
cc   change line
```

### Copy & Paste
```
yy   yank (copy) line
p    paste after cursor
P    paste before cursor
```

---

# Undo / Redo
```
u        undo
Ctrl+r   redo
```
---

# The Vim Grammar (VERY IMPORTANT)

Vim commands follow a **verb + object** structure.

Examples:

- `d` = delete
    
- `w` = word
    
- `d + w` → `dw` → delete word
    

More examples:
```
d$    delete to end of line
c$    change to end of line
yG    yank to end of file
```
This is why Vim scales so well.

---

# Searching

From Normal mode:

`/pattern`

Navigate results:
```
n   next
N   previous
```

---

# Visual Mode (Selecting)
```
v    select characters
V    select lines
```

Then apply commands:
```
d    delete selection
y    yank selection
```

---

# Help System (Underrated Superpower)

Vim has one of the best help systems ever.
```
:help
:help dd
:help motion
```

Exit help like any file:

`:q`

---

# A Minimal Practice Routine (Do This)

1. Open a file:
    

`vim test.txt`

2. Practice:
    

- Move with `hjkl`
    
- Insert with `i`, exit with `Esc`
    
- Delete with `dd`, `dw`
    
- Save with `:w`
    
- Quit with `:q`
    

Do **not** rush ahead yet.

---

# Common Beginner Mistakes

- Trying to type while in Normal mode
    
- Forgetting `Esc`
    
- Using arrow keys
    
- Memorizing commands without understanding _verbs + motions_
    

---

# What You Know Now

You can:

- Navigate efficiently
    
- Insert and edit text
    
- Save and quit safely
    
- Understand Vim’s core philosophy
    

That puts you ahead of most people who “use” Vim.