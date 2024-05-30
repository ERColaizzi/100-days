#looping
#
#password generatorz
#input length, numbers, special
# string lenth less inputs
#generate rand capitals 1-third/half
#rand insert numb,special
#

import random
import string
import pyperclip


def inp_len():
    while True:
        try:
            inp_len = int(input("How long of a password would you like?: "))    
            if inp_len >=10:
                break
            raise Exception()
        except:
            print("Enter a number greater than 10")
    return inp_len

def inp_num():
    while True:
        try:
            inp_num = int(input("How many numbers would you like?: "))    
            if inp_num >=2:
                break
            raise Exception()
        except:
            print("Enter a number greater than 2")
    return inp_num

def inp_char():
    while True:
        try:
            inp_char = int(input("How many special characters would you like?: "))    
            if inp_char >=2:
                break
            raise Exception()
        except:
            print("Enter a number greater than 2")
    return inp_char

##verify inputs


num_len = inp_len()
num_num = inp_num()
num_char = inp_char()

if num_num + num_char < num_len -4:
    length = num_len - num_char - num_num
else:
    print("your password length has been increased due to numbers and characters")
    length = num_num + num_char + 4

uppermax = length -2
num_upper = random.randint(2,uppermax)
num_lower = length - num_upper
start_str = ""



for i in range(num_num):
    start_str += random.choice(string.digits)

for i in range(num_char):
    start_str += random.choice(string.punctuation)

for i in range(num_upper):
    start_str += random.choice(string.ascii_uppercase)

for i in range(num_lower):
    start_str += random.choice(string.ascii_lowercase)


##i really hate that i have to go string to list to string
def string_shuffle(s):
    s2 = list(s)
    random.shuffle(s2)
    shuffled= "".join(s2)
    return shuffled


password = string_shuffle(start_str)
pyperclip.copy(password)

print("Your password is: ", password, " it has been copied to your clipboard")


