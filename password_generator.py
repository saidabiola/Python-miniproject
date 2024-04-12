import string
import random

name = input("Enter your name: ")
print(f"Hello {name} welcome to trusted password generator")


#Bunch of characters to generate from

char = string.ascii_letters + string.digits + string.punctuation

number_of_pswds = int(input("Enter the number of passwords you wish to generate: "))
passsword_length = int(input("Enter the length of password you want: "))


print("\nHere are your passwords...")


for i in range(number_of_pswds):
    pswd = ''
    for n in range(passsword_length):
        pswd += random.choice(char)
    
    print(pswd)