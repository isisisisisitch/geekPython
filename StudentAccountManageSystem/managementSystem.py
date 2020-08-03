from StudentAccountManageSystem.student import Student


class managementSystem(object):

    def __init__(self):
        self.student_list = []#保存用户信息


    def run(self):
        self.load_student()
        while True:
        #显示功能列表
            self.show_menu()
            #获得用户输入
            num = int(input("plz choose your option:1~7:"))
            #根据用户不同的输入值，执行相应的功能
            if num == 1:
                self.add_student()

            elif num == 2:
                self.del_student()

            elif num == 3:
                print(self.modify_student())
            elif num == 4:
                print(self.query_student_by_name())

            elif num == 5:
                self.show_all()

            elif num == 6:
                self.save_student()

            elif num == 7:
                break
            print("========================================")



#显示功能列表
#加载数据
#保存数据

# - 添加
# - 删除
# - 修改
# - 查询

#显示功能列表
    def show_menu(self):
        print("plz select the option that you need:")
        print("1:add student")
        print("2:del student")
        print("3:modify student")
        print("4:query student")
        print("5:show all students info")
        print("6:save student info")
        print("7:add exit")


# - 添加
    def add_student(self):
        name = input("plz input student' name")
        gender = input("plz input student' gender")
        grade = input("plz input student' grade")

        student = Student(name,gender,grade)#constructor
        self.student_list.append(student)

        #print(self.student_list)

# - 删除
    def del_student(self):
        del_name = input("plz input student' name")

        for i in self.student_list:#student
            if del_name == i.name:
                self.student_list.remove(i)
                return f" student:{i.name} deleted"
        return "no such student!"


    # - 修改
    def modify_student(self):
        modify_name = input("plz input student' name")

        for i in self.student_list:  # student
            if modify_name == i.name:
                i.name = input("name:")
                i.gender = input("gender:")
                i.grade = input("grade:")
                return f'{i.name},{i.gender},{i.grade}'
        return "no such student!"
    # - 查询
    def query_student_by_name(self):
        query_name = input("plz input student' name")

        for i in self.student_list:  # student
            if query_name == i.name:

                return f'name : {i.name}, gender:{i.gender}, grade: {i.grade}'
        return "no such student!"


    def show_all(self):
        for i in self.student_list:
            print(f'name : {i.name}, gender:{i.gender}, grade: {i.grade}')
    #保存数据
    def save_student(self):
        f = open('studentinfo.data','w')

        new_list = [i.__dict__ for i in self.student_list]

        f.write(str(new_list))

        f.close()

    #加载数据
    def load_student(self):
        f = open('studentinfo.data', 'r')
        data = f.read()#每次读一个数据
        new_list = eval(data)#str
        self.student_list = [Student(i['name'],i['gender'],i['grade']) for i in new_list]
        print(self.student_list)

        f.close()

