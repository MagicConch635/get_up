# (C) COPYRIGHT 2024  Beijing GuangLun Electronic Technology Co., Ltd.

'''AIOE系统内核模块

该模块定义了AIOE系统的功能函数，包含系统初始化等。
'''


def system_init() -> None:
    '''AIOE系统初始化函数，用于初始化整个AIOE系统，包括初始化系统配置、初始化从机模块对象、以及从机握手等
    
    Raises:
        KeyError: 如果config.json系统配置文件中，uarts列表内的串口对象的键没有完全包含'port', 'baudrate'和'model_name'三个必要的值。
        ValueError: 如果config.json系统配置文件中，uarts列表内的串口对象的串口号('port')重复，或是'port', 'baudrate'和'model_name'三个值的类型错误。
        ImportError: 如果实例化从机模块时，找不到从机名称('module_name')对应的从机模块
        AttributeError: 如果实例化从机模块时，从机模块中找不到从机名称('module_name')对应的从机类
        Exception: 如果实例化从机模块失败
        TypeError: 如果实例化从机模块时，从机实例类型错误(从机实例不是AIOE_BaseModule的子类)
    '''
    ...
