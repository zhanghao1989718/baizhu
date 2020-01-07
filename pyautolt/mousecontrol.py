import autoit


class MouseControl(object):
    '''
    AutoIt鼠标相关操作
    '''

    def __init__(self):
        '''
        Constructor
        '''

    def click(self, title, text, x, y, button="main", clicks=1):
        '''
        :description 执行鼠标点击操作
        '''
        pos = autoit.win_get_pos(title, text=text)
        autoit.mouse_click(button, x + pos[0], y + pos[1], clicks=clicks)

    def move(self, title, text, x, y):
        '''
        :description 移动鼠标指针
        '''
        pos = autoit.win_get_pos(title, text=text)
        autoit.mouse_move(x + pos[0], y + pos[1])

    def drag(self, title, text, x1, y1, x2, y2):
        '''
        :description 执行鼠标拖拽操作
        '''
        pos = autoit.win_get_pos(title, text=text)
        autoit.mouse_click_drag(x1 + pos[0], y1 + pos[1], x2 + pos[0], y2 + pos[1])

    def wheel(self, direction="up"):
        '''
        :description 产生向上或向下滚动鼠标滚轮事件.仅支持NT/2000/XP及更高.
        '''
        autoit.mouse_wheel(direction)