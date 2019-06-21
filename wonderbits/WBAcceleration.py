from .wbits import Wonderbits

def _format_str_type(x):
    if isinstance(x, str):
       x = str(x).replace('"', '\\"')
       x = "\"" + x + "\""
    return x

class Acceleration(Wonderbits):
    def __init__(self, index = 1):
        Wonderbits.__init__(self)
        self.index = index

    
    def register_x_acceleration(self, cb):
        self._register_event('acceleration{}'.format(self.index), 'x_acceleration', cb)
    
    def register_y_acceleration(self, cb):
        self._register_event('acceleration{}'.format(self.index), 'y_acceleration', cb)
    
    def register_z_acceleration(self, cb):
        self._register_event('acceleration{}'.format(self.index), 'z_acceleration', cb)
    
    def register_acceleration(self, cb):
        self._register_event('acceleration{}'.format(self.index), 'acceleration', cb)
    
    def register_x_angular_velocity(self, cb):
        self._register_event('acceleration{}'.format(self.index), 'x_angular_velocity', cb)
    
    def register_y_angular_velocity(self, cb):
        self._register_event('acceleration{}'.format(self.index), 'y_angular_velocity', cb)
    
    def register_z_angular_velocity(self, cb):
        self._register_event('acceleration{}'.format(self.index), 'z_angular_velocity', cb)
    
    def get_x_acceleration(self):
        """
        获取x轴加速度值，单位m/s2:rtype: float
        """

        command = 'acceleration{}.get_x_acceleration()'.format(self.index)
        return self._get_command(command)

    
    def get_y_acceleration(self):
        """
        获取y轴加速度值，单位m/s2:rtype: float
        """

        command = 'acceleration{}.get_y_acceleration()'.format(self.index)
        return self._get_command(command)

    
    def get_z_acceleration(self):
        """
        获取z轴加速度值，单位m/s2:rtype: float
        """

        command = 'acceleration{}.get_z_acceleration()'.format(self.index)
        return self._get_command(command)

    
    def get_acceleration(self):
        """
        获取x、y、z轴合加速度值，单位m/s2:rtype: float
        """

        command = 'acceleration{}.get_acceleration()'.format(self.index)
        return self._get_command(command)

    
    def get_x_angular_velocity(self):
        """
        获取x轴角速度值，单位°/s:rtype: float
        """

        command = 'acceleration{}.get_x_angular_velocity()'.format(self.index)
        return self._get_command(command)

    
    def get_y_angular_velocity(self):
        """
        获取y轴角速度值，单位°/s:rtype: float
        """

        command = 'acceleration{}.get_y_angular_velocity()'.format(self.index)
        return self._get_command(command)

    
    def get_z_angular_velocity(self):
        """
        获取z轴角速度值，单位°/s:rtype: float
        """

        command = 'acceleration{}.get_z_angular_velocity()'.format(self.index)
        return self._get_command(command)

    
    def calibrate(self, block = None):
        """
        校准加速度传感器注意：校准过程中需确保加速度模块且保持静止不动，有汉字的一面朝上。校准时，模块指示灯会变为黄色，等待指示灯变蓝说明校准完成了。

        :param block: 阻塞参数：  False表示不阻塞 True表示阻塞
        """

        
        args = []    
        if block != None:
            args.append(str(block))
        command = 'acceleration{}.calibrate({})'.format(self.index, ",".join(args))
        self._set_command(command)

    