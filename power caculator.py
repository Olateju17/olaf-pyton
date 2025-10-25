
number = int(input("Enter a number: "))
n = int(input("Enter how many powers you want to calculate: "))

print(f"\nPowers of {number} up to {n} are:")
for i in range(1, n + 1):
    power_value = number ** i
    print(f"{number}^{i} = {power_value}")
