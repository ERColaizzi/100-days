""" 
random
coin flip n times
overwrite each time

 """

import random
import time

def coin_flip(n):
    heads = 0
    tails = 0
    for i in range(n+1):
        x=random.randint(0,1)
        if x == 0:
            heads+=1
        else:
            tails+=1
        print(f"\rHeads: {heads}   Tails: {tails}", end="")

print("Welcome to the coin flip simulator!")
times = input("Please select a large number to sample: ")
coin_flip(int(times)) 

