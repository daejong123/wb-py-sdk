from .wbSerial import WBSerial

class wb_tool():
    '''
    豌豆拼工具集合
    '''

    @staticmethod
    def show_console():
        '''
        开启控制台输出
        '''
        WBSerial._is_show_console = True

    @staticmethod
    def hide_console():
        '''
        隐藏控制台输出（默认）
        '''
        WBSerial._is_show_console = False