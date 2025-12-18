You generally **cannot “see” your terminal (system) password**, but you **can change it**. This is a security feature on all modern operating systems.
## Why you can’t see your password

- Your system **never stores your password in plain text**.
    
- It stores a **cryptographic hash**, which cannot be reversed to reveal the original password.
    
- So there is **no command** like `show my password` — if you see one online, it’s fake or malicious.
## How to change your terminal password

### Linux (Ubuntu, Debian, Arch, Fedora, etc.)

#### Change your own password

`passwd`

You’ll be prompted for:

1. Current password
    
2. New password
    
3. Confirm new password
    

> Note: When typing, **nothing will appear** (no dots, no stars). This is normal.