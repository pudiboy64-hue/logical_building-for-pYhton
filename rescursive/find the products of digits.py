# def product(n):
    

#     if n <10:
#         return n
#     return (n%10) *product(n//10)
# print(product(123))
# def even_sum(n):
#     if n==0:
#         return n
#     if n%2==0:
#         return even_sum(n-1)
#     even_sum(n-1)

# print(even_sum(20)) 
def even_sum(n):
    # Base case: stop at 0
    if n == 0:
        return 0
    
    # If the number is even, add it and move to the next number
    if n % 2 == 0:
        return n + even_sum(n - 1)
    
    # If the number is odd, skip it and just move to the next number
    return even_sum(n - 1)

print(even_sum(20))  # Output: 110
