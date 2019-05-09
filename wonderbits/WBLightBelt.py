from .wbits import Wonderbits





class LightBelt(Wonderbits):
    def __init__(self, index = 1):
        Wonderbits.__init__(self)
        self.index = index

    
    def set_leds_rgb(self, start, end, r, g, b):
        """
        设置灯带上某一段灯的颜色

        :param start: 起始位置：1~100 
        :param end: 结束位置：1~100 
        :param r: 红色：0~255 
        :param g: 绿色：0~255 
        :param b: 蓝色：0~255 
        """

        args = []
        args.append(start)
        args.append(end)
        args.append(r)
        args.append(g)
        args.append(b)
        command = f'lightBelt{self.index}.set_leds_rgb({",".join(args)})'
        self._set_command(command)

    
    def set_single_led_rgb(self, num, r, g, b):
        """
        设置灯带上某个灯的颜色

        :param num: 灯的位置：1~100 
        :param r: 红色：0~255 
        :param g: 绿色：0~255 
        :param b: 蓝色：0~255 
        """

        args = []
        args.append(num)
        args.append(r)
        args.append(g)
        args.append(b)
        command = f'lightBelt{self.index}.set_single_led_rgb({",".join(args)})'
        self._set_command(command)

    