import random
check=[random.randint(1,30) for _ in range(2)]
a,b=check[0],check[1]

if a %2==0 and b%2==0:
        print("both number are even ")
elif a%2!=0 and b%2!=0:
        print("both number are odd ")

# Check variable a
if a % 2 == 0:
    a = "even"
else:
    a = "odd"

# Check variable b
if b % 2 == 0:
    b = "even"
else:
    b = "odd"


