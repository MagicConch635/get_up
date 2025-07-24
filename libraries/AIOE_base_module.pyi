# (C) COPYRIGHT 2024  Beijing GuangLun Electronic Technology Co., Ltd.

'''AIOE从机类模板模块

该模块定义了AIOE从机模块的父类
'''


class AIOE_BaseModule:
    '''AIOE模块基类
    
    所有AIOE从机模块的父类

    继承自该类的AIOE从机模块必须实现:
        - MACHINE_CODE (int): 类属性，AIOE从机模块机器码

    可以选择重写的函数:
        - _handshake (function): 握手函数，系统上电后会自动执行一次握手函数，用于确认从机是否已经通过串口连接。默认情况下会发送主机的机器码和附加信息，收到从机回复的从机机器码和附加信息即为握手成功，未收到应答最多会尝试三次。
        - _frame_received_callback (function): 串口收到从机发送的一个数据帧后执行的回调函数，用于解析从机发送的数据帧。默认情况下什么也不做。

    注意: 从机模块的__init__函数需要执行父类构造函数，即`super().__init__()`

    Attributes:
        uart_id (int): 只读属性，该从机模块对应的串口id。
        _uart (UART | None): 私有属性，该从机模块对应的串口对象。
        _uart_id (int): 私有属性，该从机模块对应的串口id。
    '''

    MACHINE_CODE: int
    '''AIOE从机模块机器码'''

    def __init__(self):
        '''初始化AIOE_BaseModule实例

        Raises:
            NotImplementedError: 如果子类没有实现`MACHINE_CODE`类属性
        '''
        ...

    @property
    def uart_id(self) -> int:
        '''获取该模块对应的串口号

        Returns:
            int: 该模块对应的串口号
        '''
        ...
