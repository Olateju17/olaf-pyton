print("Enter marks obtained in 5 subjects")
mark1=int(input())
mark2=int(input())
mark3=int(input())
mark4=int(input())
mark5=int(input())

tot = mark1+mark2+mark3+mark4+mark5
avg=tot/5
if avg>=91 and avg <=100:
 print("grade A")
elif avg>70 and avg<=90:
  print("grade b")
elif avg>60 and avg<=69:
  print("grade c")




