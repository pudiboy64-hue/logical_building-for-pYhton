# a=[1,2,3,4,5,6]
# max=0
# for i in a:
#     if i>max:
#         max=i
# a = [12, 35, 1, 10, 34, 1]

# # Convert to set to handle duplicates, sort it, and pick the second last element
# unique_sorted = sorted(list(set(a)))

# if len(unique_sorted) < 2:
#     print("No second largest element exists.")
# else:
#     print("Second largest element:", unique_sorted[-2])  # Output: 34

a=[12,35,1,10,34,1]
unq_sorted=sorted(set(a))[::-1]
if len(unq_sorted)<2:
    print("list must not equal not equal to 2 elment")
else:
    print("second smallest elment: ",unq_sorted[-2])    
print(unq_sorted)    