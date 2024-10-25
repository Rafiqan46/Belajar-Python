import random

print('Welcome To Your Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(),.0123456789'

number = int(input('Amount of password to generate: '))
lenght = int(input('Your password Length: '))

print('\n==here are your password==')

for pwd in range(number):
    passwords = ''
    for c in range(lenght):
        passwords += random.choice(chars)
    print(passwords)