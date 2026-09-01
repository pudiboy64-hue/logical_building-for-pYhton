# def triangle(n):
#     if n==0:
#         return
#     print(n*"*")
#     triangle(n-1)
# triangle(4)    
def triangle(n):
    if n==0:
        return
    triangle(n-1)
    print(n*("*"))
triangle(5)    