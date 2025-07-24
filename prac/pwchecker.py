# import random

# print("Password Checker")

# length = int(input("Enter password length: "))
# alphalen = int(input("Enter number of alphabets: "))
# numlen = int(input("Enter number of numbers: "))
# symlen = int(input("Enter number of symbols: "))

# # Define possible characters
# lowerAlphabets = "abcdefghijklmnopqrstuvwxyz"
# upperAlphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# numbers = "0123456789"
# symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?/~`"
# password = []

# def generate_password(length, alphalen, numlen, symlen):
#     if length < (alphalen + numlen + symlen):
#         print("Length is too short for the specified character counts.")
#         return None

    
#     for _ in range(alphalen):
#         password.append(random.choice(lowerAlphabets))
    
#     for _ in range(alphalen):  # This should be 'for _ in range(upperAlphabets)' or use the specified number
#         password.append(random.choice(upperAlphabets))
    
#     for _ in range(numlen):
#         password.append(random.choice(numbers))
    
#     for _ in range(symlen):
#         password.append(random.choice(symbols))
    
#     while len(password) < length:
#         password.append(random.choice(lowerAlphabets + upperAlphabets + numbers + symbols))
    
#     random.shuffle(password)
    
#     print("Generated Password: " + ''.join(password))

# generate_password(length, alphalen, numlen, symlen)

username = input("username : ")
password = input("password : ")
print(f"username is {username} and password is {'*'*(len(password)-2)+password[-2:]} ") 