# 🐧💻 Day 001 — Linux CLI Basics

> **Phase 01: Tech Foundations**  
> **Topic:** Linux CLI Basics  
> **Today's Task:** Navigate the Linux filesystem confidently from the terminal 🧭

---

## 🌱 Welcome to Day 1

Before cloud platforms.

Before pipelines.

Before containers.

Before security automation.

There is Linux. 🐧

Today is about getting comfortable inside the terminal and learning how to move around the Linux filesystem without relying on a GUI.

The goal is simple:

> Know **where I am**, **what is around me**, **where I want to go**, and **how to inspect what I find**.

Tiny commands today. Massive payoff later. ☁️📊🔐

---

## 🎯 Learning Objectives

By the end of this day, I should be able to:

- 📍 Identify my current working directory
- 📂 Move between directories confidently
- 🏠 Navigate using root, home, parent, and current-directory paths
- 👀 List files and folders, including hidden files
- 🧠 Understand absolute vs relative paths
- 📁 Create files and directories
- 📦 Copy, move, rename, and remove files safely
- 🔎 Locate files and commands
- 📖 Inspect file contents from the terminal
- 🔗 Understand pipes and redirection at a beginner level
- 🔐 Read basic Linux permission output
- 💾 Inspect basic filesystem and disk information
- ⌨️ Use terminal shortcuts that make CLI work faster

---

# 🧠 Linux Filesystem Mental Model

Linux uses one large directory tree.

Everything starts at:

```text
/
```

This is called the **root directory**.

A simplified filesystem may look like:

```text
/
├── bin/
├── etc/
├── home/
│   └── buhle/
│       ├── Documents/
│       ├── Downloads/
│       └── projects/
├── tmp/
├── usr/
└── var/
```

At any moment in the terminal, I am standing somewhere inside this tree.

The core navigation questions are:

```text
pwd  → Where am I?
ls   → What is here?
cd   → Take me somewhere else.
find → Where did that file go? 😭
```

---

# 🗺️ Important Path Symbols

| Symbol | Meaning | Example |
|---|---|---|
| `/` | Root of the entire filesystem | `cd /` |
| `~` | Current user's home directory | `cd ~` |
| `.` | Current directory | `ls .` |
| `..` | Parent directory | `cd ..` |
| `../..` | Two directories up | `cd ../..` |
| `-` | Previous working directory when used with `cd` | `cd -` |

---

## 📍 Absolute vs Relative Paths

### Absolute Path

Starts from the filesystem root `/`.

```bash
cd /home/buhle/Documents
```

### Relative Path

Starts from my current location.

```bash
cd Documents
```

If I am already inside `/home/buhle`, both commands can lead to the same place.

---

# 🧰 Master Linux CLI Command Reference

## 🧭 Navigation & Paths

| Command / Syntax | What It Does | Example |
|---|---|---|
| `pwd` | Prints the full path of the current working directory | `pwd` |
| `cd directory` | Changes into a directory | `cd Documents` |
| `cd /path/to/folder` | Moves using an absolute path | `cd /etc` |
| `cd ..` | Moves one directory up | `cd ..` |
| `cd ../..` | Moves two directories up | `cd ../..` |
| `cd ../../..` | Moves three directories up | `cd ../../..` |
| `cd ~` | Moves to the current user's home directory | `cd ~` |
| `cd` | Also returns to the home directory | `cd` |
| `cd -` | Returns to the previous working directory | `cd -` |
| `ls .` | Lists the current directory explicitly | `ls .` |
| `ls ..` | Lists the parent directory without moving into it | `ls ..` |
| `realpath path` | Shows the resolved absolute path | `realpath ../README.md` |
| `basename path` | Returns only the final filename or directory name | `basename /var/log/syslog` |
| `dirname path` | Returns the directory portion of a path | `dirname /var/log/syslog` |
| `pushd directory` | Moves to a directory while saving the previous location on a stack | `pushd /var/log` |
| `popd` | Returns to the last directory saved by `pushd` | `popd` |
| `dirs` | Displays the current directory stack | `dirs -v` |

---

## 👀 Listing Files & Directories

| Command / Syntax | What It Does | Example |
|---|---|---|
| `ls` | Lists files and directories | `ls` |
| `ls -l` | Shows a detailed long listing | `ls -l` |
| `ls -a` | Shows all files, including hidden files beginning with `.` | `ls -a` |
| `ls -la` | Combines long listing with hidden files | `ls -la` |
| `ls -lh` | Shows file sizes in human-readable format | `ls -lh` |
| `ls -R` | Recursively lists subdirectories | `ls -R` |
| `ls -t` | Sorts files by modification time | `ls -lt` |
| `ls -S` | Sorts files by size | `ls -lS` |
| `ls -d */` | Lists directories only in the current folder | `ls -d */` |
| `tree` | Displays folders visually as a tree if installed | `tree` |
| `tree -L 2` | Limits tree output to two levels | `tree -L 2` |

> 💡 **Important:** `ls -a` is the option specifically responsible for showing hidden files.  
> `ls -la` simply combines `-l` and `-a`.

---

# 🔐 Understanding `ls -l`

Example:

```text
-rwxr-xr-- 1 buhle developers 2048 Aug 11 10:30 script.sh
```

Breakdown:

```text
-  rwx  r-x  r--
│   │    │    │
│   │    │    └── others
│   │    └─────── group
│   └──────────── owner
└──────────────── file type
```

### File Type

| Symbol | Meaning |
|---|---|
| `-` | Regular file |
| `d` | Directory |
| `l` | Symbolic link |

### Permission Symbols

| Symbol | Meaning |
|---|---|
| `r` | Read |
| `w` | Write |
| `x` | Execute / enter directory |
| `-` | Permission not granted |

---

## 📁 Creating Files & Directories

| Command / Syntax | What It Does | Example |
|---|---|---|
| `touch file` | Creates an empty file if it does not exist, or updates its timestamp | `touch notes.txt` |
| `mkdir directory` | Creates a directory | `mkdir linux-lab` |
| `mkdir -p path/to/folder` | Creates nested directories and missing parents | `mkdir -p labs/linux/navigation` |
| `echo "text" > file` | Writes text into a file, replacing existing contents | `echo "Linux Day 1" > notes.txt` |
| `echo "text" >> file` | Appends text to the end of a file | `echo "pwd shows my location" >> notes.txt` |
| `cat > file` | Redirects keyboard input into a file until input ends | `cat > notes.txt` |

> 🧠 `cat > file` is not a special "create file" version of `cat`.  
> The shell's `>` operator redirects output into the file.

---

## 📦 Copying, Moving & Renaming

| Command / Syntax | What It Does | Example |
|---|---|---|
| `cp source destination` | Copies a file | `cp notes.txt notes-backup.txt` |
| `cp file directory/` | Copies a file into another directory | `cp notes.txt docs/` |
| `cp -r source/ destination/` | Copies a directory recursively | `cp -r data/ data-backup/` |
| `cp -i source destination` | Prompts before overwriting | `cp -i report.txt archive/report.txt` |
| `mv old new` | Renames a file or directory | `mv draft.txt final.txt` |
| `mv file directory/` | Moves a file into another directory | `mv report.csv data/` |
| `mv -i source destination` | Prompts before overwriting | `mv -i report.csv data/` |

---

## 🗑️ Removing Files & Directories

| Command / Syntax | What It Does | Example |
|---|---|---|
| `rm file` | Deletes a file | `rm notes.txt` |
| `rm -i file` | Prompts before deleting | `rm -i notes.txt` |
| `rmdir directory` | Removes an empty directory | `rmdir empty-folder` |
| `rm -r directory/` | Removes a directory and its contents recursively | `rm -r old-lab/` |
| `rm -rf directory/` | Forcefully removes a directory tree without normal prompts | `rm -rf ./temporary-lab/` |

> 🚨 `rm -rf` is powerful and unforgiving.  
> Before deleting anything important:

```bash
pwd
ls
```

Then read the command again before pressing Enter. 😭

---

## 🔗 Links

| Command / Syntax | What It Does | Example |
|---|---|---|
| `ln file linkname` | Creates a hard link | `ln data.csv data-hardlink.csv` |
| `ln -s target linkname` | Creates a symbolic link | `ln -s /var/log/app.log latest.log` |
| `readlink linkname` | Shows the target of a symbolic link | `readlink latest.log` |

---

## 📖 Reading & Inspecting Files

| Command / Syntax | What It Does | Example |
|---|---|---|
| `cat file` | Prints the entire file | `cat notes.txt` |
| `cat -n file` | Prints file contents with line numbers | `cat -n notes.txt` |
| `head file` | Shows the first 10 lines by default | `head notes.txt` |
| `head -n 20 file` | Shows the first 20 lines | `head -n 20 app.log` |
| `tail file` | Shows the last 10 lines by default | `tail app.log` |
| `tail -n 20 file` | Shows the last 20 lines | `tail -n 20 app.log` |
| `tail -f file` | Follows new lines added to a file in real time | `tail -f app.log` |
| `less file` | Opens a scrollable viewer | `less /etc/services` |
| `more file` | Displays file content page by page | `more /etc/services` |
| `nl file` | Displays file contents with numbered lines | `nl notes.txt` |
| `file filename` | Identifies the type of a file | `file dataset.csv` |
| `stat filename` | Displays detailed file metadata | `stat README.md` |
| `wc file` | Counts lines, words, and bytes | `wc notes.txt` |
| `wc -l file` | Counts lines only | `wc -l app.log` |
| `wc -w file` | Counts words only | `wc -w notes.txt` |

---

## 🔎 Finding Files & Commands

| Command / Syntax | What It Does | Example |
|---|---|---|
| `find path` | Searches through a directory tree | `find .` |
| `find . -name "file.txt"` | Finds entries matching a name | `find . -name "notes.txt"` |
| `find . -iname "readme*"` | Case-insensitive name search | `find . -iname "readme*"` |
| `find . -type f` | Finds regular files | `find . -type f` |
| `find . -type d` | Finds directories | `find . -type d` |
| `find . -type f -name "*.csv"` | Finds CSV files | `find . -type f -name "*.csv"` |
| `find . -maxdepth 2 -type f` | Limits search depth | `find . -maxdepth 2 -type f` |
| `find . -size +100M` | Finds files larger than 100 MB | `find . -size +100M` |
| `find . -mtime -1` | Finds files modified within the last day | `find . -mtime -1` |
| `locate filename` | Searches a pre-built filename database | `locate apache2.conf` |
| `sudo updatedb` | Updates the database used by `locate` | `sudo updatedb` |
| `which command` | Shows the executable found in `PATH` | `which python3` |
| `whereis command` | Finds binary, source, and manual locations | `whereis python3` |
| `command -v command` | Shows how the current shell resolves a command | `command -v python3` |
| `type command` | Shows whether something is an alias, builtin, function, or executable | `type cd` |

> 💡 `find` is much more powerful than an exact-name search.  
> It can filter by **name, type, size, modification time, ownership, permissions, depth, and more**.

---

## 🔍 Searching Inside Files

| Command / Syntax | What It Does | Example |
|---|---|---|
| `grep "text" file` | Searches for matching text inside a file | `grep "ERROR" app.log` |
| `grep -i "text" file` | Case-insensitive search | `grep -i "error" app.log` |
| `grep -n "text" file` | Shows matching line numbers | `grep -n "ERROR" app.log` |
| `grep -v "text" file` | Shows lines that do not match | `grep -v "DEBUG" app.log` |
| `grep -r "text" directory/` | Searches recursively inside files | `grep -r "database" config/` |
| `grep -E "pattern" file` | Uses extended regular expressions | `grep -E "ERROR|WARNING" app.log` |

---

# 🔀 Pipes & Redirection

Linux commands become much more powerful when their input and output are connected.

| Syntax | What It Does | Example |
|---|---|---|
| `|` | Sends one command's output into another | `cat app.log | grep "ERROR"` |
| `>` | Writes output to a file and overwrites it | `ls -la > directory-list.txt` |
| `>>` | Appends output to a file | `echo "Day 1 complete" >> notes.txt` |
| `<` | Uses a file as standard input | `wc -l < notes.txt` |
| `2>` | Redirects error output | `find / -name "*.log" 2> errors.txt` |
| `2> /dev/null` | Discards error output | `find / -name "*.log" 2> /dev/null` |
| `2>&1` | Sends standard error to the same destination as standard output | `command > output.txt 2>&1` |

`/dev/null` is basically the Linux void. Things sent there disappear. 🕳️

---

# ✨ Wildcards & Globbing

| Pattern | Meaning | Example |
|---|---|---|
| `*` | Matches zero or more characters | `ls *.txt` |
| `?` | Matches exactly one character | `ls file?.txt` |
| `[abc]` | Matches one character from the set | `ls file[123].txt` |
| `[0-9]` | Matches one digit in the range | `ls report[0-9].txt` |

---

# 🆘 Help & Documentation

| Command / Syntax | What It Does | Example |
|---|---|---|
| `command --help` | Shows a quick usage guide | `ls --help` |
| `man command` | Opens the manual page | `man ls` |
| `man -k keyword` | Searches manual descriptions | `man -k permissions` |
| `apropos keyword` | Searches manual-page descriptions | `apropos filesystem` |
| `info command` | Opens GNU info documentation where available | `info ls` |
| `history` | Displays command history | `history` |
| `history 20` | Shows recent commands | `history 20` |
| `clear` | Clears the visible terminal screen | `clear` |

---

# 👤 User & System Context

| Command / Syntax | What It Does | Example |
|---|---|---|
| `whoami` | Shows the current effective username | `whoami` |
| `id` | Shows user ID, group ID, and group memberships | `id` |
| `groups` | Shows current user's groups | `groups` |
| `hostname` | Shows the machine hostname | `hostname` |
| `uname` | Shows system information | `uname` |
| `uname -a` | Shows detailed kernel/system information | `uname -a` |

---

# 💾 Disk & Filesystem Context

| Command / Syntax | What It Does | Example |
|---|---|---|
| `df -h` | Shows filesystem usage in human-readable sizes | `df -h` |
| `df -i` | Shows inode usage | `df -i` |
| `du -sh directory/` | Shows total size of a directory | `du -sh data/` |
| `du -h --max-depth=1 .` | Shows disk usage one directory level down | `du -h --max-depth=1 .` |
| `lsblk` | Lists block devices | `lsblk` |
| `lsblk -f` | Shows filesystems and mount points | `lsblk -f` |
| `mount` | Shows mounted filesystems or mounts a filesystem | `mount` |
| `findmnt` | Displays mounted filesystems in a tree-like format | `findmnt` |

---

# 🔐 Permission Management Basics

| Command / Syntax | What It Does | Example |
|---|---|---|
| `chmod` | Changes file permissions | `chmod 640 secrets.txt` |
| `chmod +x file` | Adds execute permission | `chmod +x backup.sh` |
| `chmod u+x file` | Adds execute permission for the owner | `chmod u+x script.sh` |
| `chmod g-w file` | Removes write permission from the group | `chmod g-w report.txt` |
| `chown user file` | Changes file owner | `sudo chown buhle report.txt` |
| `chown user:group file` | Changes owner and group | `sudo chown buhle:developers report.txt` |
| `chgrp group file` | Changes group ownership | `chgrp developers report.txt` |

Numeric permission values:

```text
r = 4
w = 2
x = 1
```

Example:

```bash
chmod 750 script.sh
```

Means:

```text
7 = rwx → owner
5 = r-x → group
0 = --- → others
```

---

# ⌨️ Terminal Shortcuts Worth Learning Early

| Shortcut | What It Does |
|---|---|
| `Tab` | Auto-completes commands, filenames, and paths |
| `Tab` twice | Shows possible completions |
| `Ctrl + C` | Stops the currently running command |
| `Ctrl + L` | Clears the terminal screen |
| `Ctrl + A` | Moves cursor to the beginning of the command |
| `Ctrl + E` | Moves cursor to the end |
| `Ctrl + U` | Deletes from cursor to beginning of line |
| `Ctrl + K` | Deletes from cursor to end of line |
| `Ctrl + R` | Searches command history |
| `↑` / `↓` | Moves through previous commands |
| `Ctrl + D` | Sends end-of-file / exits some shells when line is empty |

---

# 🧪 Hands-On Lab — Build My Linux Playground

Time to make the terminal do some actual work. 😤🐧

## 1️⃣ Create the Lab

```bash
cd ~
mkdir -p linux-cli-lab/data/raw
cd linux-cli-lab
pwd
```

## 2️⃣ Inspect the Structure

```bash
ls
ls -la
tree
```

If `tree` is not installed, `ls -R` works too.

## 3️⃣ Create Files

```bash
touch notes.txt
touch data/raw/sample.csv
echo "Day 1: Linux CLI Basics" > notes.txt
echo "Filesystem navigation unlocked 🐧" >> notes.txt
cat notes.txt
```

## 4️⃣ Create a Documentation Folder

```bash
mkdir docs
cp notes.txt docs/notes-backup.txt
mv notes.txt linux-notes.txt
ls -lah
```

## 5️⃣ Inspect the File

```bash
file linux-notes.txt
stat linux-notes.txt
wc -l linux-notes.txt
```

## 6️⃣ Practise Navigation

```bash
cd data/raw
pwd
cd ..
pwd
cd ../..
pwd
cd ~
cd -
```

## 7️⃣ Find the File Again

```bash
find ~/linux-cli-lab -type f -name "linux-notes.txt"
find ~/linux-cli-lab -type f -name "*.txt"
```

## 8️⃣ Practise Search

```bash
grep "Linux" ~/linux-cli-lab/linux-notes.txt
grep -n "Linux" ~/linux-cli-lab/linux-notes.txt
```

## 9️⃣ Practise Redirection

```bash
ls -la ~/linux-cli-lab > directory-listing.txt
cat directory-listing.txt
```

## 🔟 Safe Cleanup Practice

```bash
mkdir disposable
touch disposable/test.txt
pwd
ls
rm -r disposable
```

Safety ritual complete. 🫡

---

# 🧩 Mini Challenge

Without using a GUI:

1. Create this structure:

```text
cloud-lab/
├── data/
│   ├── raw/
│   └── processed/
├── logs/
├── scripts/
└── README.txt
```

2. Add this text to `README.txt`:

```text
My first Linux CLI lab.
```

3. Copy `README.txt` into `logs/`.
4. Rename the copied file to `lab-info.txt`.
5. Find every `.txt` file under `cloud-lab`.
6. Display the full path to the `processed` directory.
7. Navigate back home using a single command.

---

# ⚠️ Common Beginner Mistakes

### ❌ Confusing `/` and `~`

```text
/  → filesystem root
~  → my home directory
```

Very different places. 😭

### ❌ Assuming hidden files are secure

A file beginning with `.` is only hidden from normal `ls` output.

```bash
ls -a
```

will reveal it.

### ❌ Forgetting quotes around wildcard patterns in `find`

Better:

```bash
find . -name "*.txt"
```

The shell can expand an unquoted wildcard before `find` receives it.

### ❌ Using `rm -rf` casually

That command has no emotional attachment to my files. 💀

### ❌ Running destructive commands without checking location

Before destructive work:

```bash
pwd
ls
```

Always.

---

# 🌍 Why This Matters for Cloud Data Engineering

Linux CLI skills appear everywhere:

- ☁️ Cloud virtual machines
- 🐳 Docker containers
- ☸️ Kubernetes workloads
- 📊 Data processing servers
- 🚰 ETL and ELT environments
- 🐍 Python automation
- 📜 Log investigation
- 🔐 Security troubleshooting
- 🛠️ CI/CD runners
- 🧱 Infrastructure automation

A cloud data engineer who can move confidently through Linux does not need a GUI to understand what is happening.

The filesystem starts feeling less like a maze and more like a map. 🗺️🐧

---

# ✅ Day 1 Completion Checklist

- [ ] I can explain what `/`, `~`, `.`, and `..` mean
- [ ] I understand absolute and relative paths
- [ ] I can use `pwd`
- [ ] I can navigate with `cd`
- [ ] I can inspect folders with `ls`
- [ ] I can show hidden files
- [ ] I can create files and folders
- [ ] I can copy, move, and rename files
- [ ] I can safely remove files and directories
- [ ] I can inspect a text file from the terminal
- [ ] I can search for files with `find`
- [ ] I can search inside files with `grep`
- [ ] I understand basic pipes and redirection
- [ ] I understand the basic structure of Linux permissions
- [ ] I completed the filesystem navigation lab
- [ ] I can navigate without terminal GPS panic 😌

---

# 🪞 Reflection

### 💡 What clicked today?

> Add reflection here.

### 🤔 What still feels confusing?

> Add reflection here.

### 🐧 Favourite command today

```text
Add command here.
```

### 🧾 Today's Win

> Add one thing I can do now that I could not do before.

---

# 📚 Resources

Useful references for this phase:

- GNU Coreutils Manual
- GNU Bash Manual
- GNU Findutils Manual
- Linux manual pages
- Ubuntu Linux Command Line for Beginners
- TLDR Pages

Useful local commands:

```bash
man ls
man find
man chmod

ls --help
find --help
grep --help
```

---

# 🔜 Next Step

Day 1 builds the navigation muscle.

From here, Linux stops being a mysterious black terminal and starts becoming an environment I can actually control. 🐧⚙️

**Learn → Practise → Break safely → Fix → Document → Repeat.** 🧱✨
