import random
num=[]
for x in range(10):
    x=random.randint(0,100)
    num.append(x)
print(num)    
for i in num:
    if i<40 and i>=0:
        print(f"the student grade is{i} =fail") 
    elif i<55 and i>=40:
        print(f"the student grade is{i} =D")
    elif i<65 and i>=55:
        print(f"the student grade is{i} =C")
    elif i<75 and i>=65:
        print(f"the student grade is{i} =B")
    elif i<85 and i>=75:
        print(f"the student grade is{i} =A")
    else:
        print(f"the student grade is{i} =A+") 
    print(num[i])