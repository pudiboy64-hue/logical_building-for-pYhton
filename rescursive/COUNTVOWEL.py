def count(n):
    if n==0:
        return 
    if n in "aeiou":
        return 1+count(n[:-1])
    else:
        return 1+count(n[:-1])
print(count("aweiou"))               