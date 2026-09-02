import os

print("===== 🐧 SYSTEM SNAPSHOT =====")

user = os.getenv("USER")
home = os.getenv("HOME")
current_directory = os.getcwd()

print(f"🙋🏻‍♀️ User: {user}")
print(f"🏡 Home: {home}")
print(f"🗂️ Current Directory: {current_directory}")