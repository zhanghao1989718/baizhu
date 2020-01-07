import time

def fib(x):
    if x<2:
        return x
    return fib(x-1)+fib(x-2)

if __name__ == '__main__':
    begin = time.time()
    print (fib(40))
    end = time.time()
    print (end-begin)

# a = time.time()
# time.sleep(0.1)
#
# b = time.time()
# c = b - a
# print("进程持续时间为: %d 秒" %c)
# print(c)
#
# sum = 0
# for i in range(1, 101):
#     sum = sum + i
#     print(sum)
# print(sum)
# a = [1,2,3,4,5]
# a.reverse()
# print(a)
