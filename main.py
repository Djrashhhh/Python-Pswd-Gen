import random

print('This is my password generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$^&*().,?0123456789'

number = input('Enter the number of passwords you want to generate: ')
number =int(number)

length = input('How long do you want your password to be:')
length = int(length)

print ('\nHere are your generated passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range (length):
        passwords += random.choice(chars)
        print(passwords)
