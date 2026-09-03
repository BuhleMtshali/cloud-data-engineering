# IMPORTING THE TIMER FUNCTION

import threading

# WELCOME MESSAGE
print("================ 🤳🏽 MINI LOGIN VALIDATOR ⛔️ =================")

# STARTING FUNCTION
def login_validator():
    
     # STARTING WHILE LOOP
    while True:
        
        
        #CLOSING THE LOOP
        login_again = input("====== ⛔️ Wanna check-in someone else? (yes/no): ")
        if login_again != "yes":
            print("======== 🐧 THANK YOU, BYE 🆘 =======")


# CALLING THE TIMER FUNCTION
timer = threading.Timer(3, login_validator)
timer.start()