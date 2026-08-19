
n=[]
p=[]
for i in range(1,101):
    n.append(i)
for i in n:
   if i <=1:
      continue
   if i==2:
      p.append(i)
      continue
   if i%2==0:
      continue
   elif i%i==0:
      p.append(i)
is_prime = True
for j in range(3, i, 2):
        if i % j == 0:
            is_prime = False
            break  # Not prime, stop checking
            
if is_prime:
        p.append(i)

print(p)  