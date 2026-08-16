import random
num=[random.randint(1,100) for _ in range(4)]
print(num)
for i in  num:
 if i%7==0:
    print("interger is multiple by seven")
 else:
   print("interger is not multliple by seven")   
 if int(str(i)[-1])==7:
   print("helllo")
 else:
   print("not helllo")  