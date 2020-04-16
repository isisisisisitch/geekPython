#the taste is not xxx poor!
#the taste is good!
#the taste is poor!
#the taste is poor!
str="the taste is  xxx poor"
snot = str.find("not")
print(snot)
spoor = str.find("poor")

if spoor> snot and snot>0:
    str = str.replace(str[snot:(spoor+4)],"good")
    print(str)
else:
    print(str)