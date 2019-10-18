import os
import shutil
# 创建获取当前桌面路径的方法
# def get_desk_p():
#     return os.path.join(os.path.expanduser('~'),"Desktop")
# 在当前桌面创建文件夹iDownload
# os.makedirs(get_desk_p() + '\\iDownload')

# 判断C盘是否有文件夹iDownload
print(os.path.exists('c:\\iDownload'))

# os.makedirs(os.path.join(os.path.expanduser('~'),"Desktop") + '\\iDownload')
# 判断桌面是否有文件夹iDownload
print(os.path.exists(os.path.join(os.path.expanduser('~'),"Desktop")+ '\\iDownload'))

# if os.path.exists(os.path.join(os.path.expanduser('~'),"Desktop")+ '\\iDownload'):
#     print("桌面已有iDownload文件夹")
# else:
#     os.makedirs(os.path.join(os.path.expanduser('~'), "Desktop") + '\\iDownload')

try:
    os.makedirs(os.path.join(os.path.expanduser('~'), "Desktop") + '\\iDownload')
    print("创建文件夹iDownload")
except:
    print("桌面已有iDownload文件夹")
    try:
        # 删除空文件夹
        os.remove(os.path.join(os.path.expanduser('~'), "Desktop") + '\\iDownload')
        print("删除空文件夹")
    except:
        # 删除非空文件夹
        shutil.rmtree(os.path.join(os.path.expanduser('~'), "Desktop") + '\\iDownload')
        print("删除非空文件夹")