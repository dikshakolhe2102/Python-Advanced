import re
##Grouping 
##Types of grouping
##1.find all = it finds in all string
##syntax re.findall(pattern,string)


##examples of grouping
# p="(ab)"
# s=input("Enter string:")
# l=re.findall(p,s)
# print(l)

# p=r"^\w+$"
# s=input("Enter string:")
# l=re.findall(p,s)
# print(l)

# p=r"[0-9]{2}[A-Z]{1}[a-z]{1}"
# s=input("Enter string:")
# l=re.findall(p,s)
# print(l)

##2.finditer = it is for iteration
##syntax re.finditer(pattern,string)

# p=r"[0-9]{2}[A-Z]{1}[a-z]{1}"
# s=input("Enter string:")
# l=re.finditer(p,s)
# for i in l:
#     print(i.group(),i.start(),i.end())

# p=r"[0-9]+"
# s=input("Enter string:")
# l=re.finditer(p,s)
# for i in l:
#     print(f"span:{i.span()},Starting Index:{i.start()},Ending Index:{i.end()},Group:{i.group()}")
#     print()


##p=r"^[1-9]{4}[-/.]{1}[0-9]{1,2}[-/.][0-9]{1,2}"
# p=r"^\d{4}[.\/\-]\d{1,2}[.\/\-][0-3]{1}\d{1}$"
# s=input("Enter a Date:")
# l=re.findall(p,s)
# print(l)

# p=r"^\d{4}-\d{4}-\d{4}-\d{4}$"
# s=input("Enter credit card no:")
# l=re.findall(p,s)
# print(l)


# p=r"https?://\w+\.\w+"
# s="Visit https://regex101.com or http://RegExp.org  or https://regexr.com for details."
# l=re.findall(p,s)
# print(l)

##3.Capturing group = it return complete group

# p=r"^(\d{4})-(\d{4})-(\d{4})-(\d{4})$"
# s=input("Enter credit card no:")
# r=re.search(p,s)
# print(r.group(1),r.group(2),r.group(3),r.group(4))

##4.Uncapturing group = this group does not capture but match the group
# p="(?:\d{4})-(\d{4})-(\d{4})-(\d{4})"
# s=input("Enter no:")
# r=re.search(p,s)
# print(r.group())
# print(r.group(1))
# print(r.group(2))
# print(r.group(3))


# p=r"(<\w+>(?:\w+)?</\w+>)+"
# s="<h1>Python</h1> or <i1>Python</i1>"
# r=re.findall(p,s)
# print(r)


# p=r"</?\w+>"
# s="<h1>Python</h1> or <i1>Python</i1>"
# r=re.findall(p,s)
# print(r)

# p=r"</?\w+>"
# s=input("Enter string:")
# r=re.findall(p,s)
# print(r)


###Back reference method = it using group number
# p=r"<(/?\w+)>(?:\w+)?<\1>"
# s=input("Enter string:")
# r=re.findall(p,s)
# print(r)


# p=r"(\w+)\1"
# s=input("Enter string:")
# r=re.findall(p,s)
# print(r)

p=r"(\b)(\w)(\1)"
s=input("Enter a string:")
r=re.findall(p,s)
print(r)