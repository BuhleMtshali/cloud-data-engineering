# ⚙️🐧 Day 003 — Linux Processes & Services

> **Phase 01: Tech Foundations**  
> **Topic:** Processes & Services  
> **Outcome:** Understand how Linux runs, manages, monitors, and troubleshoots services 🔍⚙️

---

## 🌱 Welcome to Day 3

Day 1 taught me how to move around Linux.

Day 2 taught me who is allowed to touch what.

Day 3 asks a new question:

> “What is actually running on this machine right now?” 👀

Today is all about **processes, services, daemons, systemd, signals, jobs, logs, and troubleshooting**.

This is where Linux starts feeling alive.

Programs are not just sitting on disk anymore.

They are running. They have IDs. They have parents. They consume memory. They can crash. They can restart.

And sometimes they refuse to die until Linux sends the digital equivalent of:

```text
We are no longer negotiating. 💀
```

---

# 🎯 Learning Objectives

By the end of Day 3, I should be able to:

- ⚙️ Explain what a process is
- 🪪 Understand PID and PPID
- 🌳 Understand parent and child processes
- 📸 Inspect processes with `ps`
- 🎥 Monitor processes live with `top`
- 🔍 Find processes with `pgrep` and `pidof`
- 🧵 Understand foreground and background jobs
- ⏸️ Pause, resume, and move jobs between foreground/background
- 💀 Send signals to processes using `kill`
- 🧠 Understand `SIGTERM` vs `SIGKILL`
- 👻 Explain what a daemon is
- 🏗️ Understand what `systemd` does
- 🚦 Manage services with `systemctl`
- 🔥 Understand `start` vs `enable`
- 📜 Inspect service logs with `journalctl`
- 🧪 Troubleshoot a failed or inactive service
- ☁️ Understand why processes and services matter in cloud/data engineering

---

# 🧠 First Mental Model: Program vs Process

A **program** is code sitting on disk.

Example:

```text
/usr/bin/python3
```

A **process** is that program **currently running**.

```text
PROGRAM
python3
   ↓ run it
PROCESS
python3 → PID 4281
```

If I run the same program twice:

```bash
python3 script.py
python3 script.py
```

Linux can create two separate processes:

```text
python3 → PID 4281
python3 → PID 4289
```

Same program. Different running instances.

---

# 🪪 PID & PPID

Every running process gets a:

```text
PID = Process ID
```

Processes can also create other processes. That introduces:

```text
PPID = Parent Process ID
```

Example:

```text
bash
PID 2000
   ↓ starts
python3
PID 2040
PPID 2000
```

So:

```text
bash    = parent process
python3 = child process
```

This connects directly to Day 2:

```text
Buhle shell
└── James shell
```

James was **not a child user**. But James's shell process could be a **child process** of Buhle's shell process. 🧠✨

---

# 🧰 Master Process Command Table

| Command / Concept | What It Does | Example | What It Means |
|---|---|---|---|
| `process` | A running instance of a program | `python3 app.py` | Python becomes a running process |
| `PID` | Unique process ID | `ps` | Linux uses it to identify a process |
| `PPID` | Parent process ID | `ps -ef` | Shows which process created another |
| `ps` | Shows processes attached to current shell | `ps` | Quick process snapshot |
| `ps -e` | Shows all processes | `ps -e` | System-wide process list |
| `ps -f` | Full-format process output | `ps -f` | Includes UID, PID, PPID, command |
| `ps -ef` | All processes in full format | `ps -ef` | Very useful for process relationships |
| `ps aux` | Detailed process information | `ps aux` | Shows CPU, memory, PID, user, command |
| `ps aux \| grep name` | Searches process list | `ps aux \| grep nginx` | Quick process lookup |
| `pgrep name` | Finds process IDs by name | `pgrep ssh` | Returns matching PIDs |
| `pgrep -a name` | Shows PID and full command | `pgrep -a ssh` | Better process lookup |
| `pidof name` | Finds PIDs of a named program | `pidof sshd` | Similar purpose to `pgrep` |
| `pstree` | Displays processes as a tree | `pstree` | Shows parent/child relationships |
| `pstree -p` | Shows process tree with PIDs | `pstree -p` | Easier relationship tracing |
| `top` | Live process monitor | `top` | Real-time CPU/memory/process activity |
| `htop` | Interactive process monitor if installed | `htop` | Friendlier version of `top` |
| `uptime` | Shows uptime and load averages | `uptime` | Quick system-health view |
| `free -h` | Displays memory usage | `free -h` | Shows RAM and swap usage |
| `lsof` | Lists open files/resources | `lsof` | Shows resources opened by processes |
| `lsof -p PID` | Shows resources opened by one process | `lsof -p 1234` | Useful for investigation |
| `lsof -i` | Shows network-related open files | `lsof -i` | Connects networking to processes |

---

# 📸 `ps` vs 🎥 `top`

Think:

```text
ps  = photograph 📸
top = livestream 🎥
```

## `ps`

```bash
ps aux
```

Useful columns:

| Column | Meaning |
|---|---|
| `USER` | User running the process |
| `PID` | Process ID |
| `%CPU` | CPU usage |
| `%MEM` | Memory usage |
| `VSZ` | Virtual memory size |
| `RSS` | Physical memory currently used |
| `STAT` | Process state |
| `COMMAND` | Command that started the process |

## `top`

```bash
top
```

Useful keys:

| Key | What It Does |
|---|---|
| `q` | Quit |
| `P` | Sort by CPU |
| `M` | Sort by memory |
| `k` | Kill a process |
| `1` | Show individual CPU cores |

---

# 🌳 Process Trees

```bash
pstree -p
```

Example:

```text
systemd(1)
├── sshd(900)
│   └── bash(1200)
│       └── python3(1300)
└── cron(950)
```

This lets me see who launched whom.

---

# 🧵 Foreground vs Background Processes

## Foreground

```bash
sleep 300
```

The process controls the terminal.

## Background

```bash
sleep 300 &
```

Linux may show:

```text
[1] 4832
```

Where:

```text
1    = job number
4832 = PID
```

---

# 🧰 Job Control Table

| Command / Shortcut | What It Does | Example |
|---|---|---|
| `command &` | Starts command in background | `sleep 300 &` |
| `jobs` | Lists current shell jobs | `jobs` |
| `Ctrl + Z` | Suspends foreground process | Press `Ctrl + Z` |
| `bg` | Resumes suspended job in background | `bg` |
| `bg %1` | Resume job 1 in background | `bg %1` |
| `fg` | Bring latest background job to foreground | `fg` |
| `fg %1` | Bring job 1 to foreground | `fg %1` |
| `Ctrl + C` | Sends interrupt signal | Press `Ctrl + C` |

---

# 💀 Signals & Killing Processes

By default:

```bash
kill 1234
```

sends:

```text
SIGTERM
```

Meaning:

> “Please shut down cleanly.”

## 📡 Common Signals

| Signal | Number | Meaning |
|---|---:|---|
| `SIGHUP` | `1` | Hangup / often reload-related |
| `SIGINT` | `2` | Interrupt, commonly `Ctrl + C` |
| `SIGKILL` | `9` | Force termination |
| `SIGTERM` | `15` | Graceful termination request |
| `SIGCONT` | `18` | Continue paused process |
| `SIGSTOP` | `19` | Pause process |

View them:

```bash
kill -l
```

---

# 🤝 `SIGTERM` vs 💀 `SIGKILL`

Graceful:

```bash
kill 1234
```

or:

```bash
kill -15 1234
```

Forceful:

```bash
kill -9 1234
```

`SIGKILL` is the:

> “We are done discussing this.” 💀

option.

Use graceful termination first whenever possible.

---

# 🧰 Process Termination Table

| Command | What It Does | Example |
|---|---|---|
| `kill PID` | Sends `SIGTERM` | `kill 1234` |
| `kill -15 PID` | Explicit `SIGTERM` | `kill -15 1234` |
| `kill -9 PID` | Sends `SIGKILL` | `kill -9 1234` |
| `killall name` | Signals processes by name | `killall firefox` |
| `pkill name` | Signals matching processes | `pkill nginx` |
| `pkill -TERM name` | Graceful termination by name | `pkill -TERM nginx` |

---

# 🎚️ Process Priority

A **nice value** influences CPU scheduling priority.

```text
lower nice value  → higher priority
higher nice value → lower priority
```

Typical range:

```text
-20 → highest priority
 19 → lowest priority
```

| Command | What It Does | Example |
|---|---|---|
| `nice` | Starts process with chosen nice value | `nice -n 10 python3 job.py` |
| `renice` | Changes a running process priority | `renice 10 -p 1234` |

---

# ⚙️ Process vs Service

A **process** is any running program.

A **service** is usually a long-running system function managed by a service manager such as `systemd`.

Example:

```text
SERVICE
ssh.service
    ↓ manages
PROCESS
sshd
PID 1532
```

Not every process is a service.

---

# 👻 What Is a Daemon?

A **daemon** is typically a long-running background process that provides a service or waits for events.

Examples:

```text
sshd
cron
systemd
```

Think:

```text
daemon = background worker 👻⚙️
```

---

# 🏗️ What Is `systemd`?

`systemd` is the service manager used by many modern Linux systems.

It handles things like:

```text
boot
services
dependencies
timers
mounts
sessions
logging
```

The main command used to talk to it is:

```bash
systemctl
```

Mental model:

```text
ME
 ↓
systemctl
 ↓
systemd
 ↓
service
 ↓
process
```

---

# 🧰 Master `systemctl` Table

| Command | What It Does | Example |
|---|---|---|
| `systemctl status service` | Shows service status | `systemctl status ssh` |
| `systemctl start service` | Starts service now | `sudo systemctl start ssh` |
| `systemctl stop service` | Stops service now | `sudo systemctl stop ssh` |
| `systemctl restart service` | Stops then starts service | `sudo systemctl restart ssh` |
| `systemctl reload service` | Reloads configuration if supported | `sudo systemctl reload nginx` |
| `systemctl enable service` | Configures boot startup | `sudo systemctl enable ssh` |
| `systemctl disable service` | Prevents boot startup | `sudo systemctl disable ssh` |
| `systemctl enable --now service` | Enable + start immediately | `sudo systemctl enable --now ssh` |
| `systemctl disable --now service` | Disable + stop immediately | `sudo systemctl disable --now ssh` |
| `systemctl is-active service` | Checks current runtime state | `systemctl is-active ssh` |
| `systemctl is-enabled service` | Checks boot enablement | `systemctl is-enabled ssh` |
| `systemctl list-units --type=service` | Lists loaded services | `systemctl list-units --type=service` |
| `systemctl list-units --type=service --state=running` | Lists running services | `systemctl list-units --type=service --state=running` |
| `systemctl list-unit-files --type=service` | Lists installed service unit files | `systemctl list-unit-files --type=service` |
| `systemctl --failed` | Shows failed units | `systemctl --failed` |
| `systemctl cat service` | Shows service unit definition | `systemctl cat ssh` |
| `systemctl show service` | Shows detailed unit properties | `systemctl show ssh` |
| `systemctl daemon-reload` | Reloads unit definitions after edits | `sudo systemctl daemon-reload` |

---

# 🚦 Service States

| State | Meaning |
|---|---|
| `active (running)` | Service is currently running |
| `inactive (dead)` | Not running |
| `activating` | Starting |
| `deactivating` | Stopping |
| `failed` | Service failed |
| `active (exited)` | One-time service finished successfully |

---

# 🧠 `start` vs `enable`

```bash
sudo systemctl start ssh
```

means:

> Start SSH **right now**.

```bash
sudo systemctl enable ssh
```

means:

> Start SSH automatically on future boots.

So:

```text
START  = now
ENABLE = future boots
```

Want both?

```bash
sudo systemctl enable --now ssh
```

---

# 🧾 Service Unit Locations

Common locations:

```text
/etc/systemd/system/
/usr/lib/systemd/system/
```

Useful commands:

```bash
ls /etc/systemd/system
ls /usr/lib/systemd/system
systemctl cat ssh
```

---

# 📜 Service Logs with `journalctl`

| Command | What It Does | Example |
|---|---|---|
| `journalctl` | Shows system journal logs | `journalctl` |
| `journalctl -u service` | Shows one service's logs | `journalctl -u ssh` |
| `journalctl -u service -n 50` | Last 50 entries | `journalctl -u ssh -n 50` |
| `journalctl -u service -f` | Follows logs live | `journalctl -u ssh -f` |
| `journalctl -b` | Current boot logs | `journalctl -b` |
| `journalctl -b -1` | Previous boot logs if retained | `journalctl -b -1` |
| `journalctl -p err` | Error-priority messages | `journalctl -p err` |
| `journalctl --since today` | Logs since today began | `journalctl --since today` |

Mental model:

```text
SERVICE
↓
PROCESS
↓
LOGS
```

That triangle is ridiculously important later. 🔥

---

# 🧠 Service Troubleshooting Flow

When a service breaks, do **not** just restart it 14 times and hope Linux develops empathy. 😭

```text
1. Is it running?
        ↓
systemctl status SERVICE

2. Did anything fail?
        ↓
systemctl --failed

3. What do the logs say?
        ↓
journalctl -u SERVICE

4. Is the process actually running?
        ↓
pgrep / ps

5. Is it consuming weird resources?
        ↓
top / free / lsof
```

Example:

```bash
systemctl status ssh
journalctl -u ssh -n 50
pgrep -a ssh
```

---

# 🔍 Troubleshooting Cheat Sheet

| Command | Question It Answers |
|---|---|
| `systemctl status ssh` | Is SSH running? |
| `systemctl is-active ssh` | Is it active right now? |
| `systemctl is-enabled ssh` | Will it start after reboot? |
| `systemctl --failed` | What services failed? |
| `journalctl -u ssh` | What has SSH been logging? |
| `pgrep -a ssh` | Which SSH processes are running? |
| `ps aux` | What is running system-wide? |
| `top` | What is consuming CPU/memory? |
| `free -h` | Is memory under pressure? |
| `lsof -i` | Which processes are using network resources? |

---

# 🧪 Day 3 Hands-On Lab

## 1️⃣ Inspect Current Processes

```bash
ps
ps -ef
ps aux
```

Look for:

```text
PID
PPID
USER
%CPU
%MEM
COMMAND
```

## 2️⃣ Inspect Process Relationships

```bash
pstree
pstree -p
```

Find the terminal shell and inspect what lives underneath it. 🌳🐧

## 3️⃣ Create a Foreground Process

```bash
sleep 300
```

Then press:

```text
Ctrl + C
```

## 4️⃣ Create a Background Process

```bash
sleep 300 &
```

Check it:

```bash
jobs
pgrep -a sleep
```

## 5️⃣ Practise Job Control

```bash
fg %1
```

Press:

```text
Ctrl + Z
```

Then:

```bash
bg %1
jobs
```

## 6️⃣ Terminate It Gracefully

```bash
pgrep -a sleep
kill PID
```

Verify:

```bash
pgrep -a sleep
```

---

# ⚙️ Service Lab

## 1️⃣ List Running Services

```bash
systemctl list-units --type=service --state=running
```

## 2️⃣ Inspect SSH

```bash
systemctl status ssh
```

Look for:

```text
Loaded:
Active:
Main PID:
Tasks:
Memory:
```

## 3️⃣ Check Runtime vs Boot State

```bash
systemctl is-active ssh
systemctl is-enabled ssh
```

Remember:

```text
active  = running now
enabled = configured for boot
```

## 4️⃣ Inspect Logs

```bash
journalctl -u ssh -n 20
```

Now I am connecting:

```text
service
+
process
+
logs
```

That is proper troubleshooting brain. 🔍🧠

---

---

# ⚠️ Common Beginner Mistakes

## ❌ Assuming every process is a service

```text
every service may involve processes
but
not every process is a service
```

## ❌ Confusing PID with job number

```text
[1] 4832
```

means:

```text
1    = shell job number
4832 = process ID
```

## ❌ Using `kill -9` immediately

Try graceful termination first:

```bash
kill PID
```

## ❌ Confusing `start` and `enable`

```text
start  = now
enable = boot
```

## ❌ Restarting without checking logs

Investigate first:

```bash
systemctl status SERVICE
journalctl -u SERVICE
```

## ❌ Assuming `inactive` means broken

A service can simply be stopped because it is not needed right now.

Context matters.

---

# 🌍 Why This Matters for Cloud Data Engineering

Processes and services are everywhere:

- ☁️ Cloud VMs
- 🐍 Python data workers
- 🚰 ETL services
- 🧱 Airflow components
- 🗃️ Database servers
- 🐳 Docker containers
- ☸️ Kubernetes workloads
- 📜 Logging agents
- 🔐 Security agents
- 🛠️ CI/CD runners
- 📊 Monitoring tools
- 🌐 Web/API services

When a pipeline suddenly dies at 02:13, someone has to answer:

```text
Is the service running?
Did the process crash?
Was it killed?
Did it run out of memory?
What PID owned the workload?
What do the logs say?
```

That someone should eventually be me. 😌⚙️

---

# 🧠 Day 3 Core Mental Models

```text
PROGRAM
↓
PROCESS
↓
PID
```

```text
PARENT PROCESS
↓
CHILD PROCESS
```

```text
SERVICE
↓
managed by systemd
↓
PROCESS
```

```text
systemctl
↓
controls services
```

```text
journalctl
↓
reads service/system logs
```

And:

```text
ps  = snapshot
top = live view
```

---

# 🎯 Commands I Want to Remember

```bash
ps
ps -ef
ps aux

pgrep -a
pstree -p

top
free -h

jobs
bg
fg

kill
kill -l

systemctl status
systemctl start
systemctl stop
systemctl restart
systemctl enable
systemctl disable
systemctl is-active
systemctl is-enabled
systemctl --failed

journalctl -u
```

---

# ✅ Day 3 Completion Checklist

- [ ] I understand program vs process
- [ ] I understand PID
- [ ] I understand PPID
- [ ] I understand parent/child processes
- [ ] I can use `ps`
- [ ] I can use `ps aux`
- [ ] I can use `pgrep`
- [ ] I can read `pstree`
- [ ] I understand foreground vs background jobs
- [ ] I can use `jobs`
- [ ] I understand `bg` and `fg`
- [ ] I understand `Ctrl + C`
- [ ] I understand `Ctrl + Z`
- [ ] I understand Linux signals
- [ ] I understand `SIGTERM`
- [ ] I understand why `SIGKILL` is a last resort
- [ ] I understand process vs service
- [ ] I understand what a daemon is
- [ ] I understand what `systemd` does
- [ ] I can use `systemctl`
- [ ] I understand `start` vs `enable`
- [ ] I can check whether a service is active
- [ ] I can check whether a service is enabled
- [ ] I can inspect service logs
- [ ] I understand `journalctl`
- [ ] I completed the process lab
- [ ] I completed the service lab
- [ ] Linux processes no longer feel like invisible ghosts running around the machine 👻😌

---

---

# 📚 Useful Reference Commands

```bash
man ps
man top
man kill
man systemctl
man journalctl
man systemd
man nice
man renice
man lsof

ps --help
systemctl --help
journalctl --help
```

---

# 🔜 Next Step

Day 1 taught me **where things live**.

Day 2 taught me **who is allowed to touch them**.

Day 3 taught me **what is actually running and how Linux keeps it alive**.

Now Linux is starting to feel less like a pile of commands and more like a real system:

```text
files
+
users
+
permissions
+
processes
+
services
+
logs
```

The machine is starting to speak.

I am finally learning the accent. 🐧⚙️✨

**Learn → Inspect → Run → Stop → Troubleshoot → Document → Repeat.**
