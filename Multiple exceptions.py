try:
    num1,num2=eval(input("enter 2 num" 
    "seperated by a comma:"))
    result = num1 /num2
    print("Reslt is ",result)    
except ZeroDivisionError:
    print("Division by zero is error!!")
except SyntaxError:
    print("comma is missing, Enter numbers seperatedby comma like this 1,2")
except:
    print("Wrong input")
else:
    print("No excepttion")
finally:
    print("This will excecute no matter what")
