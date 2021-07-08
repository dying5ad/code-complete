import random
#all characters involved#
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!"£$%^&*():@;?><,./\|'
#number of passwords#
number = input('number of passwords you want? -  ')
number = int(number)

length = input('password length?  -  ')
length = int(length)

for p in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
