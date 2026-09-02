# 🐍💻 Day 006 — Python Basics

> **Phase 01: Tech Foundations**  
> **Topic:** Python Basics  
> **Outcome:** Understand Python fundamentals and use them to build small automation-style programs ⚙️🐍

---

## 🌱 Welcome to Day 6

Five days of Linux later and Python finally walks in like:

> “What if automation was readable?” 😭✨

Today is about the basic building blocks of Python:

```text
variables
+
data types
+
input
+
operators
+
conditions
+
loops
+
functions
+
modules
+
basic file handling
```

The goal is not to memorize every Python feature. The goal is to understand enough Python to start building useful programs and eventually use it for data engineering, cloud automation, log parsing, security tooling, ETL pipelines, API work, and scripting. 🐍🔥

---

# 🎯 Learning Objectives

By the end of Day 6, I should be able to:

- 🧠 Understand basic Python syntax
- 📦 Create variables
- 🔢 Work with strings, integers, floats, booleans, and `None`
- 📥 Accept user input
- 🔄 Convert input into numbers
- 🧮 Use arithmetic and comparison operators
- 🚦 Write `if / elif / else` logic
- 🔁 Create `for` and `while` loops
- 📚 Work with lists and dictionaries
- 🧱 Create functions
- 📤 Return values from functions
- ✨ Use f-strings
- 📦 Import Python modules
- 🚨 Handle simple exceptions
- 📁 Read and write files
- 🐧 Access Linux environment information from Python
- 🧪 Build two small Python mini projects

---

# 🧠 Python Mental Model

```text
GET DATA
   ↓
STORE DATA
   ↓
PROCESS DATA
   ↓
MAKE DECISIONS
   ↓
REPEAT IF NEEDED
   ↓
RETURN / DISPLAY RESULT
```

That translates nicely into:

```text
input
↓
variables
↓
operators
↓
conditions
↓
loops
↓
functions
↓
output
```

---

# 🧰 Python Basics Master Table

| Concept / Syntax | What It Does | Example | What It Means |
|---|---|---|---|
| `print()` | Displays output | `print("Hello Buhle")` | Print text to terminal |
| `#` | Creates a comment | `# Welcome message` | Python ignores the comment |
| variable | Stores a value | `name = "Buhle"` | Save a value under a name |
| `=` | Assignment operator | `age = 25` | Store value in variable |
| `str` | Text type | `name = "Buhle"` | String |
| `int` | Whole number | `servers = 5` | Integer |
| `float` | Decimal number | `price = 4.5` | Floating point |
| `bool` | True/false value | `active = True` | Boolean |
| `None` | No value | `result = None` | Empty/no result yet |
| `type()` | Shows data type | `type(name)` | Returns type information |
| `input()` | Gets keyboard input | `input("Name: ")` | Waits for user input |
| `int()` | Converts to integer | `int("25")` | `"25"` → `25` |
| `float()` | Converts to float | `float("2.5")` | `"2.5"` → `2.5` |
| `str()` | Converts to string | `str(25)` | `25` → `"25"` |
| `+` | Addition / concatenation | `10 + 5` | `15` |
| `-` | Subtraction | `10 - 5` | `5` |
| `*` | Multiplication | `10 * 2` | `20` |
| `/` | Division | `10 / 2` | `5.0` |
| `//` | Floor division | `10 // 3` | `3` |
| `%` | Remainder | `10 % 3` | `1` |
| `**` | Power | `2 ** 3` | `8` |
| `==` | Equal comparison | `age == 25` | Is it equal? |
| `!=` | Not equal | `age != 18` | Is it different? |
| `>` | Greater than | `age > 18` | Comparison |
| `<` | Less than | `age < 30` | Comparison |
| `>=` | Greater/equal | `age >= 18` | Comparison |
| `<=` | Less/equal | `age <= 65` | Comparison |
| `and` | Both conditions true | `age >= 18 and active` | Logical AND |
| `or` | At least one true | `admin or owner` | Logical OR |
| `not` | Reverses boolean | `not active` | `True` → `False` |
| `if` | Starts conditional | `if age >= 18:` | Run if true |
| `elif` | Checks another condition | `elif age >= 13:` | Else-if |
| `else` | Fallback | `else:` | Runs if others fail |
| indentation | Defines code block | `    print("Yes")` | Python uses indentation |
| `match` | Pattern matching | `match operator:` | Compare one value against cases |
| `case` | Handles a match option | `case "+":` | Run for matching value |
| `case _` | Default match case | `case _:` | Runs if nothing else matches |
| `list` | Ordered collection | `tools = ["Git", "Python"]` | Multiple values |
| `.append()` | Adds to list | `tools.append("AWS")` | Add item |
| `.remove()` | Removes item | `tools.remove("Git")` | Remove matching item |
| `len()` | Counts items | `len(tools)` | Number of items |
| `dict` | Key/value collection | `{"name":"Buhle"}` | Labelled data |
| `.get()` | Gets dictionary value | `user.get("name")` | Safe key lookup |
| `for` | Loops through items | `for tool in tools:` | Repeat per item |
| `while` | Repeats while true | `while True:` | Keep looping |
| `break` | Stops a loop | `break` | Exit loop |
| `continue` | Skips iteration | `continue` | Go to next loop cycle |
| `def` | Defines function | `def calculator_app():` | Create reusable code block |
| `return` | Sends result back | `return output` | Return function result |
| `f"..."` | Formatted string | `f"Hello {name}"` | Insert variables into text |
| `import` | Loads module | `import os` | Use external functionality |
| `os.getenv()` | Reads environment variable | `os.getenv("HOME")` | Get Linux environment value |
| `os.getcwd()` | Gets current working directory | `os.getcwd()` | Python version of `pwd` |
| `try` | Starts error-handling block | `try:` | Attempt risky code |
| `except` | Handles error | `except ValueError:` | Catch exception |
| `with open()` | Opens file safely | `with open("file.txt") as file:` | Automatically closes file |
| `.read()` | Reads file contents | `file.read()` | Read text |
| `.write()` | Writes to file | `file.write("Hello")` | Write text |
| `.lower()` | Converts text to lowercase | `"YES".lower()` | Returns `"yes"` |
| `threading.Timer()` | Runs a function after a delay | `threading.Timer(2, func)` | Wait, then call function |

---

# 📦 Variables & Data Types

```python
name = "Buhle"
age = 25
storage = 2.5
active = True
```

| Type | Used For | Example |
|---|---|---|
| `str` | Text | `"AWS"` |
| `int` | Whole numbers | `10` |
| `float` | Decimals | `10.5` |
| `bool` | True/false | `True` |
| `list` | Ordered collection | `["Linux", "Git"]` |
| `tuple` | Fixed ordered collection | `(22, 80, 443)` |
| `dict` | Key/value pairs | `{"status":"running"}` |
| `set` | Unique values | `{22, 80, 443}` |
| `None` | No value | `None` |

---

# 📥 User Input

```python
name = input("What is your name? ")
age = int(input("Age: "))
price = float(input("Price: "))
```

Important:

```text
input() returns a string by default
```

---

# 🚦 Conditions

```python
age = 25

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Python uses indentation to define code blocks. Whitespace has authority here 😭

---

# 🎯 `match / case`

```python
operator = "+"

match operator:
    case "+":
        print("Addition")
    case "-":
        print("Subtraction")
    case _:
        print("Unknown operator")
```

This became useful in today's calculator project. 🧮🔥

---

# 🔁 Loops

## `while`

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

## `for`

```python
tools = ["Linux", "Git", "Python"]

for tool in tools:
    print(tool)
```

---

# 🧱 Functions

```python
def greet(name):
    print(f"Hello {name}")

greet("Buhle")
```

Functions package reusable logic.

---

# 📤 `return`

```python
def calculate_total(a, b):
    total = a + b
    return total
```

---

# ✨ F-Strings

```python
output = 50
print(f"Output: {output}")
```

Cleaner than stitching strings together manually. 😌

---

# 📦 Modules

Today's projects used:

```python
import os
import threading
```

| Module | Why It Matters |
|---|---|
| `os` | Interact with operating-system information |
| `threading` | Work with threads and timers |

---

# 🐧 `os` Module

| Code | What It Does |
|---|---|
| `os.getenv("USER")` | Gets current Linux username |
| `os.getenv("HOME")` | Gets home directory |
| `os.getcwd()` | Gets current working directory |
| `os.listdir()` | Lists directory contents |
| `os.path.exists()` | Checks if path exists |

---

# ⏱️ `threading.Timer`

Today's calculator used:

```python
timer = threading.Timer(2, calculator_app)
timer.start()
```

Meaning:

```text
wait 2 seconds
↓
call calculator_app()
```

---

# 🚨 Error Handling Basics

```python
try:
    number = float(input("Enter number: "))
except ValueError:
    print("Please enter a valid number.")
```

This is how interactive programs stop falling dramatically down the stairs when input is wrong 😭

---

# 📁 File Handling Basics

Read:

```python
with open("notes.txt", "r") as file:
    content = file.read()
```

Write:

```python
with open("notes.txt", "w") as file:
    file.write("Python Day 6")
```

Append:

```python
with open("notes.txt", "a") as file:
    file.write("\nLearning Python")
```

---

# 🧪 Mini Project 1 — Mini Calculator 🧾🧺

Today's first project is an interactive calculator.

It practises:

```text
functions
+
while loops
+
user input
+
floats
+
match/case
+
conditions
+
f-strings
+
modules
```

## 💻 Code

```python
# IMPORTING TIMER
import threading

# WELCOME MESSAGE
print("=========== 🧾 MINI CALCULATOR 🧺 ===========")

# CREATING THE FUNCTION
def calculator_app():

    # STARTING THE WHILE LOOP
    while True:

        first_number = float(input("🧺 Enter your first number: "))
        operator = input("🧩 Choose an operator (+, /, *, -): ")
        second_number = float(input("🧺 Enter your second number: "))

        output = 0

        match operator:
            case "+":
                output = first_number + second_number
                print(f"Output: {output}")

            case "-":
                output = first_number - second_number
                print(f"Output: {output}")

            case "*":
                output = first_number * second_number
                print(f"Output: {output}")

            case "/":
                if second_number == 0:
                    print("🚫 Cannot divide by 0")
                else:
                    output = first_number / second_number
                    print(f"Output: {output}")

            case _:
                print("‼️ Invalid Operators")

        # CLOSING THE LOOP
        runAgain = input(
            "==== 💡 Wanna run the calculator again? (yes/no): "
        ).lower()

        if runAgain != "yes":
            print("===== ⛳️ Thank you For Trying My Mini Calculator 🎲 =====")
            break

# CALLING THE TIMER FUNCTION
timer = threading.Timer(2, calculator_app)
timer.start()
```

> 💡 I added the `break` after the goodbye message so the loop actually ends when the user says anything other than `yes`.

---

# 🧠 What This Calculator Practises

| Concept | Where It Appears |
|---|---|
| `import` | `import threading` |
| Function | `def calculator_app():` |
| Infinite loop | `while True:` |
| Input | `input(...)` |
| Type conversion | `float(input(...))` |
| Variables | `first_number`, `output`, etc. |
| Pattern matching | `match operator:` |
| Cases | `case "+"`, `case "-"`, etc. |
| Condition | `if second_number == 0:` |
| F-string | `f"Output: {output}"` |
| String method | `.lower()` |
| Loop control | `break` |
| Timer | `threading.Timer(2, calculator_app)` |

---

# 🔐 Division-by-Zero Check

```python
if second_number == 0:
    print("🚫 Cannot divide by 0")
```

This prevents a `ZeroDivisionError` before it happens.

That is already basic defensive programming. 👀🐍

---

# 🧪 Mini Project 2 — Linux System Snapshot 🐧🖥️

This project connects Python directly to the Linux foundation from the earlier days.

## 💻 Code

```python
import os

print("===== 🐧 SYSTEM SNAPSHOT =====")

user = os.getenv("USER")
home = os.getenv("HOME")
current_directory = os.getcwd()

print(f"🙋🏻‍♀️ User: {user}")
print(f"🏡 Home: {home}")
print(f"🗂️ Current Directory: {current_directory}")
```

---

# 🧠 What This Project Practises

| Concept | Where It Appears |
|---|---|
| Module import | `import os` |
| Environment variable | `os.getenv("USER")` |
| Environment variable | `os.getenv("HOME")` |
| Working directory | `os.getcwd()` |
| Variables | `user`, `home`, `current_directory` |
| F-strings | `f"🙋🏻‍♀️ User: {user}"` |
| Linux + Python | Reading OS-level information |

---

# 🐧 Bash vs Python Connection

Yesterday in Linux/Bash:

```bash
whoami
echo "$HOME"
pwd
```

Today in Python:

```python
os.getenv("USER")
os.getenv("HOME")
os.getcwd()
```

Same environment. Different language. 🔥

---

# ⚠️ Common Python Beginner Mistakes

| Mistake | What Happens |
|---|---|
| Forgetting `:` | `SyntaxError` |
| Bad indentation | Python cannot understand the block |
| Mixing `=` and `==` | Assignment vs comparison confusion |
| Forgetting `input()` returns string | Maths can fail |
| Invalid numeric input | `ValueError` |
| Dividing by zero | `ZeroDivisionError` |
| Misspelling variable | `NameError` |
| Wrong capitalization | Variables are case-sensitive |
| Infinite `while True` without exit | Program never ends 😭 |
| Forgetting to call a function | Function exists but never runs |
| Forgetting `break` when needed | Loop keeps going |
| Wrong dictionary key | `KeyError` |

---

# 🌍 Why Python Matters for Cloud Data Engineering

Python shows up in:

- 📊 data processing
- 🚰 ETL pipelines
- 🧹 data cleaning
- 🗃️ database workflows
- ☁️ cloud automation
- 📦 AWS Lambda
- 🌐 APIs
- 📜 log parsing
- 🔐 security automation
- ⚙️ infrastructure tooling
- 🔥 Spark
- 🧠 machine learning

Future code starts looking like:

```python
data = extract()
clean_data = transform(data)
load(clean_data)
```

Which becomes:

```text
EXTRACT
↓
TRANSFORM
↓
LOAD
```

Hello, data engineering 👀📊

---

# 🎯 Day 6 Syntax to Burn Into Memory

```python
print()

variable = value

input()

int()
float()
str()

if
elif
else

match
case

for
while
break

list
dict

def
return

import

try
except

with open()

f"{variable}"
```

Core mental model:

```text
DATA
 ↓
VARIABLES
 ↓
LOGIC
 ↓
LOOPS
 ↓
FUNCTIONS
 ↓
AUTOMATION
```

---

# ✅ Day 6 Completion Checklist

- [ ] I understand Python variables
- [ ] I understand basic data types
- [ ] I can use `input()`
- [ ] I can convert input using `int()` and `float()`
- [ ] I understand arithmetic operators
- [ ] I understand comparison operators
- [ ] I can write `if / elif / else`
- [ ] I understand indentation
- [ ] I understand `match / case`
- [ ] I understand `while` loops
- [ ] I understand `for` loops
- [ ] I understand `break`
- [ ] I can work with lists
- [ ] I understand dictionaries
- [ ] I can create functions
- [ ] I understand parameters and arguments
- [ ] I understand `return`
- [ ] I can use f-strings
- [ ] I understand modules
- [ ] I can use basic `os` module functions
- [ ] I understand basic exception handling
- [ ] I understand simple file handling
- [ ] I built the Mini Calculator
- [ ] I built the Linux System Snapshot
- [ ] Python syntax is starting to feel less like code soup 🐍😌

---

# 📚 Useful Reference Commands

Run Python:

```bash
python3 script.py
```

Check Python version:

```bash
python3 --version
```

Interactive Python:

```bash
python3
```

Built-in help:

```python
help()
help(print)
help(str)
help(list)
help(dict)
```

---

# 🔜 Next Step

Day 1 taught me how to navigate Linux.

Day 2 taught me Linux permissions and ownership.

Day 3 taught me processes and services.

Day 4 taught me Bash automation.

Day 5 taught me version control.

Day 6 introduces the language that will help glue a huge amount of this roadmap together.

```text
Linux
+
Git
+
Bash
+
Python
```

Now the engineering toolbox is starting to look serious. 🧰🐍☁️🔥

**Learn → Build → Run → Debug → Improve → Commit → Repeat.**
