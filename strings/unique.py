a=[1,2,3,4,5,6,7,8,9]
b={}
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
if len(b)==len(a):
        print("it,s are unquire number of arrays")
else:
        print("the arrays is not unquire")                     
