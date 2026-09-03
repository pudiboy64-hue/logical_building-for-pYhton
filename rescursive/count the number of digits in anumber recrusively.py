# def count(n):
#     if n<10:
#         return 1
    
    
#     return 1+count(n//10)
# print(count(12))   
# def reverse(n):
#     if n<10:
#         return 1
#     return n[::reverse(n//10)]

# print(print(1234))   


#reverse the number recursively
def reverse_num(n):
    # Convert to string to handle reversal easily
    s = str(n)
    
    # Base case: if it's a single digit, return it
    if len(s) == 1:
        return s
    
    # Take the last digit and put it in front of the reversed remaining digits
    return s[-1] + reverse_num(s[:-1])

# Convert back to an integer at the end
result = int(reverse_num(1234))
print(result)  # Output: 4321
