#abc
#abcing
#abcingly
str=input("plz input a word:")
if str[-3:]=="ing":
    str = str+"ly"
else:
    str = str + "ing"
print(str)
