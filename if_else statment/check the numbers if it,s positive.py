import random
num=[random.randint(-100,100) for _ in range(2)]
a,b=num[0],num[1]
sum=a+b
bolean=(a>0 and b>0)
print(a,b)
if bolean  :
    print("it,s both are positive ")
else:
    print("it,s that there are not both posivitve")        
if sum <100:  
    print("and less than hundered")  
elif sum>100:
    print("thier are not less than hundered ")    
