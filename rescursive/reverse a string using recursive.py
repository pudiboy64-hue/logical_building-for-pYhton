# def string(n):
#     if len(n)==1:
#         return n
#     return n[:-1],string(n[:-1])
# print(string("abcd"))        
# def string(n):
#     if len(n) <= 1:
#         return n
#     # Takes the first character and puts it at the end
#     return string(n[1:]) + n[0]

# print(string("abcd"))
# def string(n):
#     if len(n)<=1:
#         return n
#     if n[0]==n[-1]:
#         return string(n[1:]) 
# print(string("abcd"))           

def is_palindrome(n):
    # Base case: an empty string or single character is always a palindrome
    if len(n) <= 1:
        return True
        
    # Check if the first and last characters match
    if n[0] == n[-1]:
        # Recursive call: strip the first and last characters and check the rest
        return is_palindrome(n[1:-1])
        
    # If they don't match, it's not a palindrome
    return False

# Test cases
print(is_palindrome("abca"))  # Returns False
print(is_palindrome("racecar"))  # Returns True
