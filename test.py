# from wonderbits import Display, Control, Led, wb_tool
# import time
# import random


# # 初始化模块
# d1 = Display()
# c1 = Control()
# l1 = Led()



# wb_tool.show_console()

# # 显示模块显示内容
# d1.print(2, 1, 'value:')

# # 计数变量
# count = 1

# for i in range(100):
#     # 获取控制模块开关sw4的值
#     sw4 = c1.get_sw4()
#     # 在显示屏上显示sw4的值
#     d1.print(2, 7, sw4)
#     # 设置彩灯rbg随机颜色
#     l1.set_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

#     # 显示模块显示计数值 
#     d1.print(1, 1, count)
#     # 将计数变量 递增1
#     count += 1

from wonderbits import wb_tool

# 方式一：通过文件上传
# wb_tool.upload.upload_with_file_path('/Users/daejong/Desktop/python-sdk/upload.py')

# 方式二：通过指定文件内容上传
content = '''
d = Display()
for i in range(10000):
    d.print(1, 1, i)
'''
wb_tool.upload.upload_with_file_content(content)

# import time
# d = Display()

# start_time = time.time();
# for i in range(100):
#     d.print(1, 1, i)
# print(time.time() - start_time);