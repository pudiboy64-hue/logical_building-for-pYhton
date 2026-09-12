# a=[2,6,21,32,34,45,1,2,3]
# max_unq=max(a)
# min_unq=min(a)

# a.remove(max_unq)
# a.remove(min_unq)
# total_sum=sum(a)
# print(a)
# print(total_sum)
a=[2,6,21,32,34,45,1,2,3,6]
# k=12
# for i in range(len(a)-1):
#     if a[i]+a[i+1]==k:
#         print("its equal to k ",a[i],a[i+1])
#     else:
#         print("else i,st not equal to ")    

k = 12

seen = {}
found = False

for num in a:
    target = k - num
    if target in seen:
        print(f"Found pair: {target} + {num} = {k}")
        found = True
        break  # Remove 'break' if you want to find all matching pairs
    seen.add(num)

if not found:
    print("No pair adds up to k.")
