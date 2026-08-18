import random
num=[]
for x in range(10):
 x=random.randint(0,50)
 num.append(x)
num.sort()
print("before list",num)
for i in num:
 if i==0:
   print(f"{i} is skipped")
 if i%5==0 and  i%3==0:
   print(f"the number  {i} is divisible by three and five")  
 elif i%5==0 :
    print(f"the random {i} nuber is divisble by five")
 elif i %3==0:
   print(f"the number {i} is divissible by three")   
 else:
    print(f"the number{i} is not divisble by five or three")    
num.sort()
print("final list",num)