# a=[12345,54321]
# result=[range(len(str(a))-1) for i in a]
# print(result)
# a=123
# b=str(123)[::-1]
# print(b)
a=[123,456,876]
b=[int(str(i)[::-1]) for i in a]
print(b)