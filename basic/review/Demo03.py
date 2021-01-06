age = 18
name = 'TOM'
weight = 75.5
student_id = 1

# 我的名字是TOM
print('my name is %s' % name)

# 我的学号是0001
print('my id num is %4d' % student_id)

# 我的体重是75.50公斤
print('my weight is %.2f kg' % weight)

# 我的名字是TOM，今年18岁了
print('my name is %s，Im %d years old' % (name, age))

# 我的名字是TOM，明年19岁了
print('my name is %s，i will be %d years old next year' % (name, age + 1))

# 我的名字是TOM，明年19岁了
print(f'my name is {name}, i will be {age + 1} years old next year')