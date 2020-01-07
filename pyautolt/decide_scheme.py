
def decide_scheme():
    c = ["软件", "办公", "onebox", "360营销", "百度营销", "游戏方案"]

    while True:
        a = input("请输入一个方案:")
        if a in c:
            print("这个方案是%s方案" % a)
            break
        print("这不是一正确的方案，请重新输入")
    return a

print(decide_scheme())
