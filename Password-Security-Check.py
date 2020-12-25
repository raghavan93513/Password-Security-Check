import string
a = input()
b = string.digits
c = string.punctuation
d = string.ascii_letters
if a[0] in d:
    for i in a:
        if i in c:
            flag1 = True
            break
        else:
            flag1 = False
else:
    flag1 = False

for i in a:
    if i in b:
        flag2 = True
        break
    else:
        flag2 = False

if len(a) >= 8:
    flag3 = True
else:
    flag3 = False

if flag1 and flag2 and flag3:
    print("Valid")
else:
    print("Invalid")