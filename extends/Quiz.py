# person 2 attributes:name(public) age(private)
# sleep
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def sleep(self):
        print(f'{self.name} is sleeping')

    def getAge(self):
        return self.__age

    def setAge(self, age):
        self.__age = age

    def run(self,a):
        print(f'{self.name} is {self.__age} years old, he/she is running')
        print(a)

# A = Person('david', 12)
# print(A.getAge())
# A.setAge(14)
# A.sleep()
# print(A.getAge())


# student person subclass
class Student(Person):
    def __init__(self, student_id, name, age):
        self.__student_id = student_id
        super().__init__(name, age)

    def study(self):
        print(f'name: {self.name}, student id:{self.__student_id} is studying')

    def run(self):
        super().run(10)

        print(f'{self.__student_id} is running')


stu1 = Student(1,'David', 13)
stu2 = Student(2,'jim', 15)
stu1.run()