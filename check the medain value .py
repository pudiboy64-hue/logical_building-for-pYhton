import random
even=[random.randint(1,9) for _ in range(6)]
odd =[random.randint(1,9) for _ in range(5)]
even.sort()
odd.sort()
print(even)
print(odd)  
odd_mid=len(odd)//2
even_mid=len(even)//2
even_median=(even[even_mid-1]+even[even_mid])/2
print("The median of odd number is ",odd[odd_mid])
print("The median of even number is ",even_median)
