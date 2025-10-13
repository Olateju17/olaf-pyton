medical_cause=input("Did you have medical cause Y or N")
atten=int(input("enter the attendance of the students"))
if medical_cause == 'Y': 
    print("You are allowed")
else:
    if atten>=75:
        print("Allowed")
    else:
        print("not allowed")