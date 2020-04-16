# 坐公交：如果有钱可以上车，没钱不能上车；
# 上车后如果有空座，则可以坐下；
# 如果没空座，就要站着。怎么书写程序？


# a = 1
# b = 2
#
# c = a if a > b else b
# money = int(input("how much money do I have:"))
# seat = 0
#
# if money>=2:
#     print("welcome")
#
#     if seat>=1:
#         print("you can have a seat")
#     else:
#         print("sorry,you have to stand by")
#
# else:
#     print("you can not get on the bus")

money=int(input('money:'))
seat=int(input('seat'))
# c = a if a > b else b
result='you cannot get on the bus' if money<2       else 'welcome'+'seat' if money>=2 and seat>=1 else 'welcome'+'stand by'
print(result)