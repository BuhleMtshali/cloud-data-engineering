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
        
        #CLOSING THE LOOP
        runAgain = input("==== 💡 Wanna run the calculor again? (yes/no): ").lower()
        if runAgain != "yes":
            print("===== ⛳️ Thank you For Trying My Mini Calculator 🎲 =====")

# CALLING THE TIMER FUNCTION
timer = threading.Timer(2, calculator_app)
timer.start()