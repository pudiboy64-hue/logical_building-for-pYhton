import random
# x= 20
# y=3
# print(x%3)
i=random.randint(1,100)
print(i)
if i%5==0 and  i%3==0:
   print("FuzzBuzz")  
elif i%5==0 :
   print("BUzz")
elif i%3==0:
   print("Fuzz")   