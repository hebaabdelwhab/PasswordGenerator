import string
import random

lowercase_Letters = list(string.ascii_lowercase)
uppercase_Letters = list(string.ascii_uppercase)
numbers = list(string.digits)
punctuation = list(string.punctuation)

characters_number = input('How many characters for the password?:')

while True:
    try:
        characters_number = int(characters_number)
        if characters_number<6:
            print('You need at least 6 characters')
            characters_number = input('How many characters for the password?:')
        else:
            break
    except:
        print('Please enter number only')
        characters_number = input('How many characters for the password?:')

random.shuffle(lowercase_Letters)
random.shuffle(uppercase_Letters)
random.shuffle(numbers)
random.shuffle(punctuation)

getNumOfFirstPart = round(characters_number * (30 / 100))
getNumOfSecondPart  = round(characters_number * (20 / 100))
password = []

for i in range(getNumOfFirstPart):
    password.append(lowercase_Letters[i])
    password.append(uppercase_Letters[i])
for i in range(getNumOfSecondPart):
    password.append(numbers[i])
    password.append(punctuation[i])

random.shuffle(password)
password = ''.join(password[0:])
print("Generated password is "+password)
