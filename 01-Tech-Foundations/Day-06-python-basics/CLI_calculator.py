# IMPORTING TIMER
import threading

# WELCOME MESSAGE
print("=========== 🧾 MINI CALCULATOR 🧺 ===========")

# CREATING THE FUNCTION
def calculator_app():
    
    #STARTING THE WHILE LOOP
    while True:
        first_number = float(input("🧺 Enter your first number: "))
        operator = input("🧩 Choose an operator (+, /, *, -): ")
        second_number = float(input("🧺 Enter your second number: "))
        
        
        
    #CLOSING THE LOOP
    runAgain = input("==== 💡 Wanna run the calculor again? (yes/no): ").lower()
    if runAgain != "yes":
        print("===== ⛳️ Thank you For Trying My Mini Calculator 🎲 =====")

# CALLING THE TIMER FUNCTION
timer = threading.Timer(2, calculator_app)
timer.start()