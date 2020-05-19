# 0     1    2    3    4    5    6    7
#   fib(1)  fib(2) fib(3)
# 1      1    2    3    5    8   13   21...
#fib(3) = fib(2)+fib(1)
#fib(4) = fib(3)+fib(2)

#fib(n) = fib(n-1)+fib(n-2)

def fib(n):#n表示第n+1个数的结果
    num1 = 1
    num2 = 1
    if n<2:#base case
        return 1

    return fib(n-1)+fib(n-2)



print(fib(6))