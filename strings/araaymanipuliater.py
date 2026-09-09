# n=int(input("enter the number of elemnet inthe arrays for squares "))
# a=[x**2 for x in range(n)]
# print(a)
# n = int(input("Enter the number of elements: "))
a=[-1,-2,-30,1,2,3]
b=[0 if x<0 else x for x in a]
print(b)