def add(P ,Q):
    return P + Q

def substract(p,q):
    return p-q
def multplicaton (p,q):
    return p*q
def division(p,q):
    return p/q

print ("Please select the operation. ")
num_1 = int(input("enter first number"))
num_2 = int(input("enter 2nd number"))
print(add(num_1, num_2))
print(substract(num_1, num_2))
print(multplicaton(num_1, num_2))
print(division(num_1, num_2))