# 🐍🔐 Day 007 — Python Control Flow

> **Phase 01: Tech Foundations**
> **Topic:** Python Control Flow
> **Outcome:** Understand how Python makes decisions, repeats actions, and controls program execution 🧠⚙️

---

## 🧠 Welcome to Day 7

Today Python gets a brain. 🧠🐍

So far, I've been learning how to write Python syntax, create variables, use functions, and work with data.

Today I'm learning how to tell Python:

```text
🤔 "If this happens, do this."

🔀 "Otherwise, do that."

🔁 "Keep doing this."

🛑 "Stop here."

⏭️ "Skip this and keep going."
```

This is **control flow**.

Control flow determines **which parts of a program execute, when they execute, and how many times they execute.**

And this is where Python starts feeling less like a list of instructions and more like an actual program. 😤🐍

---

# 🎯 What This Day Covers

* 🚦 `if`
* 🔀 `elif`
* 🛑 `else`
* ⚖️ Comparison operators
* 🧠 Boolean values
* 🔗 Logical operators
* 🔁 `for` loops
* ♾️ `while` loops
* 🛑 `break`
* ⏭️ `continue`
* 🚀 `pass`
* 🔢 `range()`
* 🎯 `match / case`
* 🧩 Nested control flow
* 🛡️ Input validation
* 🔐 Authentication logic
* 🧪 Building a Mini Login Validator

---

# 🧠 Control Flow Mental Model

A normal program might simply execute:

```text
A
↓
B
↓
C
↓
D
```

Control flow allows the program to make decisions:

```text
             START
               ↓
          Get information
               ↓
         Check condition
          ↙           ↘
       TRUE           FALSE
        ↓                ↓
      Do A             Do B
        ↘                ↙
             CONTINUE
```

Or repeat:

```text
START
 ↓
CHECK
 ↓
TRUE?
 ↓
DO SOMETHING
 ↓
CHECK AGAIN
 ↓
FALSE
 ↓
STOP
```

This logic appears everywhere in software.

---

# 🚦 Conditional Statements

## `if`

Runs code when a condition is true.

```python
age = 20

if age >= 18:
    print("Access granted")
```

---

## `if / else`

Provides two possible paths.

```python
age = 16

if age >= 18:
    print("Access granted")
else:
    print("Access denied")
```

Mental model:

```text
IF true
   ↓
DO THIS

ELSE
   ↓
DO THAT
```

---

## `if / elif / else`

Useful when there are multiple possible conditions.

```python
score = 75

if score >= 80:
    print("Excellent")

elif score >= 60:
    print("Good")

else:
    print("Needs improvement")
```

Python checks the conditions from top to bottom.

Once a matching condition is found, its block executes.

---

# ⚖️ Comparison Operators

| Operator | Meaning               | Example              |
| -------- | --------------------- | -------------------- |
| `==`     | Equal to              | `status == "active"` |
| `!=`     | Not equal to          | `status != "active"` |
| `>`      | Greater than          | `score > 80`         |
| `<`      | Less than             | `score < 80`         |
| `>=`     | Greater than or equal | `age >= 18`          |
| `<=`     | Less than or equal    | `age <= 65`          |

### ⚠️ `=` vs `==`

This is important:

```python
age = 20
```

means:

> Store `20` inside `age`.

While:

```python
age == 20
```

means:

> Is `age` equal to `20`?

One `=` stores.

Two `==` compares.

Tiny symbols. Huge difference. 😭

---

# 🧠 Boolean Logic

Boolean values are:

```python
True
False
```

Example:

```python
logged_in = True
```

Python can use these values when making decisions.

---

# 🔗 Logical Operators

| Operator | Meaning                             | Example                |
| -------- | ----------------------------------- | ---------------------- |
| `and`    | Both conditions must be true        | `age >= 18 and has_id` |
| `or`     | At least one condition must be true | `admin or owner`       |
| `not`    | Reverses the result                 | `not active`           |

Example:

```python
age = 25
has_id = True

if age >= 18 and has_id:
    print("Access granted")
```

Both conditions must be true.

---

# 🔁 `for` Loops

A `for` loop repeats code for each item in a collection.

```python
tools = ["Linux", "Python", "Git"]

for tool in tools:
    print(tool)
```

Output:

```text
Linux
Python
Git
```

---

# ♾️ `while` Loops

A `while` loop continues while its condition is true.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```text
1
2
3
4
5
```

A common interactive-program pattern is:

```python
while True:
```

This keeps the program running until something stops the loop.

---

# 🛑 `break`

`break` immediately exits a loop.

```python
for number in range(10):

    if number == 5:
        break

    print(number)
```

Output:

```text
0
1
2
3
4
```

Once Python reaches `break`, the loop ends.

---

# ⏭️ `continue`

`continue` skips the current iteration and moves to the next one.

```python
for number in range(5):

    if number == 2:
        continue

    print(number)
```

Output:

```text
0
1
3
4
```

`2` gets skipped.

---

# 🚀 `pass`

`pass` is a placeholder.

```python
if condition:
    pass
```

It basically tells Python:

> "There's supposed to be code here, but we're not writing it yet."

Useful while building program structures.

---

# 🔢 `range()`

`range()` generates a sequence of numbers.

```python
range(5)
```

represents:

```text
0
1
2
3
4
```

Example:

```python
for number in range(1, 6):
    print(number)
```

Output:

```text
1
2
3
4
5
```

---

# 🎯 `match / case`

Python's `match / case` syntax can compare one value against different possibilities.

```python
operator = "+"

match operator:

    case "+":
        print("Addition")

    case "-":
        print("Subtraction")

    case "*":
        print("Multiplication")

    case "/":
        print("Division")

    case _:
        print("Invalid operator")
```

The `_` acts as the default case.

---

# 🧩 Nested Control Flow

Control structures can live inside other control structures.

Example:

```python
users = ["Buhle", "James"]

for user in users:

    if user == "Buhle":
        print("Admin user")

    else:
        print("Standard user")
```

Mental model:

```text
FOR every user
      ↓
CHECK the user
   ↙       ↘
Buhle     Other
 ↓          ↓
Admin    Standard
```

This pattern becomes incredibly useful when processing data.

---

# 🛡️ Input Validation

Control flow can also validate information supplied by users.

Example:

```python
number = int(input("Enter a number: "))

if number < 0:
    print("Invalid number")

else:
    print("Valid number")
```

Instead of blindly accepting everything, the program checks the data first.

That is the beginning of **defensive programming**. 🛡️

---

# 🔐 Why Control Flow Matters for Security

Today's project puts these concepts into an authentication scenario.

Authentication logic is essentially:

```text
USER ENTERS INFORMATION
        ↓
CHECK USERNAME
        ↓
DOES USER EXIST?
    ↙           ↘
  YES           NO
   ↓             ↓
CHECK PASSWORD   ERROR
   ↓
MATCH?
 ↙     ↘
YES     NO
 ↓       ↓
LOGIN   ERROR
```

That's control flow doing security-flavoured work. 🔐🐍

Later, this same style of logic can be used for:

* 🚨 suspicious login detection
* 📜 log analysis
* 🔍 security event filtering
* 🛡️ access-control logic
* ☁️ cloud automation
* 📊 data validation

---

# 🧪 Mini Project — Mini Login Validator 🤳🏽⛔️

Today's project is a small simulated login-validation program.

It uses:

```text
dictionaries
+
functions
+
input
+
string methods
+
if statements
+
nested conditions
+
while loops
+
return values
+
modules
+
timers
```

The program contains a simulated user database:

```python
USER_DATABASE = {

    "admin": "Secrete123!",

    "alice": "Wonderland99",

    "bob": "Builder456"

}
```

The program then checks whether:

1. 👤 The username exists
2. 🔑 The supplied password matches
3. 🔁 The user wants to perform another validation

---

# 💻 Project Code

```python
# IMPORTING THE TIMER FUNCTION

import threading


# WELCOME MESSAGE

print("================ 🤳🏽 MINI LOGIN VALIDATOR ⛔️ =================")


# SIMULATED USER DATABASE

USER_DATABASE = {

    "admin": "Secrete123!",

    "alice": "Wonderland99",

    "bob": "Builder456"

}


# VALIDATING IF THE REGISTERED USER IS THE ONE LOGGING IN

def login_check():

    print("------ 🗂️ Let's Validate 🐝 ------")

    username = input("Enter username: ").strip().lower()

    password = input("Enter password: ").strip()


    # CHECK IF THE USERNAME EXISTS

    if username in USER_DATABASE:


        # CHECKING IF THE PASSWORD MATCHES

        if USER_DATABASE[username] == password:

            print(
                f"----- ✅ Login successful! Welcome back {username}!"
            )

            return True

        else:

            print(
                "----- 🆘 ERROR: INCORRECT password."
            )

    else:

        print(
            "----- ⛔️ ERROR: USERNAME NOT FOUND ⛔️ ------"
        )


# STARTING FUNCTION

def login_validator():


    # STARTING WHILE LOOP

    while True:

        login_check()


        # CLOSING THE LOOP

        login_again = input(
            "====== ⛔️ Wanna check-in someone else? (yes/no): "
        ).lower()

        if login_again != "yes":

            print(
                "======== 🐧 THANK YOU, BYE 🆘 ======="
            )

            break


# CALLING THE TIMER FUNCTION

timer = threading.Timer(3, login_validator)

timer.start()
```

---

# 🔍 Breaking Down the Project

## 1️⃣ User Database

```python
USER_DATABASE = {
    "admin": "Secrete123!",
    "alice": "Wonderland99",
    "bob": "Builder456"
}
```

This is a Python dictionary.

The structure is:

```text
username → password
```

For example:

```text
admin → Secrete123!
```

This is only a **simulation for learning**.

Real authentication systems should not store passwords like this.

---

## 2️⃣ Getting the Username

```python
username = input("Enter username: ").strip().lower()
```

Three things happen here.

### `input()`

Gets information from the user.

### `.strip()`

Removes unnecessary whitespace around the input.

### `.lower()`

Converts the username to lowercase.

So:

```text
"  BUHLE  "
```

becomes:

```text
"buhle"
```

---

# 3️⃣ Checking Whether the User Exists

```python
if username in USER_DATABASE:
```

Python checks whether the username exists as a key in the dictionary.

Conceptually:

```text
Is username inside USER_DATABASE?
        ↓
     YES / NO
```

---

# 4️⃣ Nested `if`

Inside the first condition:

```python
if username in USER_DATABASE:
```

there is another condition:

```python
if USER_DATABASE[username] == password:
```

So the program performs two checks:

```text
CHECK USERNAME
      ↓
   EXISTS?
      ↓ YES
CHECK PASSWORD
      ↓
   MATCH?
```

This is **nested control flow**.

---

# 5️⃣ `return True`

If the credentials match:

```python
return True
```

The function immediately sends `True` back to wherever it was called.

The function is essentially saying:

> "Yep. Validation succeeded." ✅

---

# 6️⃣ `while True`

The validator uses:

```python
while True:
```

This allows the program to keep validating users.

The loop only ends when:

```python
break
```

is reached.

---

# 7️⃣ `break`

The user is asked:

```text
Wanna check-in someone else? (yes/no)
```

If the answer isn't `"yes"`:

```python
if login_again != "yes":
    break
```

The loop ends.

---

# 8️⃣ `threading.Timer`

The program finishes with:

```python
timer = threading.Timer(3, login_validator)

timer.start()
```

This means:

```text
Wait 3 seconds
      ↓
Run login_validator()
```

This connects back to the Python modules introduced on Day 6. 🐍🔗

---

# 🧠 Control Flow Used in the Project

| Concept     | Where It Appears                | Purpose                       |
| ----------- | ------------------------------- | ----------------------------- |
| `if`        | `if username in USER_DATABASE:` | Check whether user exists     |
| nested `if` | Password validation             | Check password after username |
| `else`      | Error handling                  | Handle failed conditions      |
| `while`     | `while True:`                   | Keep validator running        |
| `break`     | `if login_again != "yes"`       | Stop the loop                 |
| `return`    | `return True`                   | Return successful validation  |
| `in`        | `username in USER_DATABASE`     | Check dictionary membership   |
| `==`        | Password comparison             | Check equality                |
| `!=`        | Repeat decision                 | Check inequality              |
| `.lower()`  | Username/repeat input           | Normalize text                |
| `.strip()`  | Username/password               | Remove surrounding whitespace |
| `import`    | `import threading`              | Load module                   |
| `Timer()`   | `threading.Timer(...)`          | Delay function execution      |

---

# 🌍 Real-World Connection

This project is intentionally small, but the logic scales.

### Authentication

```text
Input
 ↓
Validate
 ↓
Check identity
 ↓
Make decision
 ↓
Allow / deny
```

### Data Engineering

```text
Input record
 ↓
Validate
 ↓
Check condition
 ↓
Transform
 ↓
Store
```

### Security Detection

```text
Log event
 ↓
Inspect data
 ↓
Check conditions
 ↓
Match detection rule
 ↓
Generate alert
```

The syntax may change.

The underlying thinking doesn't.

---

# 🐍 Day 7 Command & Syntax Cheat Sheet

| Syntax     | Purpose                       | Example                  |
| ---------- | ----------------------------- | ------------------------ |
| `if`       | Conditional decision          | `if status == "active":` |
| `elif`     | Additional condition          | `elif score >= 50:`      |
| `else`     | Fallback                      | `else:`                  |
| `==`       | Equality comparison           | `x == 10`                |
| `!=`       | Inequality comparison         | `x != 10`                |
| `>`        | Greater than                  | `x > 10`                 |
| `<`        | Less than                     | `x < 10`                 |
| `>=`       | Greater/equal                 | `x >= 10`                |
| `<=`       | Less/equal                    | `x <= 10`                |
| `and`      | Both true                     | `x > 0 and y > 0`        |
| `or`       | Either true                   | `admin or owner`         |
| `not`      | Reverse Boolean               | `not active`             |
| `for`      | Iterate                       | `for item in items:`     |
| `while`    | Repeat conditionally          | `while running:`         |
| `break`    | Exit loop                     | `if done: break`         |
| `continue` | Skip iteration                | `if invalid: continue`   |
| `pass`     | Placeholder                   | `if condition: pass`     |
| `range()`  | Number sequence               | `range(1, 6)`            |
| `match`    | Match value                   | `match status:`          |
| `case`     | Match option                  | `case "active":`         |
| `case _`   | Default case                  | `case _:`                |
| `in`       | Membership test               | `"admin" in users`       |
| `.lower()` | Lowercase text                | `username.lower()`       |
| `.strip()` | Remove surrounding whitespace | `name.strip()`           |

---

# 🌟 Skills Gained

By the end of Day 7, I should understand:

* 🧠 How Python makes decisions
* ⚖️ How comparisons work
* 🔗 How multiple conditions can be combined
* 🔁 How loops repeat work
* 🛑 How `break` stops loops
* ⏭️ How `continue` skips iterations
* 🎯 How `match / case` works
* 🧩 How nested control flow works
* 🛡️ How input can be validated
* 🔐 How control flow can model authentication logic
* 🐍 How Python code can begin interacting with security concepts

---

# 🔐 The Security Connection

Day 7 is where Python starts connecting directly with my cybersecurity path.

A simple:

```python
if
```

statement can eventually become part of:

```text
📜 Log Analysis
      ↓
🔍 Detection Logic
      ↓
🚨 Security Alert
```

A simple:

```python
for
```

loop can eventually process:

```text
10 logs
↓
10,000 logs
↓
10 million events
```

And a simple:

```python
while
```

loop can become part of an automation workflow.

Small syntax.

Big systems.

That's the game. 🐍☁️🔐

---

# ✅ Day 7 Completion Checklist

* [ ✅ ] Understand `if`
* [ ✅ ] Understand `elif`
* [ ✅ ] Understand `else`
* [ ✅ ] Understand comparison operators
* [ ✅ ] Understand Boolean values
* [ ✅ ] Understand `and`, `or`, and `not`
* [ ✅ ] Understand `for` loops
* [ ✅ ] Understand `while` loops
* [ ✅ ] Understand `break`
* [ ✅ ] Understand `continue`
* [ ✅ ] Understand `pass`
* [ ✅ ] Understand `range()`
* [ ✅ ] Understand `match / case`
* [ ✅ ] Understand nested conditions
* [ ✅ ] Understand input validation
* [ ✅ ] Build the Mini Login Validator
* [ ✅ ] Understand how control flow connects to authentication
* [ ✅ ] Understand how control flow connects to future security and data-engineering work

---

# 🚀 Day 7 Takeaway

Day 6 taught me the **building blocks of Python**.

Day 7 taught me how to **control those building blocks**.

```text
Variables
    ↓
Data
    ↓
Conditions
    ↓
Loops
    ↓
Functions
    ↓
Logic
    ↓
Automation
```

Python is no longer just executing instructions.

Now I'm telling it **how to think about what happens next.** 🧠🐍

**Learn → Build → Break → Debug → Understand → Improve → Commit.** 🚀
