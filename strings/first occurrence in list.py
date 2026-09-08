# # a=[0,0,0,0,0,0,0,1,1,1,1,1,1]
# # x=set()
# # for i in a:
# #     if i not in x:
# #         print("the first occurencee number is %d",i)
# #         x.add(i)
# #     print(i)    
# a=[1,2,3,4,5]
# for i in range(len(a)):
#     print(a[i])
# def find_occurrences(arr, target):
#     first_idx = 1
#     last_idx = 1
    
#     # Find first occurrence (scan forward)
#     for i in range(len(arr)):
#         if arr[i] == target:
#             first_idx = i
#             break # Stop immediately
            
#     # Find last occurrence (scan backward)
#     for i in range(len(arr) - 1, -1, -1):
#         if arr[i] == target:
#             last_idx = i
#             break # Stop immediately
            
#     return first_idx, last_idx

# # Example Usage:
# numbers = [4, 2, 7, 2, 8, 2, 5]
# print(find_occurrences(numbers, 2)) # Output: (1, 5)
for i in range(7,-1,-1):
    print(i)