# def sum_digits(n):
#     # Base Case: If the number is a single digit, just return it
#     if n == 1:
#         return 1
    
#     # Recursive Case: Take the last digit + sum the rest of the digits
#     last_digit = n % 10
#     remaining_digits = n // 10
    
#     return last_digit + sum_digits(remaining_digits)

# # Test the function
# result = sum_digits(1234)
# print(result)
def fibonnaci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonnaci(n-1)+fibonnaci(n-2)
a=fibonnaci(5)
print(a)