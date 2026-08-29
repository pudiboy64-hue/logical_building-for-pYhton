import random
x=random.randint(100,1000)
print(x)
x_str=str(x)
min=x_str[0]
lar=x_str[0]
for i in x_str:
    if i>min:
        min=i
        print(min)
    if i<lar:
        lar=i
        print(lar)
