
# def Even_num(n):
#     if n==0:
#         return 
#     if n%2==0:
#             print(n)
#     Even_num(n-1)
   
# Even_num(10)
def Even_num(n):
    if n==0:
        return 
    if n%2!=0:
            print(n)
    Even_num(n-1)
   
Even_num(10)