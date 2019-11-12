import time

a = time.time()
time.sleep(0.1)

b = time.time()
c = b - a
print("进程持续时间为: %d 秒" %c)
print(c)

sum = 0
for i in range(1, 101):
    sum = sum + i
    print(sum)
print(sum)
