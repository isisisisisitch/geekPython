#check password
#at least 1 letter a~z A~Z
#at least 1 number 0~9
#at least 1 char [!$@]
#min length 6
#max length 16
if __name__ == '__main__':

    def get_user_password():
        ui = input("pls input ur password:")
        return ui


    def check_password(password):
        if len(password) < 6 or len(password) > 16:
            return "your password must be less than 16 digits and greater than 6 digits, pls input it again!"
        alp = False
        num = False
        cha = False
        for i in password:
            if i.isdigit():
                num = True
            elif i.isalpha():
                alp = True
            elif i == "!" or i == "$" or i == "@":
                cha = True
        if num == True and alp == True and cha == True:
             return "your password is set"

        return "your password must at least include 1 number, 1 letter, and 1 char, pls input it again!"



    print(check_password(get_user_password()))


