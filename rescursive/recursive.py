# def stars(n):
#     if n==0:
#         return 0
#     stars(n-1)
#     print(n*"*")
# stars(5)    
# def print_column(cols):
#     if cols==0:
#         return  
#     print("*",end=" ")
#     print_column(cols-1)
# def square(rows,cols=0):
#     if cols is None:  
         
#      cols=rows
#     if rows==0:
#        return 
#     print_column(cols)  # Recursive call to print the asterisks in this row
#     print()          # Move to the next line
#     square(rows - 1, cols)
# square(4)    
def print_row(cols):
    """Recursively prints a single row of asterisks."""
    if cols == 0:
        return
    print("*", end=" ")
    print_row(cols - 1)

def square(rows, cols=None):
    """Recursively prints an n x n square grid."""
    # Initialize cols to match the starting size of the rows
    if cols is None:
        cols = rows
        
    # Base case: stop when no rows are left
    if rows == 0:
        return
        
    print_row(cols)  # Recursive call to print the asterisks in this row
    print()          # Move to the next line
    square(rows - 1, cols) # Recursive call to print the next row

# Test the function
square(4)
