import random

Alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', ':', ';', '"', "'", '|', '/', '?', '>', '<', '.', ',', '~']

password = []

no_pass_chars = int(input("Enter the number of characters you want in your password: "))

no_pass_letters = int(input("Enter the number of letters: "))
no_pass_spcl_chars = int(input("Enter the number of special characters: "))
no_pass_numbers = no_pass_chars - (no_pass_letters + no_pass_spcl_chars)

i = 0
j = 0
k = 0

while i < no_pass_letters:
    password.append(random.choice(Alphabets))
    i+=1
while j < no_pass_spcl_chars:
    password.append(random.choice(special_characters))
    j+=1
while k < no_pass_numbers:
    password.append(random.choice(numbers))
    k+=1

random.shuffle(password)

password_final = ""

for x in password:
    password_final += x

print(password_final)
