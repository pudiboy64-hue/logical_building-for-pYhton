import random
num=[]
for x in range(3):
    x=random.randint(0,20)
    num.append(x)
print("list ",num)
max=num[0]
for i in num:
    if i > max:
        max=i
print("the greatest is number between random choice iss ",max)