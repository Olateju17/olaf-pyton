age_input = input("Enter your age: ")

if age_input.isdigit():  
    age = int(age_input)
    if age % 2 == 0:
        print("The age entered is even.")
    else:
        print("The age entered is odd.")
else:
    print("Value Error: Invalid age entered!")
