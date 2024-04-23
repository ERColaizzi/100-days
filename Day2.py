""" bill calculator
bill
percent
total
split number
 """

print("Welcome to the tip calculator\n")
try:   #tries for valid input types, since defined as float/int
    bill = float(input("what is the total of the bill? $"))
    tip_percent = float(input("How much tip would you like to give? "))
    split_number = int(input("How many ways would you like to split the bill? "))
except:    #on error
    print("Sorry looks like you entered something incorrectly")

else:   #if no error continue here
    total_bill = bill * (1 + (tip_percent/100))
    per_person = total_bill/split_number
    print("Each person should pay: ${}".format(per_person))    
    
    



