import random
playing=True
number=str(random.randint(10,15))

print("I will generate a number from 10 to 15,and you have to guess the number 1 digit at a time ")
print("The game ends when you get 1 hero")
while playing:
    guess=input("Give your best guess! \n")
    if number ==guess:
        print("You wi the game ")
        print("Theumber was",number)
        break

else:
    print("Your guess is not right,try again. \n")