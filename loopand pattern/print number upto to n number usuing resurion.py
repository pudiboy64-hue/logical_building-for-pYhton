# def num(n):
#     print("the umber are follows is:")
#     return num(n-1)
# a=num(2)
# print(a)
# def factorial(n):
#     # 1. Base Case
#     if n == 1:
#         return 1
    
#     # 2. Recursive Case
#     else:
#         return n +factorial(n - 1)
# a=factorial(5)
# print(a)
# def num(n):
#     if n==1:
#        return 1
#     for i in range(int(n)+1):
#       return n+num(n-1)
# a=num(10)
# print(a)    
# def num(n):
#     if n==0:
#         return 
#     num(n-1)
#     print(n)
# num(5)    
# def print_up_to_n(current, n):
#     # Base Case: Stop when current passes n
#     if current > n:
#         return
    
#     # Print the current number
#     print(current)
    
#     # Recursive Case: Call with the next number
#     print_up_to_n(current + 1, n)

# # To use it, you start at 1:
# print_up_to_n(1, 5)
# def num(current,n):
#     if n==0:
#         return
#     print(n)
#     num(current,n-1)
# print(1,5)  
# def num(n):
#     if n==0:
#         return
#     print(n)
#     num(n-1)  
# num(5)    
def num(n):
    if n==0:
        return
    num(n-1) 
    print(n)
     
num(5)    
