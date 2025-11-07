# s=input("Enter a string:")
# def f1():
#     if(len(s)==10 or len(s)==13):
#         if(s.isdigit()):
#             if(not s.startswith("0")):
#                 if(s.startswith("+91")):
#                     print(s)
#     else:
#         print("Invalid")
# f1()


a='''python
program'''
'''Diksha'''     #comment

#how to form pattern?
"\d,\D,\w,\W,\s,\S"     # all are meta characters
'[abc]'
'[^abc]' #cap means that does not includes these character
'[a-z]'  #a-z means it includes all characters between a to z
'[A-Z]'
'[0-9]' or '\d'  #it includes 0 to 9 number #d stands for digit
'[^0-9]' or '\D'  #it excludes all number between 0 to 9
'[a-b A-Z 0-9]' or '\w'  #it includes all 
'[^a-b A-Z 0-9]' or '\W'  #Excludes
'[\n \t.........]'  or '\s' #includes
'[^ \n \t........]' or '\S'  #Excludes

#regx101.com for practice

#Quantifier (It tells quantity)
"""
[0-9] it occur only one character
a+    | 1 or more         | a,aa,aaa,aaaa,..........
------|-------------------|-------------------------
a*    |0 or more          | ,a,aa,aaa,aaaa,.........
------|-------------------|-------------------------
a?    |0 or 1             |
------|-------------------|-------------------------
a{2}  | only 2            | aa
------|-------------------|-------------------------
a{2, }|Min 2 Max many more|aa,aaa,aaaa,......
------|-------------------|-------------------------
a{ ,3}|at most 3          |a,aa,aaa
------|-------------------|-------------------------
a{2,3}|min 2 max 3        |aa,aaa
------|-------------------|-------------------------
"""

#examples
print("abc\\tpqr")
print(r'abc\tpqr')


"""
. operator 
^ carect operator
$ operator
| operator
for fix character use this operator ^
for ending fix ending use this character $
"""

## formation of patterns
#write a pattern in which 1st 4 character are digit between 1 to 4 followed by 2 uppercase character and 2 lowecase operator
a="[1-4]{4}[A-Z]{2}[a-z]{2}"


#create a pattern in which 1st 3 character are from sir name followed by dob followed by 3 character of 1st name and followed by age
a="^[a-z A-Z]{3}[1-9]{8}[a-z A-Z]{3}[1-9]{2}$"

#create pincode
r="^4[0-4][1-9]{4}$"

# formation of mobile number
#1.start with +91
#2.1st digit between 7 to 9
#3.9 digit between 0 to 9
mobile_Number="^[+91]?[7-9][0-9]{9}$"

#formtion of mail id
#1.
mail="^\w+@[a-z A-Z]{2,8}\.[a-z A-Z]{2,3}$"



