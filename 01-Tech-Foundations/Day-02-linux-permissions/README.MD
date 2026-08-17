# 🔐🐧 Day 002 — Linux File Permissions & Ownership

> **Phase 01: Tech Foundations**  
> **Topic:** File Permissions, Ownership, Users & Groups  
> **Outcome:** Understand how Linux decides **who can access what** 👀🔑

---

## 🌱 Welcome to Day 2

Yesterday I learned how to move around Linux.

Today Linux looked me dead in the eye and said:

> “Cool. But are you actually allowed to touch that file?” 😭

This day is all about **permissions, ownership, users, groups, and privilege**.

By the end of this, strings like:

```text
-rwxr-xr--
```

and commands like:

```bash
chmod 754 file.txt
```

should stop looking like ancient runes carved into a server room wall. 🐧📜

The big idea:

```text
WHO are you?
↓
WHO owns the file?
↓
WHICH group applies?
↓
WHAT permissions are allowed?
```

Linux access control is basically very strict nightclub security. No wristband? No entry. 😭🔐

---

# 🎯 Learning Objectives

By the end of Day 2, I should be able to:

- 👤 Understand Linux users and user IDs
- 👥 Understand groups and group IDs
- 🔍 Read `id`, `whoami`, and `groups`
- 📁 Understand file ownership
- 🔐 Read `rwx` permissions confidently
- 🧠 Understand **owner / group / others**
- 🔢 Decode numeric permissions like `600`, `640`, `700`, `754`, and `755`
- 💡 Understand why `r = 4`, `w = 2`, and `x = 1`
- 🛠️ Use `chmod` to change permissions
- 👑 Use `chown` and `chgrp` to change ownership
- 👤 Create users
- 👥 Create and manage groups
- ➕ Add users to groups safely
- 🏠 Understand user home directories
- 🐚 Understand login shells
- 🔑 Understand what `sudo` actually means
- 🔄 Switch between users correctly
- 🚪 Understand why `exit` returns to the previous shell

---

# 🧠 The Linux Permission Mental Model

Every file or directory has:

```text
OWNER
GROUP
OTHERS
```

And each of those can receive:

```text
r = read
w = write
x = execute
```

Linux is constantly asking:

```text
Who is requesting access?
        ↓
Are they the owner?
        ↓
If not, are they in the owning group?
        ↓
If not, use "others"
        ↓
Check the permissions for that class
```

That is the permission engine in miniature. 🔐⚙️

---

# 👀 Reading `ls -l`

Run:

```bash
ls -l
```

Example:

```text
-rwxr-xr-- 1 buhle developers 2048 Aug 17 10:30 script.sh
```

Breakdown:

```text
- | rwx | r-x | r--
    │     │      │
    │     │      └── Others
    │     └───────── Group
    └─────────────── Owner
```

| Section | Meaning |
|---|---|
| `-` | Regular file |
| `rwx` | Owner permissions |
| `r-x` | Group permissions |
| `r--` | Others permissions |
| `buhle` | Owner |
| `developers` | Owning group |

---

# 🧱 File Types

| Symbol | Meaning |
|---|---|
| `-` | Regular file |
| `d` | Directory |
| `l` | Symbolic link |
| `c` | Character device |
| `b` | Block device |
| `p` | Named pipe |
| `s` | Socket |

---

# 🔐 Permission Symbols

| Permission | Symbol | Meaning |
|---|---|---|
| Read | `r` | View/read |
| Write | `w` | Modify |
| Execute | `x` | Run or enter |
| None | `-` | Permission not granted |

---

# 📄 File Permissions vs 📁 Directory Permissions

| Permission | On a File | On a Directory |
|---|---|---|
| `r` | Read file contents | List filenames inside |
| `w` | Change file contents | Create/delete/rename entries |
| `x` | Execute file | Enter/traverse the directory |

So:

```text
drwx------
```

means only the owner gets access. Everyone else gets the Linux version of “private property, keep walking.” 😭

---

# 👤 Owner, Group & Others

Permissions always split into three groups:

```text
OWNER | GROUP | OTHERS
```

Example:

```text
rwxr-xr--
```

Split it:

```text
rwx | r-x | r--
```

| Class | Permissions |
|---|---|
| Owner | `rwx` |
| Group | `r-x` |
| Others | `r--` |

---

# 🔢 Binary / Octal Permissions

Each permission is a binary switch:

```text
r   w   x
4   2   1
```

Why?

```text
r = 100 = 4
w = 010 = 2
x = 001 = 1
```

## 🧩 Complete Permission Number Table

| Number | Binary | Permission | Meaning |
|---:|:---:|:---:|---|
| `0` | `000` | `---` | Nothing |
| `1` | `001` | `--x` | Execute |
| `2` | `010` | `-w-` | Write |
| `3` | `011` | `-wx` | Write + execute |
| `4` | `100` | `r--` | Read |
| `5` | `101` | `r-x` | Read + execute |
| `6` | `110` | `rw-` | Read + write |
| `7` | `111` | `rwx` | Read + write + execute |

Memory key:

```text
r = 4
w = 2
x = 1
```

---

# 🧮 Decoding `754`

```text
OWNER | GROUP | OTHERS
  7   |   5   |   4
```

| Class | Calculation | Result |
|---|---|---|
| Owner | `4+2+1` | `rwx` |
| Group | `4+1` | `r-x` |
| Others | `4` | `r--` |

So:

```text
754 = rwxr-xr--
```

---

# 🧮 Decoding `600`

```text
6 | 0 | 0
```

```text
6 = rw-
0 = ---
0 = ---
```

So:

```text
600 = rw-------
```

| Who | Access |
|---|---|
| Owner | Read + write |
| Group | Nothing |
| Others | Nothing |

Basically: “mine, mine, absolutely not yours.” 😭🔐

---

# 🧰 Common Permission Modes

| Mode | Symbolic | Meaning |
|---:|---|---|
| `600` | `rw-------` | Private file |
| `640` | `rw-r-----` | Owner RW, group read |
| `644` | `rw-r--r--` | Common regular file |
| `700` | `rwx------` | Private directory/executable |
| `750` | `rwxr-x---` | Owner full, group read/execute |
| `754` | `rwxr-xr--` | Owner full, group RX, others read |
| `755` | `rwxr-xr-x` | Common directory/executable |
| `777` | `rwxrwxrwx` | Everyone gets everything 🚨 |

---

# 🛠️ `chmod` — Change Permissions

| Command | What It Does | Example |
|---|---|---|
| `chmod 640 file` | Sets exact numeric permissions | `chmod 640 report.txt` |
| `chmod u+x file` | Adds execute for owner | `chmod u+x script.sh` |
| `chmod u-w file` | Removes owner write | `chmod u-w notes.txt` |
| `chmod g+r file` | Adds group read | `chmod g+r report.txt` |
| `chmod g+w file` | Adds group write | `chmod g+w shared.txt` |
| `chmod o-r file` | Removes others read | `chmod o-r secret.txt` |
| `chmod o-rwx file` | Removes all others access | `chmod o-rwx private.txt` |
| `chmod a+r file` | Gives read to everyone | `chmod a+r notes.txt` |

Symbols:

```text
u = owner
g = group
o = others
a = all
```

Operators:

```text
+ = add
- = remove
= = set exactly
```

---

# 🚨 Why `chmod 777` Is Usually Sus

```bash
chmod 777 file
```

means:

```text
Owner  → rwx
Group  → rwx
Others → rwx
```

That is basically “everybody gets keys.” 😭🔑

It can hide a permissions problem instead of actually fixing it.

---

# 👑 Ownership vs Permissions

Keep this burned into memory:

```text
chown = WHO owns it
chgrp = WHICH GROUP owns it
chmod = WHAT they can do
```

| Command | What It Does | Example |
|---|---|---|
| `chown` | Changes owner | `sudo chown james file.txt` |
| `chown user:group` | Changes owner + group | `sudo chown james:developers file.txt` |
| `chgrp` | Changes group | `chgrp developers file.txt` |
| `chmod` | Changes permissions | `chmod 640 file.txt` |

---

# 👤 Linux Identity

| Command | What It Does | Example |
|---|---|---|
| `whoami` | Shows current username | `whoami` |
| `id` | Shows UID, GID, and groups | `id` |
| `id user` | Shows another user's identity | `id james` |
| `groups` | Shows current groups | `groups` |
| `groups user` | Shows another user's groups | `groups james` |

Example:

```text
uid=1000(buhle) gid=1000(buhle) groups=1000(buhle),27(sudo),124(wireshark),...
```

| Part | Meaning |
|---|---|
| `uid=1000(buhle)` | User ID |
| `gid=1000(buhle)` | Primary group ID |
| `groups=...` | Supplementary groups |

Linux sees the numbers. Humans see the names. Very computer-core behaviour 😭

---

# 👥 Primary vs Supplementary Groups

Every user has:

```text
1 primary group
+
0 or more supplementary groups
```

Example:

```text
buhle
├── primary group: buhle
├── supplementary: sudo
└── supplementary: wireshark
```

---

# 👤 Creating Users

On Kali / Debian-style systems:

```bash
sudo adduser james
```

This normally:

- creates `james`
- creates `/home/james`
- creates a matching group
- copies starter files from `/etc/skel`
- asks for a password
- asks for optional account info

Verify:

```bash
id james
getent passwd james
```

---

# 🧱 `adduser` vs `useradd`

| Command | What It Means |
|---|---|
| `sudo adduser james` | Friendly interactive user creation |
| `sudo useradd james` | Lower-level user creation |
| `sudo useradd -m james` | Create user + home directory |
| `sudo useradd -m -s /bin/bash james` | Create user + home + Bash shell |

---

# 🏠 User Home Directories

A new user may have:

```text
/home/james
```

but `ls` can look empty.

Check hidden files:

```bash
ls -la /home/james
```

You may see:

```text
.bashrc
.profile
.bash_logout
```

These commonly come from:

```text
/etc/skel
```

Check it:

```bash
ls -la /etc/skel
```

---

# 🖥️ Why No Desktop / Documents / Downloads?

Those folders are often handled by **XDG user directories** and may appear after a graphical login/session.

If needed:

```bash
xdg-user-dirs-update
```

Or create them manually:

```bash
mkdir ~/Desktop ~/Documents ~/Downloads
```

---

# 🐚 Login Shells

Check James's user record:

```bash
getent passwd james
```

Example:

```text
james:x:1001:1001:James:/home/james:/bin/bash
```

The last field:

```text
/bin/bash
```

is his login shell.

Important:

```text
shell ≠ admin power
```

James can have Bash and still be a normal non-admin user.

---

# 🔑 `sudo` Is Separate

Example setup:

```text
buhle → sudo-capable ✅
james → normal user ❌
```

If James runs:

```bash
sudo apt update
```

and gets:

```text
james is not in the sudoers file
```

that means James is **not allowed to elevate privileges**.

It does not mean James has no shell.

---

# 👑 Add a User to `sudo`

Only if I intentionally want James to have admin-capable access:

```bash
sudo usermod -aG sudo james
```

Verify:

```bash
id james
```

For learning, keeping James as a normal user is actually useful because I can test permission boundaries properly. 🔐

---

# 👥 Creating Groups

Create:

```bash
sudo groupadd developers
```

Verify:

```bash
getent group developers
```

---

# ➕ Add a User to a Group

```bash
sudo usermod -aG developers james
```

Breakdown:

```text
-a = append
-G = supplementary groups
```

Memory trick:

```text
-aG = append group
```

---

# 🚨 The `-G` Trap

Risky if I intend to preserve existing memberships:

```bash
sudo usermod -G developers james
```

Safer:

```bash
sudo usermod -aG developers james
```

Without `-a`, I can replace James's existing supplementary group list.

---

# 🔡 `-g` vs `-G`

| Option | Meaning |
|---|---|
| `-g` | Primary group |
| `-G` | Supplementary groups |

Example:

```bash
sudo usermod -g developers james
```

changes the primary group.

```bash
sudo usermod -aG developers james
```

adds a supplementary group.

Tiny capital letter. Massive difference 😭

---

# ➖ Removing Users from Groups

```bash
sudo gpasswd -d james developers
```

or on Debian-style systems:

```bash
sudo deluser james developers
```

Verify:

```bash
groups james
```

---

# 🗑️ Deleting Users & Groups

| Command | Meaning |
|---|---|
| `sudo userdel james` | Delete user |
| `sudo userdel -r james` | Delete user + home directory |
| `sudo deluser james` | Debian-friendly user deletion |
| `sudo groupdel developers` | Delete group |

Be careful with `-r` because that can remove the user's home files too.

---

# 🔄 Switching Users

From Buhle:

```bash
sudo su james
```

This changes identity but may leave the current working directory unchanged.

Example:

```text
(james㉿kali)-[/home/buhle]
```

That means:

```text
WHOAMI = james
LOCATION = /home/buhle
```

Identity and location are separate things.

---

# 🏠 Login-Style User Switch

Use:

```bash
sudo su - james
```

or:

```bash
sudo -iu james
```

Then:

```bash
whoami
pwd
```

should show James and usually `/home/james`.

---

# 🚪 Returning to Buhle

If I switched from Buhle into James:

```text
Buhle shell
└── James shell
```

I can return with:

```bash
exit
```

or:

```text
Ctrl + D
```

No `sudo` required from James. The James shell closes and the Buhle shell underneath becomes active again.

---

# 👶 Is James a Child User?

Nope.

James is a separate user account.

What can be parent/child is the **shell process**:

```text
Buhle shell process
└── James shell process
```

So:

```text
users ≠ parent/child hierarchy
processes = can have parent/child relationships
```

---

# 🎭 `umask` Basics

`umask` influences permissions on **new** files and directories.

Check:

```bash
umask
```

Common value:

```text
0022
```

Typical results:

```text
new files       → 644
new directories → 755
```

Restrictive example:

```bash
umask 077
```

Often gives:

```text
new files       → 600
new directories → 700
```

Important:

```text
umask is not the permission itself
```

It controls which requested permissions are masked away.

---

# 🧠 ACLs — Extra Permission Rules

Classic permissions give:

```text
owner
owning group
others
```

ACLs let me add extra rules for specific users or groups.

| Command | What It Does | Example |
|---|---|---|
| `getfacl` | View ACLs | `getfacl report.txt` |
| `setfacl -m` | Add/modify ACL | `setfacl -m u:james:r report.txt` |
| `setfacl -x` | Remove ACL entry | `setfacl -x u:james report.txt` |

---

# 🔍 Debugging `Permission denied`

Do **not** immediately unleash:

```bash
chmod 777 everything
```

😭

Instead:

```bash
whoami
id
ls -l file
getfacl file
namei -l /full/path/to/file
```

Mental checklist:

```text
Who am I?
↓
What groups am I in?
↓
Who owns the file?
↓
What permissions exist?
↓
Are ACLs involved?
↓
Can I traverse every parent directory?
```

---

# 🧰 Master Command Table

| Command | What It Does | Example |
|---|---|---|
| `ls -l` | View permissions & ownership | `ls -l file.txt` |
| `ls -la` | Include hidden files | `ls -la` |
| `stat` | Detailed file metadata | `stat file.txt` |
| `whoami` | Current username | `whoami` |
| `id` | Current UID/GID/groups | `id` |
| `id user` | Inspect another user | `id james` |
| `groups` | Current groups | `groups` |
| `chmod` | Change permissions | `chmod 640 file.txt` |
| `chmod u+x` | Add owner execute | `chmod u+x script.sh` |
| `chown` | Change owner | `sudo chown james file.txt` |
| `chown user:group` | Change owner + group | `sudo chown james:developers file.txt` |
| `chgrp` | Change group owner | `chgrp developers file.txt` |
| `adduser` | Create user | `sudo adduser james` |
| `useradd -m` | Create user + home | `sudo useradd -m james` |
| `passwd` | Set/change password | `sudo passwd james` |
| `groupadd` | Create group | `sudo groupadd developers` |
| `usermod -aG` | Add supplementary group | `sudo usermod -aG developers james` |
| `usermod -g` | Change primary group | `sudo usermod -g developers james` |
| `getent passwd` | Inspect user record | `getent passwd james` |
| `getent group` | Inspect group record | `getent group developers` |
| `sudo -l` | Show sudo permissions | `sudo -l` |
| `sudo su james` | Switch identity | `sudo su james` |
| `sudo su - james` | Login-style switch | `sudo su - james` |
| `sudo -iu james` | Login-style switch via sudo | `sudo -iu james` |
| `exit` | Close current shell | `exit` |
| `umask` | Show default creation mask | `umask` |
| `getfacl` | View ACL permissions | `getfacl file.txt` |
| `setfacl` | Set ACL permissions | `setfacl -m u:james:r file.txt` |
| `namei -l` | Inspect permissions along a path | `namei -l /home/james/file.txt` |

---

# 🧪 Day 2 Hands-On Lab

## 1️⃣ Create a Test User

```bash
sudo adduser james
```

Verify:

```bash
id james
getent passwd james
```

## 2️⃣ Create a Group

```bash
sudo groupadd data-team
```

Verify:

```bash
getent group data-team
```

## 3️⃣ Add James to the Group

```bash
sudo usermod -aG data-team james
```

Verify:

```bash
id james
```

## 4️⃣ Create a Lab File

```bash
sudo touch /tmp/report.txt
sudo chown james:data-team /tmp/report.txt
sudo chmod 640 /tmp/report.txt
ls -l /tmp/report.txt
```

Expected shape:

```text
-rw-r----- 1 james data-team ... report.txt
```

Decode:

```text
Owner  → rw- → 6
Group  → r-- → 4
Others → --- → 0
```

## 5️⃣ Switch to James

```bash
sudo -iu james
```

Check:

```bash
whoami
pwd
id
```

Return:

```bash
exit
```

---

# 🧩 Mini Challenges

## Challenge 1

Decode:

```text
-rwxr-x---
```

Answer:

```text
Owner  = 7
Group  = 5
Others = 0
Numeric = 750
```

## Challenge 2

Decode:

```text
-rw-r--r--
```

What numeric permission is this? 644

## Challenge 3

What does:

```bash
chmod 700 private/
```

mean for owner, group, and others? Only the owner has permission to that file

---

# ⚠️ Common Beginner Mistakes

## ❌ Mixing up `chmod` and `chown`

```text
chmod = permissions
chown = ownership
```

## ❌ Thinking `700` creates a user

Nope. `chmod 700 /home/james` only changes permissions on that directory.

## ❌ Thinking a shell means admin access

```text
/bin/bash ≠ sudo
```

## ❌ Thinking James is Buhle's child user

Separate account. Only the shell process may be nested.

## ❌ Forgetting `-a` in `usermod -aG`

Safer:

```bash
sudo usermod -aG developers james
```

## ❌ Using `777` because something broke

Permission problem may disappear. Security problem may arrive wearing sunglasses. 😭

---

# 🌍 Why This Matters for Cloud Data Engineering

These concepts show up everywhere:

- ☁️ Cloud VMs
- 🐧 Linux servers
- 📊 Data pipeline workers
- 🗃️ Shared datasets
- 🔑 SSH keys
- 🐳 Docker containers
- ☸️ Kubernetes nodes
- 🛠️ CI/CD runners
- 🔐 Secret files
- 📜 Application logs
- 🚰 ETL directories
- 👥 Service accounts

A pipeline can fail because of:

```text
wrong owner
wrong group
wrong permissions
wrong user
wrong path
```

And Linux will often just say:

```text
Permission denied
```

No emotional support. No explanation. Just vibes. 😭🐧

---

# ✅ Day 2 Completion Checklist

- [ ✅] I understand owner, group, and others
- [ ✅] I can read `rwx`
- [ ✅] I know `r=4`, `w=2`, `x=1`
- [ ✅] I can decode numeric permissions
- [ ✅] I understand `600`, `640`, `700`, `754`, `755`
- [ ✅] I can explain why `777` is risky
- [ ✅] I understand `chmod` vs `chown`
- [ ✅] I understand `chgrp`
- [ ✅] I can interpret `id`
- [ ✅] I understand UID and GID
- [ ✅] I understand primary vs supplementary groups
- [ ✅] I can create a user
- [ ✅] I can create a group
- [ ✅] I can add a user to a group safely
- [ ✅] I understand `-g` vs `-G`
- [ ✅] I understand `sudo`
- [ ✅] I understand why James is not automatically an admin
- [ ✅] I understand that a shell and sudo access are separate
- [ ✅] I know how to switch users
- [ ✅] I know how to return with `exit`
- [ ✅] I understand why James is not a child user
- [ ✅] Permission strings no longer look like keyboard damage 😌

---

# 🪞 Reflection

### 💡 What clicked today?

> The biggest breakthrough was understanding that permissions split into **owner / group / others**, and each section can be calculated using `4 + 2 + 1`.

### 🤯 What confused me at first?

> Commands like `chmod 600` looked random until I understood the binary/octal system.

### 🧠 Biggest lesson

```text
chown = who owns it
chmod = what they can do
sudo  = whether I can elevate privileges
```

### 🧾 Today's Win

> Add my own reflection here.

---

# 📚 Useful Reference Commands

```bash
man chmod
man chown
man chgrp
man id
man adduser
man useradd
man usermod
man groupadd
man sudo
man su

chmod --help
chown --help
id --help
```

---

# 🔜 Next Step

Day 1 taught me how to **move through Linux**.

Day 2 taught me that moving through Linux does not mean Linux will let me touch everything. 😭🔐

Now I understand:

```text
identity
+
ownership
+
groups
+
permissions
+
privilege
```

And suddenly Linux access control feels less like black magic and more like a system I can reason about.

**Learn → Decode → Test → Break safely → Fix → Document → Repeat.** 🐧🧱✨
