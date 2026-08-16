import random
num=[random.randint(1,100) for _ in range(4)]
print(num)
for i in  num:
 if i%7==0:
    print("hello")
 else:
   print("not hello")   
 if i.isendswith(7):
    print("hello")