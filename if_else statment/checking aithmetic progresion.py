# import random
# num=[random.randint(2,30) for _ in range(3)]

# num=[1,4,7,9,11,15,20]


# if num[5]-num[6]==d:
#     print("it,s arithmetic progression")
# else:
#     print("its it no arithmectic progresssion") 
num=[2,4,6,8,10,12,14]
# d=num[1]-num[0]   
# is_app=True
# for i in range(len(num)-1):
#     if num[i+1]-num[i]!=d:
#      is_app=False
#      break
# print(f"the number {num} are {is_app}")
# num=[2,4,8,16,32,64,128]
d=num[1]//num[0]   
is_app=True
for i in range(len(num)-1):
    if num[i+1]//num[i]!=d:
     is_app=False
     break
print(f"the number {num} are {is_app} in goemretics progression")