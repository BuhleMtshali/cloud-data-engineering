# 🐙💻 Day 005 — Git & GitHub Basics

> **Phase 01: Tech Foundations**  
> **Topic:** Git & GitHub  
> **Outcome:** Understand version control and confidently track, manage, and share code changes 🔄📦

---

## 🌱 Welcome to Day 5

Today we officially stop living the:

> “I changed the file and now I have no idea what I changed” 😭

life.

Git gives me history.

GitHub gives that history somewhere to live online.

Together they let me:

- track changes
- create checkpoints
- experiment safely
- undo mistakes
- work with branches
- collaborate
- push projects online
- keep proof of progress

Basically:

```text
CODE
↓
CHANGE
↓
TRACK
↓
COMMIT
↓
PUSH
↓
REPEAT
```

Version control is not just “save but fancier.”

It is the memory system of an engineering project. 🧠⚙️

---

# 🎯 Learning Objectives

By the end of Day 5, I should be able to:

- 🧠 Explain Git vs GitHub
- 📁 Understand what a repository is
- 🧭 Understand working directory, staging area, local repo, and remote
- 🔍 Use `git status`
- ➕ Stage changes with `git add`
- 📸 Create commits
- 🧾 Write useful commit messages
- 🔎 Inspect changes with `git diff`
- 🕰️ Inspect history with `git log`
- 🌳 Create and switch branches
- 🔀 Merge branches
- ☁️ Connect a local repo to GitHub
- ⬆️ Push commits
- ⬇️ Pull/fetch remote changes
- 🙈 Use `.gitignore`
- ↩️ Understand safe undo workflows
- 🎒 Temporarily store work with stash
- ⚔️ Understand what merge conflicts are
- 🐙 Understand Pull Requests at a beginner level

---

# 🧠 Git vs GitHub

```text
GIT
↓
version control software
```

```text
GITHUB
↓
online platform for hosting Git repositories
```

Git works locally.

GitHub adds:

```text
remote hosting
collaboration
pull requests
issues
GitHub Actions
portfolio visibility
```

So:

> **Git tracks the history. GitHub hosts and shares that history.** 🐙

---

# 📁 What Is a Repository?

A **repository**, or **repo**, is a project tracked by Git.

Create one:

```bash
git init
```

Git creates:

```text
.git/
```

That hidden folder stores the repository metadata and history.

Basically:

```text
.git = repository brain 🧠
```

---

# 🧠 The Core Git Workflow

```text
WORKING DIRECTORY
      ↓
    git add
      ↓
STAGING AREA
      ↓
  git commit
      ↓
LOCAL REPOSITORY
      ↓
   git push
      ↓
REMOTE / GITHUB
```

Short version:

```text
EDIT
 ↓
STAGE
 ↓
COMMIT
 ↓
PUSH
```

---

# 🎭 Git File States

| State | Meaning |
|---|---|
| Untracked | Git sees the file but is not tracking it yet |
| Unmodified | File is tracked and unchanged |
| Modified | Tracked file has changed |
| Staged | Change selected for next commit |
| Committed | Change saved into Git history |

Flow:

```text
UNTRACKED
   ↓ git add
STAGED
   ↓ git commit
COMMITTED
   ↓ edit
MODIFIED
   ↓ git add
STAGED
```

---

# 🧰 Master Git Command Table

| Command / Concept | What It Does | Example | What It Means |
|---|---|---|---|
| `git --version` | Shows Git version | `git --version` | Confirms Git is installed |
| `git init` | Creates a new repo | `git init` | Creates `.git/` |
| `git status` | Shows repo state | `git status` | Git GPS 🧭 |
| `git add file` | Stages one file | `git add README.md` | Include in next commit |
| `git add .` | Stages current directory changes | `git add .` | Convenient, but review first |
| `git add -A` | Stages all repo changes | `git add -A` | Includes additions, edits, deletions |
| `git restore --staged file` | Unstages a file | `git restore --staged README.md` | Keeps local edit |
| `git diff` | Shows unstaged changes | `git diff` | What changed before staging |
| `git diff --staged` | Shows staged changes | `git diff --staged` | What next commit will include |
| `git commit -m` | Creates commit | `git commit -m "Add Day 5 notes"` | Saves staged snapshot |
| `git log` | Shows commit history | `git log` | Detailed history |
| `git log --oneline` | Compact history | `git log --oneline` | Great daily command |
| `git log --graph --oneline --all` | Visual branch history | `git log --graph --oneline --all` | Terminal history map |
| `git show HASH` | Shows one commit | `git show a1b2c3d` | Inspect by commit ID |
| `git branch` | Lists branches | `git branch` | `*` marks current branch |
| `git switch branch` | Switches branch | `git switch main` | Modern branch switch |
| `git switch -c name` | Creates + switches branch | `git switch -c feature-x` | Very handy |
| `git merge branch` | Merges branch | `git merge feature-x` | Combines histories |
| `git branch -d name` | Deletes merged branch | `git branch -d feature-x` | Safe deletion |
| `git remote -v` | Shows remotes | `git remote -v` | See GitHub connection |
| `git remote add origin URL` | Adds remote | `git remote add origin <url>` | Connect local to GitHub |
| `git push` | Uploads commits | `git push` | Local → remote |
| `git push -u origin main` | First push + upstream | `git push -u origin main` | Future push becomes easier |
| `git fetch` | Downloads remote updates | `git fetch` | Does not merge automatically |
| `git pull` | Fetches + integrates | `git pull` | Remote → current branch |
| `git clone URL` | Downloads existing repo | `git clone <url>` | Creates local copy |
| `git rm file` | Removes + stages deletion | `git rm old.txt` | Git-aware delete |
| `git mv old new` | Renames + stages | `git mv old.txt new.txt` | Git-aware rename |
| `git restore file` | Restores tracked file | `git restore README.md` | Discards unstaged edit 🚨 |
| `git revert HASH` | Creates undo commit | `git revert a1b2c3d` | Safe for shared history |
| `git reset --soft` | Moves history, keeps changes staged | `git reset --soft HEAD~1` | History rewrite tool |
| `git reset --hard` | Moves history and discards changes | `git reset --hard HEAD~1` | Dangerous 💀 |
| `git stash` | Temporarily stores work | `git stash` | Put unfinished work aside |
| `git stash list` | Lists stashes | `git stash list` | See stash history |
| `git stash pop` | Restores latest stash | `git stash pop` | Bring work back |
| `git tag` | Creates/lists tags | `git tag v1.0.0` | Useful for releases |
| `git config` | Reads/sets Git config | `git config --global user.name "Buhle"` | Configure identity |

---

# 🧭 `git status` = Git GPS

Whenever Git feels confusing:

```bash
git status
```

It tells me:

- current branch
- staged files
- modified files
- untracked files
- whether branch differs from remote

```text
confused?
↓
git status
```

Works suspiciously often 😭

---

# 🧪 Step 1 — Create a Git Lab

```bash
mkdir ~/git-day5-lab
cd ~/git-day5-lab
git init
```

Check:

```bash
ls -la
```

Look for:

```text
.git
```

---

# 📝 Step 2 — Create Files

```bash
echo "# Git & GitHub Day 5 Lab" > README.md
echo "Version control practice" > notes.txt
```

Now:

```bash
git status
```

They should appear as untracked.

---

# 📥 Step 3 — Stage Changes

```bash
git add README.md
git status
```

Then:

```bash
git add notes.txt
```

---

# 🎬 What Is the Staging Area?

Think of a commit like taking a photo. 📸

The working directory may contain many changes.

The staging area lets me choose:

> “These specific changes belong in the next snapshot.”

Then:

```bash
git commit
```

takes the photo.

---

# 📸 Step 4 — Commit

Check identity:

```bash
git config --global user.name
git config --global user.email
```

If needed:

```bash
git config --global user.name "Buhle"
git config --global user.email "your-email@example.com"
```

Commit:

```bash
git commit -m "Create Day 5 Git lab"
```

Then:

```bash
git status
```

Possible result:

```text
nothing to commit, working tree clean
```

Tiny victory trumpet 🎺😭

---

# 🧾 Good Commit Messages

Avoid:

```text
update
stuff
changes
final
final-final
final-final-real-this-time 😭
```

Prefer:

```text
Add Day 5 Git notes
Create Bash backup script
Fix backup source validation
Document Linux permissions
Add service troubleshooting lab
```

A good commit message answers:

> **What changed?**

---

# 🔍 `git diff`

Modify:

```bash
echo "Learning version control" >> README.md
```

Check:

```bash
git diff
```

Stage:

```bash
git add README.md
```

Now:

```bash
git diff --staged
```

Mental model:

```text
git diff
→ working directory vs staging

git diff --staged
→ staging vs last commit
```

---

# 🕰️ Git History

```bash
git log
```

Compact:

```bash
git log --oneline
```

Example:

```text
f428b76 Add Bash backup script
3d991ae Document Linux permissions
91ab821 Add Linux CLI notes
```

---

# 🆔 Commit Hashes

Every commit gets an identifier.

Example:

```text
f428b7637abc...
```

Usually the short form is enough:

```text
f428b76
```

Think:

```text
commit hash = commit ID card 🪪
```

Inspect:

```bash
git show f428b76
```

---

# 🌳 Branches

Create:

```bash
git switch -c backup-improvements
```

Mental picture:

```text
main
  \
   backup-improvements
```

Branches are parallel code timelines 🌀

---

# 🧰 Branch Command Table

| Command | Meaning |
|---|---|
| `git branch` | List branches |
| `git branch feature` | Create branch |
| `git switch feature` | Switch branch |
| `git switch -c feature` | Create + switch |
| `git merge feature` | Merge into current branch |
| `git branch -d feature` | Delete merged branch |

---

# 🔀 Typical Branch Workflow

```bash
git switch -c backup-improvements
```

Make changes:

```bash
git add .
git commit -m "Add timestamped backups"
```

Return:

```bash
git switch main
```

Merge:

```bash
git merge backup-improvements
```

---

# ☁️ Connecting Local Git to GitHub

```bash
git remote add origin <repository-url>
```

Check:

```bash
git remote -v
```

`origin` is the conventional nickname for the remote repo.

---

# ⬆️ Push to GitHub

First push:

```bash
git push -u origin main
```

After that:

```bash
git push
```

is usually enough.

---

# ⬇️ `fetch` vs `pull`

## Fetch

```bash
git fetch
```

Downloads remote updates but does not automatically integrate them.

## Pull

```bash
git pull
```

Roughly:

```text
fetch
+
integrate
```

So:

```text
fetch = bring updates nearby 👀
pull  = bring updates into my branch 📥
```

---

# 📥 Clone

```bash
git clone <repository-url>
```

Downloads the project and its Git history.

---

# 🙈 `.gitignore`

Example:

```gitignore
.env
*.log
__pycache__/
venv/
node_modules/
.DS_Store
```

Create:

```bash
touch .gitignore
```

---

# 🔐 Security Note — Secrets Do NOT Belong in Git

Never intentionally commit:

```text
API keys
passwords
access tokens
private keys
cloud credentials
.env secrets
```

Important:

```text
.gitignore prevents future tracking
```

but:

```text
.gitignore does NOT erase something already committed
```

If a secret is committed, treat it as exposed and rotate it.

---

# ↩️ Undoing Changes

## Unstage

```bash
git restore --staged README.md
```

Keeps the edit but removes it from staging.

## Discard unstaged changes

```bash
git restore README.md
```

Restores tracked version.

🚨 Use carefully.

---

# 🔄 `revert` vs `reset`

## `git revert`

```bash
git revert HASH
```

Creates a new commit that reverses an old one.

Good for shared history.

## `git reset --soft`

```bash
git reset --soft HEAD~1
```

Moves history back, keeps changes staged.

## `git reset --hard`

```bash
git reset --hard HEAD~1
```

Moves history back and discards changes.

💀 Respect this command.

---

# 🎒 Stashing Work

```bash
git stash
```

Check:

```bash
git stash list
```

Bring back:

```bash
git stash pop
```

Tiny code backpack 🎒

---

# ⚔️ Merge Conflicts

Possible conflict markers:

```text
<<<<<<< HEAD
Current branch version
=======
Other branch version
>>>>>>> feature
```

Git is basically saying:

> “Friend, this is above my pay grade. You decide.” 😭

Resolve manually, then:

```bash
git add file
git commit
```

---

# 🐙 GitHub Concepts

| Concept | Meaning |
|---|---|
| Repository | Hosted Git project |
| Issue | Bug/task/discussion |
| Pull Request | Proposal to merge changes |
| Fork | Personal copy of another repo |
| Actions | GitHub CI/CD automation |
| Release | Packaged project version |
| README | Project landing page |

---

# 🔀 Pull Request Mental Model

```text
main
 ↓
create feature branch
 ↓
make changes
 ↓
commit
 ↓
push branch
 ↓
open Pull Request
 ↓
review
 ↓
merge
```

---

# 🧪 Day 5 Hands-On Lab

## 1️⃣ Create Repo

```bash
mkdir ~/git-day5-lab
cd ~/git-day5-lab
git init
```

## 2️⃣ Inspect

```bash
git status
ls -la
```

## 3️⃣ Create Files

```bash
echo "# Git & GitHub Day 5 Lab" > README.md
echo "Version control practice" > notes.txt
```

## 4️⃣ Stage

```bash
git add README.md
git status
git add notes.txt
```

## 5️⃣ Commit

```bash
git commit -m "Create Day 5 Git lab"
```

## 6️⃣ Modify

```bash
echo "" >> README.md
echo "Learning staging, commits and branches." >> README.md
```

Inspect:

```bash
git diff
```

Stage:

```bash
git add README.md
git diff --staged
```

Commit:

```bash
git commit -m "Document Git workflow"
```

## 7️⃣ View History

```bash
git log --oneline
git log --graph --oneline --all
```

## 8️⃣ Create Branch

```bash
git switch -c add-gitignore
printf "*.log\n.env\n" > .gitignore
git add .gitignore
git commit -m "Add Git ignore rules"
```

## 9️⃣ Merge Back

```bash
git switch main
git merge add-gitignore
```

Then:

```bash
git log --graph --oneline --all
```

---

---

# ⚠️ Common Beginner Mistakes

| Mistake | What Happens |
|---|---|
| Forgetting `git add` | Commit misses the change |
| Thinking save = commit | Saving and committing are different |
| `git add .` without checking | Unwanted files may be staged |
| Bad commit messages | History becomes useless |
| Committing `.env` | Potential secret leak 🔐💀 |
| Mixing up Git and GitHub | Workflow gets confusing |
| Pulling blindly | Unexpected changes/conflicts |
| `reset --hard` casually | Local work may vanish |
| Doing everything on `main` | Experiments become riskier |
| Ignoring `git status` | Walking through Git blindfolded 😭 |

---

# 🌍 Why Git Matters for Cloud Data Engineering

Git shows up in:

- 🐍 Python pipelines
- 🗃️ SQL transformations
- 🚰 ETL/ELT code
- 📊 dbt projects
- ☁️ cloud infrastructure
- 🧱 Terraform
- 🐳 Dockerfiles
- ☸️ Kubernetes manifests
- 🔐 security rules
- 📜 detection logic
- 🛠️ CI/CD pipelines
- ⚙️ configuration
- 📚 documentation

Future workflow:

```text
write code
↓
git add
↓
git commit
↓
git push
↓
Pull Request
↓
CI/CD checks
↓
deploy
```

Git becomes part of the engineering control system. 🧠⚙️

---

# 🎯 Day 5 Commands to Burn Into Memory

```bash
git init

git status

git add

git diff
git diff --staged

git commit -m

git log --oneline

git branch
git switch
git switch -c

git merge

git remote -v

git fetch
git pull
git push

git clone

git restore

git stash
```

Remember:

```text
EDIT
 ↓
STAGE
 ↓
COMMIT
 ↓
PUSH
```

---

# ✅ Day 5 Completion Checklist

- [ ✅ ] I understand Git vs GitHub
- [ ✅ ] I understand what a repository is
- [ ✅ ] I know what `.git/` is
- [ ✅ ] I understand working directory vs staging area
- [ ✅ ] I can use `git status`
- [ ✅ ] I can stage changes
- [ ✅ ] I can create commits
- [ ✅ ] I can write useful commit messages
- [ ✅ ] I can use `git diff`
- [ ✅ ] I can inspect commit history
- [ ✅ ] I understand commit hashes
- [ ✅ ] I can create a branch
- [ ✅ ] I can switch branches
- [ ✅ ] I understand merging
- [ ✅ ] I understand remotes
- [ ✅ ] I understand push
- [ ✅ ] I understand fetch vs pull
- [ ✅ ] I can clone a repo
- [ ✅ ] I understand `.gitignore`
- [ ✅ ] I understand why secrets should not enter Git
- [ ✅ ] I can unstage a file
- [ ✅ ] I understand `revert` vs `reset`
- [ ✅ ] I understand stash
- [ ✅ ] I understand merge conflicts
- [ ✅ ] I understand Pull Requests
- [ ✅ ] Version control no longer feels like “Save As v27 FINAL REAL” 😌🐙

---

# 📚 Useful Reference Commands

```bash
git help
git help status
git help commit
git help branch
git help merge

git status --help
git commit --help
git log --help
```

---

# 🔜 Next Step

Day 1 taught me where things live.

Day 2 taught me who can access them.

Day 3 taught me what is running.

Day 4 taught me how to automate Linux.

Day 5 taught me how to **track every change I make while building all of it**.

Now the journey has history.

And history has receipts. 🧾🐙🔥

**Edit → Stage → Commit → Push → Learn → Repeat.**
