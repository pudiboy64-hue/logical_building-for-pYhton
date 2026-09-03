# n=int(input("enter the number of ara you want to create"))
# arrays=[]
# for i in range(n):
#     user=input(f"input the {i+1} in ")
#     current=[int(x) for x in user.spilt()]
#     arrays.append(current)
# print(arrays)
# 1. Ask for the number of arrays
# num_arrays = int(input("Enter the number of arrays (N): "))

# all_arrays = []

# # 2. Loop N times to collect each array
# for i in range(num_arrays):
#     # Ask user to input numbers separated by spaces (e.g., "1 2 3 4")
#     user_input = input(f"Enter elements for array {i+1} (separated by spaces): ")
    
#     # Split the string by spaces and convert each piece into an integer
#     current_array = [int(x) for x in user_input.split()]
    
#     # Store it in our master list
#     all_arrays.append(current_array)

# # Print the resulting list of arrays
# print("\nYour nested arrays:")
# print(all_arrays)
my=[1,2,3,4,5]
sum=0
avg=0
# for i in range(len(my)):
#     print(i)
for i in my:
    sum+=i

print(f"the sum of the arrays is {sum}")
avg=sum/len(my)
print(avg)