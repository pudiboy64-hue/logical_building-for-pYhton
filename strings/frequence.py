a=[1,2,3,4,5,6,7,8,43,2,1,5,6,4,54,32,34,4,4]
freq={}
for i in a:
   if i in freq:
    freq[i]+=1
   else:
    freq[i]=1
print(freq)     
