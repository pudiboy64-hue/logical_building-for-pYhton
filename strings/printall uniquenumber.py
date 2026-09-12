# a=[1,3,5,6,7,54,42,131,1,22,3,4,5,6]
# # b=set(a)
# # print(b)
# # print(a & b)


# seen = set()
# duplicates = set()

# for num in a:
#     if num in seen:
#         duplicates.add(num)  # This is the "intersection" of elements appearing multiple times
#     seen.add(num)
# print(a)
# print(list(seen))
# print(list(duplicates))
# # Subtract the duplicates from all seen elements
# unique_elements = list(seen - duplicates)

# print("Elements appearing only once:", unique_elements)
# # Output:
a =[1,1,1,12,2,2,2,3,3,3,6,21,12,32,23,43,21,21]

seen = set()
duplicates = set()

# 1. Isolate duplicates using history tracking
for num in a:
    if num in seen:
        duplicates.add(num)
    seen.add(num)
print(a)
print(list(seen))
print(list(duplicates))

# 2. Use intersection (&) to find which unique items are duplicates
duplicate_items = seen & duplicates
print(list(duplicate_items))
# 3. Print the frequencies of those items
print("Duplicate Element Frequencies:")
for num in duplicate_items:
    # Use .count() only on the duplicates to keep it efficient
    print(f"Element {num} appears {a.count(num)} times")
