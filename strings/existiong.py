a=[1,2,3,4,5,6,7]
b=int(input("enter the number :"))
for i in a:
    if b==i:
        print("the number existed in array ",b)
        break
else:
    print("the number don,t existed ",b)


