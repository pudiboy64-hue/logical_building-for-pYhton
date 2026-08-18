import random
sides =[random.randint(1,10) for _ in range(3)]
sides.sort()
a,b,c=sides[0],sides[1],sides[2]
print(a,b,c)
if a+b >c:
    if a**2 +b**2==c**2:
     print("its the right sides reiangle")
    else:
       print("it,s the simple triangle") 
else:
   print("invalid sides")

