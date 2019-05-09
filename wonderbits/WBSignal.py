from .wbits import Wonderbits





class Signal(Wonderbits):
    def __init__(self, index = 1):
        Wonderbits.__init__(self)
        self.index = index

    
    def set_rgb(self, r, g, b):
        """
        设置LED灯颜色三个参数都为0时，表示灯不发光

        :param r: 红色：0~255 
        :param g: 绿色：0~255 
        :param b: 蓝色：0~255 
        """

        args = []
        args.append(r)
        args.append(g)
        args.append(b)
        command = f'signal{self.index}.set_rgb({",".join(args)})'
        self._set_command(command)

    
    def set_buzzer(self, frequency):
        """
        设置蜂鸣器声音频率，单位Hz设置频率为0表示关闭蜂鸣器参数为1~20时发出的是同一个声音

        :param frequency: 频率：0~20000 Hz 
        """

        args = []
        args.append(frequency)
        command = f'signal{self.index}.set_buzzer({",".join(args)})'
        self._set_command(command)

    
    def set_vibration(self, strength):
        """
        设置震动马达的震动幅度这里的振动幅度没有单位，值越大表示震动幅度越大，参数为0则停止震动

        :param strength: 振动幅度：0~100 
        """

        args = []
        args.append(strength)
        command = f'signal{self.index}.set_vibration({",".join(args)})'
        self._set_command(command)

    
    def play_a_note(self, frequency, time, block = None):
        """
        设置蜂鸣器以一个固定频率发声并保持一段时间后关闭蜂鸣器

        :param frequency: 频率：20~20000 Hz 
        :param time: 时间: 50~60000 ms 
        :param block: 阻塞参数：  False表示不阻塞 True表示阻塞 
        """

        args = []
        args.append(frequency)
        args.append(time)
        if block != None:
            args.append(block)
        command = f'signal{self.index}.play_a_note({",".join(args)})'
        self._set_command(command)

    