import random
num=[random.randint(-10,10) for _ in range(2)]
x,y=num[0],num[1]

if x>0 and y>0:
    print(f"the x {x}, {y} y quardrant lies in 1st")
elif x<0 and y>0:
    print(f"the x {x}, {y} y quardrant lies in 2nd")    
elif x<0 and y<0:
    print(f"the x {x}, {y} y  quandrant lies in 3rd")  
elif x>0 and y<0:
    print(f"the x {x}, {y} y quardrant lies in 4rd")      
if x==0 and y==0:
    print(f"the {x}x and {y}y lies in origin")
elif y==0:
    print(f"the coridinate lies in {x} x axis")
elif x==0:
    print(f"the coridinate lies in {y} Y axis")        