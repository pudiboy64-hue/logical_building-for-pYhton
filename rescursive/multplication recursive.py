# def multiplication(n):
#     if n==1:
#         return
#     s=n
#     multiplication(s-1)
#     print(n*s)
# multiplication(4)  
def multiplication_table(n, count=1):
    # Base case: stop after multiplying up to 10 (or any limit you choose)
    if count > 11:
        return
    
    # Print the current multiplication step
    print(f"{n} * {count} = {n * count}")
    
    # Recursive call: move to the next multiplier
    multiplication_table(n, count + 1)

# Test the function
multiplication_table(4)
  