# for i in range(1,501):
#     if i==i[:-1]:
#         print(i)
# for i in range(1, 501):
#     # Convert i to a string to slice it, then convert back to int for comparison
#     if i == int(str(i)[:-1] or 0): 
#         print(i)
# i=122
# # print(int(str(i[-1])))
# print(str(i)[::-1])
for i in range(1,501):
    if i==int(str(i)[::-1]):
        print(i)
