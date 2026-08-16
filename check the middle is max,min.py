import random
num=[random.randint(1,9) for _ in range(5)]
mid=len(num)//2
print(num[mid])
print(num)

if num[mid]==max(num):
        print("the middle man is largest")
elif num[mid]==min(num):
        print("the middle man is smallest")    
else:
        print("the middle iss somewhere")        