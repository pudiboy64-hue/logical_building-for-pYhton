# def vowel(n):
#     if len(n)==0:
#         return True
#     if n[-1].lower() in "aeiou" :
#             return vowel(n[:-1])
#     return False
# print(vowel("aieou"))            
# print(vowel("tpqrt"))
# def spaces(n):
#     if len(n)<=0:
#         return n
#     if n in " ":
#         return vowel(n[:-1])
#     return n
# print(spaces("fahad"))  
# print(spaces("fahad karim"))        
# def spaces(n):
#     # Base case: if the string is empty, return it
#     if len(n) == 0:
#         return n
        
#     # If the first character is a space, skip it and check the rest
#     if n[0] == " ":
#         return spaces(n[1:])
        
#     # If it's not a space, keep the character and check the rest
#     return n[0] + spaces(n[1:])

# print(spaces("fahad"))        # Prints: fahad
# print(spaces("fahad karim"))  # Prints: fahadkarim
  
def spaces(n):
    if len(n) == 0:
        return 0
        
    # Add 1 if the first character is a space, then check the rest
    if n[0] == " ":
        return 1 + spaces(n[1:])
        
    return 0 + spaces(n[1:])

print(spaces("fahad"))        # Prints: 0
print(spaces("fahad karim"))  # Prints: 1
