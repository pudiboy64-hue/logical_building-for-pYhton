a=[1,2,3,4,6,5]

# a=[6,5,4,3,2,1]
if a == sorted(a)[::-1]:
    print("the array is in disacending sorteded: ",a)
elif a!=sorted(a)[::-1]:
    print("the arrays is in acncsending  sorteed:",a)    
   