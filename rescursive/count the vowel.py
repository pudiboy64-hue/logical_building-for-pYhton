# def vowel(n):
#     if len(n)==0:
#         return True
#     if n[-1].lower() in "aeiou" :
#             return vowel(n[:-1])
#     return False
# print(vowel("aieou"))            
# print(vowel("tpqrt"))
def spaces(n):
    if len(n)<=0:
        return n
    if n in " ":
        return vowel(n[:-1])
    return n
print(spaces("fahad"))  
print(spaces("fahad karim"))          
