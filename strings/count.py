# a=[1,2,34,2,3,3,94,-2,-3,-23,-23,0]
# count_p,count_n,count_z=0,0,0
# for i in a:
#     if i>0:
#         count_p+=1
#     if i==0:
#         count_n+=1
#     if i<0:
#         count_z+=1        
# print(count_p,count_n,count_z)        
a=[1,2,3,4,5,6,7,8,9]
count_e,count_o=0,0
for i in a:
    if i%2==0:
        count_e+=1
    else:
        count_o+=1
print(count_e,count_o)            