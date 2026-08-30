def sum_num(n):
    if n==0:
        return 0
    return n+sum_num(n-1)
a=sum_num(10)
print(a)
# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)
# a=factorial(5)
# print(a)
# def square(n):
#     if n<=1:
#         return 1
#     return n*square(n)
# a=square(2)
# print(a)
# def square(n):
#     # Base Case: The square of 1 is 1 (or square of 0 is 0)
#     if n == 0:
#         return 0
    
#     # Recursive Case: Uses the algebraic pattern for squares
#     return square(n - 1) + (2 * n) - 1

# a = square(5)
# print(a)

# def power(base, exp):
#     # Base Case: Any number to the power of 0 is 1
#     if exp == 0:
#         return 1
    
#     # Recursive Case: base^exp = base * base^(exp-1)
#     return base * power(base, exp - 1)

# # Example: 2 to the power of 3 (2 * 2 * 2)
# result = power(2, 3)
# print(result)
