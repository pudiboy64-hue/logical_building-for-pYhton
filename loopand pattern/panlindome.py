def is_palindrome(number):
    # Convert the number to a string
    num_str = str(number)
    
    # Compare the string with its reverse
    return num_str == num_str[::-1]

# Test cases
test_numbers = [121, 1331, 456, 7]

for num in test_numbers:
    if is_palindrome(num):
        print(f"✅ {num} is a palindrome number!")
    else:
        print(f"❌ {num} is NOT a palindrome number.")
