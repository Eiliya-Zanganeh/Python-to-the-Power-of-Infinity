# PowerShell Terminal Commands

## `cd` (Set-Location)
Change the current working directory.

```powershell
# Go to a specific path
cd C:\Windows\System32

# Go up one level
cd ..

# Go to user home directory
cd ~

# Go to root of current drive
cd \
```

**Output:** Prompt changes to reflect new location.
```
PS C:\Windows\System32>
```

---

## `mkdir` (New-Item)
Create a new directory.

```powershell
# Create single folder
mkdir Projects

# Create nested folders in one command
mkdir C:\Users\Admin\Documents\Projects\2026

# Create multiple folders at once
mkdir Folder1, Folder2, Folder3
```

**Output:**
```
    Directory: C:\Users\Admin

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d----          29/06/2026    14:30                Projects
```

---

## `mv` (Move-Item)
Move or rename files and folders.

```powershell
# Move file to another folder
mv report.pdf C:\Backup\

# Rename a file
mv old_document.docx new_document.docx

# Move and rename at the same time
mv C:\Temp\data.csv C:\Archive\data_2026.csv

# Move entire folder
mv C:\OldProject C:\Archive\
```

**Output:** No output on success unless `-PassThru` is used.
```
    Directory: C:\Backup

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a---          29/06/2026    14:35          1024 report.pdf
```

---

## `cp` (Copy-Item)
Copy files and folders.

```powershell
# Copy file to another location
cp config.json C:\Backup\

# Copy folder recursively
cp -Recurse C:\Project C:\Backup\

# Copy multiple files with wildcard
cp *.log C:\Logs\Archive\

# Copy and rename
cp template.txt C:\Output\final.txt
```

**Output:** No output on success unless `-PassThru` is used.
```
    Directory: C:\Backup

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a---          29/06/2026    14:40            512 config.json
```

---

## `rm` (Remove-Item)
Delete files and folders.

```powershell
# Delete a single file
rm temp.txt

# Delete folder and all contents
rm -Recurse C:\OldData

# Delete all .log files in a folder
rm C:\Logs\*.log

# Force delete without confirmation
rm -Force important.txt
```

**Output:** No output on success.
```
# When used without -Force on a folder:
Confirm
The item at C:\OldData has children and the Recurse parameter
was not specified. Are you sure you want to continue?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help
```

---

## `ls` (Get-ChildItem)
List files and folders in a directory.

```powershell
# List current directory
ls

# List specific path
ls C:\Windows

# List hidden items
ls -Hidden

# List recursively
ls -Recurse
```

**Output:**
```
    Directory: C:\Users\Admin\Projects

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d----          29/06/2026    14:30                src
d----          29/06/2026    14:31                docs
-a---          29/06/2026    14:32           2048 README.md
-a---          29/06/2026    14:33            512 script.ps1
```

---

## `clear` (Clear-Host)
Clear all output from the terminal screen.

```powershell
clear
```

**Output:** Terminal screen is completely cleared. Only the prompt remains at the top.
```
PS C:\Users\Admin>
```