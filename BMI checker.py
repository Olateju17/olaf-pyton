height=float(input("enter your height in cm"))
weight=float(input("enter your weight in kg"))

BMI= weight / (height/100)**2
print("Your BMI is",BMI)

if BMI <= 18.4:
    print("You are underweight")
if BMI <= 24.7:
    print("You are healthy")
elif BMI <= 29.9:
    print("You are overweight")
elif BMI <= 34.9:
    print("You are severly overweight")
elif BMI <= 39.9:
    print("You are obese")
else:
    print("you are severly obese")
