#学生成绩评比
#90～100 A+
#80～89 A
#70～79 B
#60～69 C
#<60 F
#代码的穿透性
#1.if ...elif...elif...elif...else 只要有一个条件命中，其他的判断不会执行，此时不会发生代码的穿透
#2.if ...if...if...if...只要有一个条件命中，其他的判断仍旧会执行，此时会发生代码的穿透
#3.if ...if...if...if...else 只要有一个条件命中，其他的判断仍旧会执行，此时会发生代码的穿透，并且else会发生就近原则
if __name__ == '__main__':

    grade = int(input('plz input your grade：'))
    if (grade >= 90) and (grade <= 100):
        print(f'your grade is {grade},A+')
    if (grade >= 80) and (grade <= 89):
        print(f'your grade is {grade},A')

    if (grade >= 70) and (grade <= 79):
        print(f'your grade is {grade},B')


    if (grade >= 60) and (grade <= 69):
        print(f'your grade is {grade},C')
    else:
        print(f'your grade is {grade},F')