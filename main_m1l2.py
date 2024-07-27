import random

character = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
panjang_sandi = input("put any password: ")
password = ""

for i in range(int(panjang_sandi)):
    password += random.choice(character)

print(password)
