def count_letters(n):
    # Base Case: When the string is completely empty, return 0 vowels and 0 consonants
    if n == "":
        return 0, 0
    
    # Get the count totals from the rest of the string first
    vowels, consonants = count_letters(n[:-1])
    
    # Grab the last character to check it, making it lowercase
    char = n[-1].lower()
    
    if char in "aeiou":
        return vowels + 1, consonants  # Found a vowel
    elif char.isalpha():
        return vowels, consonants + 1  # Found a consonant (is a letter, but not a vowel)
    else:
        return vowels, consonants       # Ignore spaces, numbers, or symbols

# Test the function
v_count, c_count = count_letters("aweiou")
print(f"Vowels: {v_count}, Consonants: {c_count}")
# Output: Vowels: 5, Consonants: 1
