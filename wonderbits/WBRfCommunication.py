from .wbits import Wonderbits

def _format_str_type(x):
    if isinstance(x, str):
       x = str(x).replace('"', '\\"')
       x = "\"" + x + "\""
    return x

class RfCommunication(Wonderbits):
    def __init__(self, index = 1):
        Wonderbits.__init__(self)
        self.index = index

    
    def register_button(self, cb):
        self._register_event('rfCommunication{}'.format(self.index), 'button', cb)
    
    def register_msg_received(self, cb):
        self._register_event('rfCommunication{}'.format(self.index), 'msg_received', cb)
    
    def get_msg(self):
        """
        使用该函数可得到最近一次通信收到的内容，如果在程序开始后或使用clear_msg函数后没有发生过通信将返回None:rtype: float
        """

        command = 'rfCommunication{}.get_msg()'.format(self.index)
        return self._get_command(command)
    
    def clear_msg(self):
        """
        清除最新的通信内容，在再次接收到新的通信内容之前调用get_msg只会返回None调用此函数并不会影响get_unread_msg_count和read的使用

        """

        args = []
        command = "rfCommunication{}.clear_msg({})".format(self.index, ",".join(args))
        self._set_command(command)

    
    def get_unread_msg_count(self):
        """
        该函数用于获取通信存储队列中未读内容的个数，最多存储32个未读内容:rtype: int
        """

        command = 'rfCommunication{}.get_unread_msg_count()'.format(self.index)
        return self._get_command(command)
    
    def read(self):
        """
        该函数用于获取通信存储队列中未读内容，读取后会删除这个数据:rtype: float
        """

        command = 'rfCommunication{}.read()'.format(self.index)
        return self._get_command(command)
    
    def send(self, number):
        """
        发送数据。调用此函数后，与本模块通信名字相同的模块将会受到发送的内容

        :param number: 发送的数值
        """

        args = []
        args.append(str(number))
        command = "rfCommunication{}.send({})".format(self.index, ",".join(args))
        self._set_command(command)

    
    def init(self, name = None):
        """
        设置模块通信名字。只有通信名字相同的模块之间才可以互相通信，不想互相通信的模块需要设置不同的通信名字

        :param name: 通信名字
        """

        name = _format_str_type(name)
        args = []
        if name != None:
            args.append(str(name))
        command = "rfCommunication{}.init({})".format(self.index, ",".join(args))
        self._set_command(command)

    
    def is_button_pressed(self):
        """
        该函数用于获取按键是否被按下:rtype: bool
        """

        command = 'rfCommunication{}.is_button_pressed()'.format(self.index)
        return self._get_command(command)
    