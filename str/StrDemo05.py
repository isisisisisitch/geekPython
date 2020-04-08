#List:[beginIndex:endIndex:len]
str="abcdefg"
    #0123456
print(str[2:5])#cde [beginIndex,endIndex)<===>[beginIndex,endIndex-1]
print(str[2:5:2])#ce 2 ---increase len
print(str[:5])#abcde beginIndex=null default beginIndex = 0
print(str[5:])#fg  endIndex=null default endIndex = str.len
print(str[0::2])#aceg
print(str[::-2])#gfedcba