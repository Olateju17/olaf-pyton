def swap_three_values():
    # Input values
    a = input("Enter first value (a): ")
    b = input("Enter second value (b): ")
    c = input("Enter third value (c): ")
    
    print(f"\nBefore swapping:\na = {a}, b = {b}, c = {c}")
    
    # Swap logic (example: rotating values)
    a, b, c = c, a, b  # You can change this logic as needed
    
    print(f"\nAfter swapping:\na = {a}, b = {b}, c = {c}")

# Run the function
swap_three_values()