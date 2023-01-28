import re
pincode=input("enter a 6 digit pin:")
result=re.findall("^[1-9]{1}[0-9]{5}$",pincode)
print(result)
if result:
    print("correct pincode")
else:
    print("wrong pincode")
