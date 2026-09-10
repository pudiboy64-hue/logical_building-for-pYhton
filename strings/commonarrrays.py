# a=[1,3,5,7,8]
# b=[2,4,6,8,10]
# for i in  a:
#     for j in b:
#         if i==j:
#             print(i)
#         else:
#             print("not found")    
# a = [1, 3, 5, 7, 8]
# b = [2, 4, 6, 8, 10]

# # Find common elements using sets
# common = set(a) & set(b)
# print(list(common))  # Output: [8]
# a=[1,2,3,4,5]
# b=[1,2,3,4,6]
# for i,j in zip(a,b):
#     if i!=j:
#         print(i)
#     else:
#         print("not found2")    
# a = [1, 2, 3, 4, 5]
# b = [1, 2, 3, 4, 6]

# # Find items that are in 'a' or 'b', but NOT both
# uncommon = set(a) ^ set(b)

# print(list(uncommon))
# # Output: [5, 6]
a=[1,2,3,4,5]
b=[1,2,3,4,6]
common=set(a)&set(b)
print(list(common))