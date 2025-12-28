import re
pattern = "Apple"
if re.match(pattern,"Appleball"):
    print("True")
else:
    print("False")