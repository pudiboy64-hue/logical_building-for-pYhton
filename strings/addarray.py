# a=[1,2,3,4,5]
# b=[1,2,3,4,5]
# c=[]
# for i in range(len(a)):
#     c.append(a[i]+b[i])
# print(c)    
# a=[1,2,3,2,1,3,4,5,6]
# freq={}
# for i in a:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# for i in freq:

#  if freq[i]>1:
#     print(freq)          
a = [1, 2, 3, 2, 1, 3, 4, 5, 6]
freq = {}
for i in a:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for i in freq:
    if freq[i] > 1:
        print(i)  # Changed from freq to i

# Output will be:
# 1
# 2
# 3

