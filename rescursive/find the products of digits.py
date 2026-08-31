# def product(n):
    

#     if n <10:
#         return n
#     return (n%10) *product(n//10)
# print(product(123))
def even_sum(n):
    if n==0:
        return n
    if n%2==0:
        return even_sum(n-1)
    even_sum(n-1)

print(even_sum(20)) 
