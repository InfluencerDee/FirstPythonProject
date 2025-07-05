#program to generate a password
import random
import string
char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
passwordlength = 7
password = ""

for i in range(passwordlength):
    password += random.choice(char)

print("your password is : ", password)

all_keys = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]
print(all_keys)
