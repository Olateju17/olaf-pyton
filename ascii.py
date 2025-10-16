def show_ascii_code():
    char = input("Enter a single alphabet character: ")
    
    if len(char) == 1 and char.isalpha():
        ascii_value = ord(char)
        print(f"The ASCII code of '{char}' is {ascii_value}.")
    else:
        print("Please enter only a single alphabet character (A-Z or a-z).")


show_ascii_code()