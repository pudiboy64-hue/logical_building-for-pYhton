# a=[123,123]
# result=[]
# for i in a:
#     count=0
#     for _ in range(len(str(i))):
#      count+=1
#     result.append(count)    
# print(result)    
# a = [123, 123]
# result = [len(str(i)) for i in a]
# print(result)  # Outputs: [3, 3]





#add the digit sum
# a=[123]
# b=0
# for i in a:
#  print(i)
#  b+=i
#  print(b)






# a="123"
# print(str(a)[-1])







# a= 1234
# num=str(a)
# sum=0
# for i in num:
#     sum+=int(i)
# print(sum)    

# The number you want to check
# number = 12321

# # Make sure the number is positive
# temp_num = abs(number)

# # Start a counter at zero
# digit_sum = 0

# # Loop until there are no digits left
# while temp_num > 0:
#     # 1. Get the last digit using the remainder (modulo) operator
#     last_digit = temp_num % 10
    
#     # 2. Add the last digit to our running total
#     digit_sum = digit_sum + last_digit
    
#     # 3. Chop off the last digit using integer division
#     temp_num = temp_num // 10

# # Print the final result
# print("The sum of the digits using pure math is:", digit_sum)












a=[123,456,7885,3221]
for i in a:
    temp=abs(i)
    sum=0
    while temp>0:
        one=temp%10
        sum+=one
        temp=temp//10
    print("the sum of the digit using pure math is:",sum)        
