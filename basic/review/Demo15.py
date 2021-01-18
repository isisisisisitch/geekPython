

if __name__ == '__main__':


    def fib(n):
        first = 0
        second = 1
        for i in range(n - 1):
            num = first
            first = second
            second = num + first
        return second


    print(fib(6))