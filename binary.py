decimal = float(input("Enter a decimal number: "))
binary = bin(int(decimal)).replace("0b", "")
print(f"The binary equivalent of {decimal} is {binary}")