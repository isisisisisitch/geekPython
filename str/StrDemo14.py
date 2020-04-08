#List:[beginIndex:endIndex:len ]
#"abc","def"  "dec         abf"
# str1  str2   new_str1   new_str2
str1 = input("plz inout a word:")
str2 = input("plz inout a word:")
new_str1 = str2[0:2] + str1[2:]
new_str2 = str1[0:2] + str2[2:]

res = new_str1+" "+new_str2

print(res)