# (C) COPYRIGHT 2024  Beijing GuangLun Electronic Technology Co., Ltd.

'''AIOE6001 4路继电器模块

该从机模块包含控制AIOE6001的4个继电器打开、关闭等功能。
'''

from libraries.AIOE_base_module import AIOE_BaseModule


class AIOE6001(AIOE_BaseModule):
    '''AIOE6001: 4路继电器模块从机类。继承自 AIOE_BaseModule。

    该类包含控制AIOE6001的4个继电器打开、关闭等功能。

    Attributes:
        MACHINE_CODE (int): AIOE6001模块机器码。
    '''

    MACHINE_CODE: int = 6001
    '''AIOE模块机器码'''

    def __init__(self) -> None:
        '''初始化AIOE6001实例'''
        ...

    def set_relay(self, relay_id: int, onoff: bool) -> None:
        '''设置单个继电器状态

        Args:
            relay_id (int): 继电器编号，范围为1到4。
            onoff (bool): 继电器开关状态，True为闭合继电器，False为断开继电器。
        '''
        ...

    def set_all_relay(self, onoff: bool) -> None:
        '''设置全部继电器状态

        Args:
            onoff (bool): 继电器开关状态，True为闭合继电器，False为断开继电器。
        '''
        ...

    def toggle_relay(self, relay_id: int) -> None:
        '''翻转单个继电器状态

        Args:
            relay_id (int): 继电器编号，范围为1到4。
        '''
        ...
        