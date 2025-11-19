try: 
    number =int(input("Enter a num:"))
    print("The number entered is",number)
except ValueError as ex:
    print("Exception:",ex)
 