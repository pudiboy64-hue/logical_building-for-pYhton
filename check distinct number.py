# import random
# from collections import Counter
# num=[random.randint(1,9) for _ in range(3)]
# print("before check distinct number",num)
# freq=Counter(num)

# if max(freq.values())==1:
#         print("the number all distinct")
# else:
#         print("all number are not distinct")    
import random
num=[random.randint(1,9) for _ in range(3)]
print("before check distinct number",num)
print(set(num))
if len(num)==len(set(num)):
    print("the NUmber all distinct ")
else:
    print("the number are not all ditinct numbert")    