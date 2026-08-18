import random
num=[random.randint(1,9) for _ in range(4)]
print(num)
if num[0]==num[len(num)-1]:
    print("the number are equal ")
else:
    print("the first and last are not equal")    
