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
        
        # VALIDATING IF THE REGIISTERED USER IS THE LOGGING IN
        def login_check():
            print("------ 🗂️ Let's Validate 🐝 ------")
            username = input("Enter username: ").strip().lower()
            password = input("Enter password: ").strip()

            #CHECK IF THE USERNAME EXISTS
            if username in USER_DATABASE:
                #CHECKING IF THE PASSWORD MATCHES
                if USER_DATABASE[username] == password:
                    print(f"----- ✅ Login successful! Welcome back {username}!")
                    return True
                else:
                    print(f"----- 🆘 ERROR: INCORRECT password.")
            else:
                print("----- ⛔️ ERROR: USERNAME NOT FOUND ⛔️ ------")
        
        #CLOSING THE LOOP
        login_again = input("====== ⛔️ Wanna check-in someone else? (yes/no): ").lower()
        if login_again != "yes":
            print("======== 🐧 THANK YOU, BYE 🆘 =======")


# CALLING THE TIMER FUNCTION
timer = threading.Timer(3, login_validator)
timer.start()