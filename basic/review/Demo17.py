#1.判断用户给定的输入是否为回文
#什么是回文：abcba, 1221

#2.判断用户输入的用户名的合法性
#要求：1.用户名可以由字母数字下划线组成 2.用户名只能以字母下划线开头 3.至少包含一个大写字母，一个数字和一个符号（!@#）

#3.给定一句话（只包含字母和空格） 将这句话的单词位置反转，单词用空格分割，单词之间只有一个空格，整句话的前后没有空格
#eg:"hello bytetube and dal"--->"dal and bytetube hello"

#4.设计一个字符串简化器
# 1) abcaaadddbvvsscccc => abca3d3bv2sc4 # 2) abc => abc # # 3) wwww => w4
# 4) abcaaddbbvvsscd => abca2d2b2v2cd

if __name__ == '__main__':

    # def get_user_input():
    #     return input("input ur string:")
    #
    #
    # def is_plalindrome(str):
    #     if str[:].__eq__(str[::-1]):
    #         return True
    #     else:
    #         return False
    #
    #
    # print(is_plalindrome(get_user_input()))
    #
    #
    # def get_user_input():
    #     return input("input ur username:")
    #
    #
    # def create_username(usr):
    #     alp = False
    #     num = False
    #     sym = False
    #     for i in usr:
    #         if i.isalpha():
    #             alp = True
    #         elif i.isdigit():
    #             num = True
    #         elif i.__eq__("!") or i.__eq__("@") or i.__eq__("#"):
    #             sym = True
    #     if usr[0] != "_" or alp != True or num != True or sym != True:
    #         return False
    #     return True


    # print(create_username(get_user_input()))
   #  def create_user_name(str):
   #
   #     return True
   #
   #
   # def reverse_str(str):
   #     return  " ".join(str.split(" ")[::-1])
       # list = str.split(" ")
       # list = list[::-1]
       # list = " ".join(list)
       # return list
   #
   #
   def transfer_str(s):
       #abcaaadddbvvsscccc  abca3d3bvs2c4
       #                    abca3d3bv2s2
       res = ""
       next = 0
       count = 1
       for i in range(len(s)):
           next += 1
           if next < len(s):
               if s[i] == s[next]:
                   count += 1

               else:
                   res += s[i]

                   if count > 1:
                       res += str(count)
                       count = 1

           else:
               res += s[i]
               if count > 1:
                   res += str(count)

       return res
# list = reverse_str("hello bytetube and dal")
# print(list)
res = transfer_str("abcaaddbbvvsscd")
#abca2d2b2v2s2cd
#abca2d2b2v2s2cd
print(res)