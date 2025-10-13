units=int(input("enter the number of units you comsumed"))

if(units <50 ):
    amount=units *2.60
    surcharge=25
elif(units <=100):
    amount=130 +((units -50)*3.25)
    surcharge=35
elif(units <=200):
    amount=130+162.25((units -100) * 3.50)
    surcharge=45
else:
    amount=130+162.50((units -200)*8.45)
    surcharge=75
total=amount+surcharge
print("n/electricity bill= %.2f"%total)