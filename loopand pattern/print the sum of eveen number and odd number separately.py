even_counter=0
odd_counter=0
for i in range(1,101):
    if i%2==0:
     even_counter+=i
  
    if i%2!=0:
       odd_counter+=i
       
print(even_counter)        
print(odd_counter)