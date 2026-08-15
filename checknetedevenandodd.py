import random
check=[random.randint(1,30) for _ in range(2)]
a,b=check[0],check[1]

if a %2==0 and b%2==0:
        print("both number are even ")
elif a%2!=0 and b%2!=0:
        print("both number are odd ")
if a%2==0 or b%2==0:
        print("one nnumber is even number other is odd")    
