#对用户的输入统计 "exit" dead loop
#a~z A~Z  str.isalpha()
#0~9 str.isdigit()
#" " str.isspace()
#others
if __name__ == '__main__':


  def count_user_input():
    while True:
      user_input = input("plz input what you want:")#fjskdlj f423cz lcz   str
      if user_input == "exit":
          break
      # c = user_input[0]
      # print(c)
      letter = 0
      digit = 0
      space = 0
      others = 0
      i = 0
      while i < len(user_input):
          c = user_input[i]
          if c.isalpha():
              letter += 1

          elif c.isdigit():
              digit += 1
          elif c.isspace():
              space += 1

          else:
              others += 1

          i += 1

      print(f"letter:{letter},digit:{digit},space:{space},others:{others} ")


  count_user_input()