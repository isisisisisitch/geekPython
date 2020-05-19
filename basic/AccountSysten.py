accout_info=[]
def add_account():
    #获得用户输入
    new_id = input("plz input your id:")
    new_name = input("plz input your name:")
    new_grade = int(input("plz input your grade:0~99"))
    # 判断之前的容器当中，是否已经有该学员信息（id）
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
    print(accout_info)
def del_account():
    del_id=input('plz input id')
    for i in accout_info:
        if del_id==i['id']:
            accout_info.remove(i)
            print(f"{i ['name']} is deleted")
            break
    else:
        print("don't exist")
    # print(accout_info)


def modify_account():
    id=input("whats ur modify id?")
    for i in accout_info:
        if i['id']==id:
            i['grade']=input("ur grade:")
            print(f"{i['name']}'s grade is updated")
            break
        else:
            print("doesn't exist")
    # print(accout_info)



def search_account():
    search_id = input("what ur id?")
    global accout_info
    for i in accout_info:
        #判断该用户是否存在
        if search_id == i['id']:
            print(i)
            break
    else:
        print("doesn't exist")

def search_accounts():
    global accout_info
    if len(accout_info)==0:
        print("nobody!")
    for i in accout_info:
        print(f"accout_id:{i[id]},account_name:{i ['name']},account_grade:{i['grade']}")


 # def exit():
 #     reference = input("do you want to exit? yes or no")
 #     if reference=="yes":
 #         exit()
def menu():
    print('add user')
    print('del user')
    print('modify user')
    print('query user by id')
    print('query all users')
    print('6.exit')
def get_user_input():
    num=int(input("plz select num:"))
    if num==1:
        add_account()
    elif num==2:
        del_account()
    elif num==3:
        modify_account()
    elif num==4:
        search_account()
    elif num==5:
        search_accounts()
    elif num==6:
        return False
    else:
        print("INVALID NUM,PLZ INPUT AGAIN!")

def driver():
    while True:
        menu()
        res=get_user_input()
        if res==False:
            break


driver()


