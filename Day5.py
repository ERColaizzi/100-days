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
            if inp_len >=2:
                break
            raise Exception()
        except:
            print("Enter a number greater than 2")
    return inp_num

def inp_char():
    while True:
        try:
            inp_char = int(input("How many special characters would you like?: "))    
            if inp_len >=2:
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

uppermax = num_len - num_char - num_num -2
num_upper = random.randint(2,uppermax) 
start_str = {}




##string.ascii_letters
#acii.lower + ascii.upper
##string.ascii_digits
##string.punctuation



#create string of length
#add upper, num, spec
#then shuffle
#or 
#Create len
#random insert into
#upper, num, spec










