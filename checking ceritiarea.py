# import random
import string


password=["abcdefg3","12345678","acbdefgh","abcd12345677"]
for i in password:
    if len(i)<=8:
     has_digit=sum(1 for char in i if char.isdigit())
     if has_digit==1:
        print("it,s genuenely")
     else:
        print("it,s not  having have a digit ")   
    else:
       print("it,s lenght exceed it,s limitaion")
       
