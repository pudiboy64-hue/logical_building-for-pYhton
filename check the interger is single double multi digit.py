import random
num=[random.randint(1,1023) for _ in range(10)]
print("started the list",num)
# print(len(str(num[0])))for 
for i in num:
    if len(str(i))==1:
        print(f"{i}  single digit interger number")
    elif len(str(i))==2:
        print(f"{i}  double digit interger number")
    else:
        print(f"{i}  multil digit interger number")        