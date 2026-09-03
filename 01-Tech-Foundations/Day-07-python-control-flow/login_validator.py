# IMPORTING THE TIMER FUNCTION

import threading

# WELCOME MESSAGE
print("================ 🤳🏽 MINI LOGIN VALIDATOR ⛔️ =================")

# STARTING FUNCTION
def login_validator():
    
    #SIMULATED USER DATABASE
    USER_DATABASE = {
        "admin": "Secrete123!",
        "alice": "Wonderland99",
        "bob": "Builder456"
    }
    
     # STARTING WHILE LOOP
    while True:
        
        
        #CLOSING THE LOOP
        login_again = input("====== ⛔️ Wanna check-in someone else? (yes/no): ")
        if login_again != "yes":
            print("======== 🐧 THANK YOU, BYE 🆘 =======")


# CALLING THE TIMER FUNCTION
timer = threading.Timer(3, login_validator)
timer.start()