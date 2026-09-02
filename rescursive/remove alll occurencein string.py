# def occur(n):
#     if len(n)==1:
#         return n
#     count=0
#     if count==2:
#         return    
# def remove_char(text, target_char):
#     # Base case: if the string is empty, return it
#     if len(text) == 0:
#         return text
        
#     # If the first character matches the target, skip it
#     if text[0] == target_char:
#         return remove_char(text[1:], target_char)
        
#     # If it doesn't match, keep it and process the rest of the string
#     return text[0] + remove_char(text[1:], target_char)

# # Examples
# print(remove_char("fahad karim", "a"))  # Prints: fhd krim
# print(remove_char("fahad karim", "m"))  # Prints: fahad kari
# print(remove_char("fahad karim", " "))  # Prints: fahadkarim
# def remove_char(text ):
#     # Base case: if the string is empty, return it
#     if len(text) == 0:
#         return text
        
#     # If the first character matches the target, skip it
    
#     # If it doesn't match, keep it and process the rest of the string
#     return text[0] + remove_char(text[1:], )

# # Examples
# print(remove_char("fahad karim"))  # Prints: fhd krim
# print(remove_char("fahad karim"))  # Prints: fahad kari
# print(remove_char("fahad karim"))  # Prints: fahadkarim

def reverse_string(text):
    # Base case: if the string is empty or one character, return it
    if len(text) <= 1:
        return text
        
    # Take the last character and place it in front of the recursively reversed rest
    return text[-1] + reverse_string(text[:-1])

# Examples
print(reverse_string("fahad"))        # Prints: dahaf
print(reverse_string("fahad karim"))  # Prints: mirak dahaf

