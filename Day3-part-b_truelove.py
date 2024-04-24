""" 
true love test
loop true
loop love
 """

word1 = "true"
word2 = "love"
fname1 = input("Enter the first persons name: ").lower()
fname2 = input("Enter the second persons name: ").lower()

def tl_count(n1,n2,w1,w2):
    count1 =0
    count2 =0
    
    for l in w1:
        count1 += n1.count(l)
        count1 += n2.count(l)
    for l in w2:
        count2 += n1.count(l)
        count2 += n2.count(l)
        
    count =  str(count1)+str(count2)
    return(count)

score = int(tl_count(fname1,fname2,word1,word2))

if score <10 or score>90 :
    print("Your score is {}, you go together like milk and chocolate".format(score))
elif score>=40 and score <= 50:
    print("Your score is {}, you are fine".format(score))
else:
    print("Your score is {}".format(score))
