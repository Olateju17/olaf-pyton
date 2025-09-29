cp=float(input("pls enter the cp "))
sp=float(input("pls enter the sp "))     
if(sp>cp):
   amount=sp-cp
   print("Total profit ={0}",format (amount))
else:
   print("no profit!!!")
   amount=cp-sp
   print("your loss amount",amount)