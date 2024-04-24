""" 
python treasure hunt
draw ascii image
pick your path

I stole the chest
 """
 
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

retry = True #needed for retry loop

while retry:
    while True: #general pick a path loop
        print("You are at a fork in the road. Do you go left or right?: ")
        choice1=input()
        if choice1.lower() == "left":
            print("You come to a river. Do you WAIT for a boat or SWIM across the river?: ")
            choice2=input()
            if choice2.lower() == "wait":
                print("You make it across the river safely. In front of you is a house with 3 doors.")
                print("Do you choose the RED door, the BLUE door, or the YELLOW door?")
                choice3 = input()
                if choice3.lower() == "red":
                    print("You get trapped in the house and die in a fire")
                    break
                elif choice3.lower() == "yellow":
                    print("Congratulations!!! You have found the treasure!")
                    retry = False #breaks overarching retry loop
                    break
                else:
                    print("You enter the door and a Troll eats you.")
                    break
            else:
                print("You get dissentary and die")
                break    
        else:
            print("You fall into a hole and die")
            break
    if retry == True: #checks for repeat
        choice_retry = input("Would you like to try again?")
        if choice_retry.lower() in {"no","n","x"}:
            break
        else:
            continue
    else: #retry broken on finish
        break    