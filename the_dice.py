import random


print("HELLO AND WELCOME TO THE UNBIASED DICE :")
print("DO YOU WISH TO ROLL THE DICE?[y/n]")
b = input()
if b == 'y':
    a = random.randint(1,6)
    print("YOU GOT A ",a)
if b == 'n':
    print("OKAY THEN ......")


