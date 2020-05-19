# - 1、添加学员  id,name,grade
# - 2、删除学员
# - 3、修改学员信息
# - 4、查询学员信息
# - 5、显示所有学员信息
# - 6、退出系统

#准备一个学员容器--->学员信息
accout_info=[]
def add_account():
    #获得用户输入
    new_id = input("plz input your id:")
    new_name = input("plz input your name:")
    new_grade = int(input("plz input your grade:0~99:"))
    # 判断之前的容器当中，是否已经有该学员信息（id）
    global accout_info
    for i in accout_info:
        if new_id == i['id']:
            print("already exist")
            return
#如果不重复，把当前数据追加到原容器中即可
    info_dict={}
    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['grade'] = new_grade
    print(f"{new_name} is added")

    accout_info.append(info_dict)



def del_account():
    #1.获得被删除用户的id
    del_id = input("plz input the del id:")

    #2.判断该用户是否存在
    #遍历容器，如果存在，从容器中删除即可
    for i in accout_info:
        if del_id== i['id']:
            accout_info.remove(i)
            print(f"{i['name']} is deleted")
            break
    #不存在，提醒用户，该用户不存在
    else:
        print("does not exist")

    # print(accout_info)



def modify_account():
    # 1.获得用户的id
    id=input("whats ur modify id:")
    # 2.判断该用户是否存在
    for i in accout_info:
        # 遍历容器，如果存在，从容器中修改其成绩
        if i['id']==id:
            i['grade']=input("ur grade:")
            print(f"{i['name']} 's  grade is updated")
            break
            # 2.不存在，提示用户
        else:
            print("doesn't exist")
    # print(accout_info)


def search_account():
    id = input("whats ur id?")
    global accout_info

    for i in accout_info:
    # 判断该用户是否存在
        if id == i['id']:
            print(i)
            break

        else:
            print("doesn't exist")


def search_accounts():

    global accout_info

    if len(accout_info) == 0:
        print("nobody!")

    for i in accout_info:
        print(f"account_id:{i['id']}, account_name:{i['name']}, account_grade: {i['grade']}")



# def exit():
#     reference = input("do you want to exit? y or n")
#
#     if reference=='y':

def menu():
    print('1. add user')

    print('2. del user')

    print('3. modify user')

    print('4. query user by id')

    print('5. query all users')

    print('6. exit')

def get_user_input():
    num = int(input("plz select #:"))

    if num==1:
        add_account()

    elif num == 2:
        del_account()

    elif num == 3:
        modify_account()

    elif num == 4:
        search_account()

    elif num == 5:
        search_accounts()

    elif num == 6:
       return False

    else:
        print("invalid num,plz input again!")


# - 1、添加学员  id,name,grade
# - 2、删除学员
# - 3、修改学员信息
# - 4、查询学员信息
# - 5、显示所有学员信息
# - 6、退出系统




def driver():
    while True:
        menu()
        res = get_user_input()

        if res==False:
            break


driver()