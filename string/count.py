# a="pudi john"

# print(len(a)-a.count(" "))\

# a="this is a sentence that belong to deterimne the how much words are ther in a sentence"
# words=a.split()
# print(len(words))
# a=""
# b="john"
# if isinstance(a,str) and a:
#     print("it,s not empty")
# else:
#     print("it,s empty string")    
a = "pudi john"

for char in a:
    print(f"Character: '{char}' -> ASCII: {ord(char)}")
