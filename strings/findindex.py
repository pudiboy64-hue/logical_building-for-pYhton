# a=[1,2,3,4,5,6,7,8,9]
# print("chose from this only",a)
# target=int(input("of"))
# index=-1
# for i in a:
#     if a[i]==target:
#         index=i
#         break
#     index+=1
# print(target)    
fruits = ['apple', 'banana', 'orange']
target = 'banana'

index = 0
found_index = -1

while index < len(fruits):
    if fruits[index] == target:
        found_index = index
        break
    index += 1

print(found_index)  # Outputs: 1
