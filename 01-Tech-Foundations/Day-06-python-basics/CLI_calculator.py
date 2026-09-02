# IMPORTING TIMER
import threading

# WELCOME MESSAGE
print("=========== 🧾 MINI CALCULATOR 🧺 ===========")

# CREATING THE FUNCTION
def calculator_app():
    
    #STARTING THE WHILE LOOP
    while True:
        print("loop running")
        
        
        
    #CLOSING THE LOOP
    runAgain = input("==== 💡 Wanna run the calculor again? (yes/no): ").lower()
    if runAgain != "yes":
        print("===== ⛳️ Thank you For Trying My Mini Calculator 🎲 =====")

# CALLING THE TIMER FUNCTION
timer = threading.Timer(2, calculator_app)
timer.start()