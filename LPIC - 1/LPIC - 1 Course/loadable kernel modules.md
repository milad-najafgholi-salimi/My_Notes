Linux like any other OS needs drivers to work with hardware. 
In Microsoft Windows, you need to install the drivers separately but in Linux, the system has most of the drivers built-in. 
But to prevent the kernel from loading all of them at the same time and to decrease the Kernel size, Linux uses Kernel Modules. 
Loadable kernel modules (.ko files) are object files that are used to extend the kernel of the Linux Distribution. 
They are used to provide drivers for new hardware like IoT expansion cards that have not been included in the Linux Distribution.
You can inspect the modules using the lsmod or manage them via modprobe commands.
# lsmod
**`lsmod`** is a Linux command used to **display the kernel modules that are currently loaded** into the running kernel.
## What Is a Kernel Module?

A **kernel module** is a piece of code that can be **loaded or unloaded at runtime** without rebooting.

Examples:

- Device drivers (Wi-Fi, USB, GPU)
    
- Filesystem support (ext4, ntfs)
    
- Networking features
    

---
## What `lsmod` Shows

When you run:

`lsmod`

You see a table like this:
```
Module                  Size  Used by
iwlwifi               413696  1
cfg80211              704512  1 iwlwifi
snd_hda_intel          57344  3
```

### Column Explanation

|Column|Meaning|
|---|---|
|**Module**|Name of the kernel module|
|**Size**|Memory used by the module (bytes)|
|**Used by**|Number of modules or processes using it|

If the **Used by** value is `0`, the module is loaded but not actively used.
## Why `lsmod` Is Useful

### 1. **Check Driver Status**

- Confirm if a hardware driver is loaded
    
- Example: Wi-Fi not working → check Wi-Fi module
    

---

### 2. **Troubleshooting**

- Identify conflicting or missing modules
    
- Check dependencies between modules
    

---

### 3. **System Monitoring**

- See what kernel features are active
    
- Useful in performance or security audits
## How `lsmod` Works Internally

`lsmod` reads information from:

`/proc/modules`

So `/proc/modules` and `lsmod` show the same data in different formats.

---

## Related Commands (Important)

### Load a Module

`sudo modprobe module_name`

### Remove a Module

`sudo modprobe -r module_name`

### Module Information

`modinfo module_name`

---

## Example Use Case

**Problem:** USB device not detected  
**Check:**

`lsmod | grep usb`

If the USB module isn’t listed, it may not be loaded.

---

## `lsmod` vs Related Commands

| Command    | Purpose             |
| ---------- | ------------------- |
| `lsmod`    | List loaded modules |
| `modprobe` | Load/unload modules |
| `modinfo`  | Show module details |
| `uname -r` | Show kernel version |
## Summary

- **`lsmod` lists loaded kernel modules**
    
- Helps identify drivers and kernel features
    
- Reads data from `/proc/modules`
    
- Essential for Linux system troubleshooting