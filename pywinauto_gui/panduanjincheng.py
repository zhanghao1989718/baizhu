#-*- coding:utf-8 -*-
def check_exsit(process_name):
    import win32com.client
    WMI = win32com.client.GetObject('winmgmts:')
    processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % process_name)
    print(process_name)
    print("=" * 50)
    print(processCodeCov)
    print("+" * 60)
    if len(processCodeCov) > 0:
        print ('%s is exists' % process_name )
    else:
        print ('%s is not exists' % process_name )

if __name__ == '__main__':
    check_exsit('chrome.exe')