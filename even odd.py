import random
even_num =[]
odd_num=[]
for x in range(1,30):
      
 x=random.randint(1,30)
 if x%2==0:
  
  even_num.append(x)
 else:
    odd_num.append(x)
even_num.sort()
odd_num.sort()    
print("this are even number",even_num)
print("this is odd number",odd_num)