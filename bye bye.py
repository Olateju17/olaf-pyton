valid=False 
while not valid:
    try:
        n=int(input("eter a num"))
        if n%2==0:
            print("bye bye ")
            valid=True
    except ValueError:
        print("in valid")