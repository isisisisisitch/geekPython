# 需求：进入系统显示系统功能界面，功能如下：
#
# - 1、添加账户(id, name,salary)
# - 2、删除账户
# - 3、修改账户信息
# - 4、查询账户信息
# - 5、显示所有账户信息
# - 6、退出系统
#dict{id:1,name:dal,salary:100}
#list[{id:1,name:dal,salary:100},{id:1,name:dal,salary:100},{id:1,name:dal,salary:100}]
account_info=[]
def add_account():

    new_id = input("plz input your id:")
    new_name = input("plz input your name:")
    new_salary = input("plz input your salary:")

    #在添加用户之前，我们需要先判断之前是否已经添加过了该用户
    global account_info
    for i in account_info:
        if new_id== i['id']:
            print("already exist")
            return
    #如果不存在，则把当前数据追加到容器account_info中
        #第一次封装--->dict
    info_dict={}
    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['salary'] = new_salary
    account_info.append(info_dict)


def del_account():
    del_id = input("plz input id that you want to delete:")
    #判断待删除用户是否存在
    for i in account_info:
        if del_id == i['id']:
            account_info.remove(i)
            break
    else:
        print("does not exist,plz check the id")

def modify_account():
    modify_id = input("whats ur modify id:")

    # 在添加用户之前，我们需要先判断之前是否已经添加过了该用户
    for i in account_info:
        if modify_id == i['id']:
           i['salary'] = input("plz input the modify salary:")
        break
    else:
        print("does not exist,plz check the id")

def query_account():
    query_id = input("plz input your id:")
    for i in account_info:
        if query_id == i['id']:
            print(i)
            break
    else:
        print("does not exist,plz check the id")

def query_all():
    global account_info
    if len(account_info) == 0:
        print("no data")

    for i in account_info:
       print(f"account_id:{i['id']},account_name:{i['name']},account_salary:{i['salary']}")

def get_user_input():
    user_num = int(input('plz select #:'))
    if user_num == 1:
        add_account()

    elif user_num == 2:
        del_account()

    elif user_num == 3:
        modify_account()

    elif user_num == 4:
        query_account()

    elif user_num == 5:
        query_all()

    elif user_num == 6:
        print('exit')
        return False



def print_info():
    print('-' * 20)
    print('welcome to account Management System')
    print('1. add user')

    print('2. del user')

    print('3. modify user')

    print('4. query user by id')

    print('5. query all users')

    print('6. exit')
    print('-' * 20)


def driver():
    while True:
        print_info()
        user_input = get_user_input()
        if user_input==False:
            break

driver()
