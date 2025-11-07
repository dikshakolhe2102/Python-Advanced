import re

##1. Search function = it means it search all string
# p=r"a|z"
# s=input("enter a string:")
# r=re.search(p,s)
# print(r)
# print(type(r))

# a=r"a|z"
# s=input("Enter a string:")
# c=re.search(a,s,re.I)
# if(c):
#     print("found",c.group(),c.start(),c.end())
# else:
#     print("Not found!")



## 2.match function = it means it only search 1st occourence
# p=r"[0-9]{2}"
# s=input("Enter a string:")
# r=re.match(p,s)
# if r:
#     print("Found",r.group(),r.start(),r.end())
# else:
#     print("Not found!")


##write a program to validate 1st name of a user which contain only alphanumeric character with length min 2 max 10
# name=r"^[a-zA-Z0-9]{2,10}$"
# user=input("Enter username:")
# r=re.search(name,user)
# if r:
#     print("Validate")
# else:
#     print("Not validate!")

#pincode are valid or not
# p="^4[0-4][1-9]{4}$"
# s=input("Enter pincode:")
# r=re.search(p,s)
# if r:
#     print("Valid")
# else:
#     print("Invalid!")


