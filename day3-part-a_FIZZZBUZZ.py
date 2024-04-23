#fizz buzz in python
# modolu with elif


def fb(num):
    for i in range (1,num+1):
        word = ""
        if i % 3 ==0:
            word += "fizz"
        if i % 5 ==0:
            word += "buzz"
        if i % 6 ==0:
            word += "bam"
        print(word or i)

fb(50)

    
"""     
c = "sds"
c+= "kok"
print(c)

 """