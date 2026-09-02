# def upper_case(n):
#     if len(n)==0:
#         return n
    
#     return n[0].upper()+upper_case(n[1:])
  
# print(upper_case("abcd"))    
def upper_case(n,is_capl=True):
    if len(n)==0:
        return n
    if is_capl:
        return n[0].upper()+upper_case(n[1:],is_capl=False)
    else:
        return n[0]+upper_case(n[1:],is_capl=False )   
    
print(upper_case("abcd"))    