# (C) COPYRIGHT 2024  Beijing GuangLun Electronic Technology Co., Ltd.

'''AIOE从机模块管理模块

管理所有从机模块实例以及对应的串口实例。
包括创建模块实例、获取模块实例、与从机模块握手、扫描串口等功能
'''

from typing import List, Type, TypeVar
from libraries.AIOE_base_module import AIOE_BaseModule


T = TypeVar("T", bound=AIOE_BaseModule)

class AIOE_ModuleHandler:
    '''AIOE模块管理类
    
    管理所有从机模块实例以及对应的串口实例。
    '''

    def __init__(self):
        '''初始化AIOE_ModuleHandler实例'''
        ...

    def insert_by_order(self, module_name: str, uart_id: int, baudrate: int=19200) -> None:
        '''按串口号从小到大的顺序添加从机模块

        Args:
            module_name (str): 从机模块名称
            uart_id (int): 从机模块对应的串口
            baudrate (int, optional): 从机模块的串口波特率，默认为19200

        Raises:
            ImportError: 如果找不到从机名称('module_name')对应的从机模块
            AttributeError: 如果从机模块中找不到从机名称('module_name')对应的从机类
            Exception: 如果实例化从机模块失败
            TypeError: 如果从机实例类型错误(从机实例不是AIOE_BaseModule的子类)
        '''
        ...

    def get(self, cls: Type[T]) -> T | None:
        '''获取从机模块类对应的从机模块对象

        Args:
            cls (AIOE_base_module.AIOE_BaseModule): 要获取的从机模块的类

        Returns:
            AIOE_base_module.AIOE_BaseModule | None: 返回从机模块类对应的模块实例。如果有多个相同的模块，则返回串口号最低的那个。如果没找到对应的从机模块实例(该从机模块未注册到系统中)则返回None。
        '''
        ...

    def get_all(self, cls: Type[T]) -> list[T]:
        '''获取对应类的所有从机模块对象。

        Args:
            cls (AIOE_base_module.AIOE_BaseModule): 要获取的从机模块的类

        Returns:
            list[AIOE_base_module.AIOE_BaseModule]: 返回从机模块类对应的所有模块实例，所有该类的从机模块放在一个列表中，按串口号从小到大排列。如果没找到对应的从机模块实例(该从机模块未注册到系统中)则返回空列表。
        '''
        ...

    def scan_all_uarts(self) -> None:
        '''扫描所有从机模块串口。
        
        读取所有从机模块串口数据，并调用从机模块收到数据帧后的回调。
        **该函数须在从机模块初始化并分配完串口后执行**
        '''
        ...

    def shake_hands_with_all_salve(self) -> None:
        '''与所有从机握手。
        
        逐个执行所有从机模块的握手函数。
        **该函数须在从机模块初始化并分配完串口后执行**
        '''
        ...


# 单例模式
modules: AIOE_ModuleHandler
'''AIOE从机模块管理实例'''