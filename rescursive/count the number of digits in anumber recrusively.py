# def count(n):
#     if n<10:
#         return 1
    
    
#     return 1+count(n//10)
# print(count(12))   



#reverse the number recursively
def reverse(n):
    if n<10:
        return 1
    return n[::reverse(n//10)]

print(print(1234))   