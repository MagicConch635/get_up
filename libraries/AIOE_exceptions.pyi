# (C) COPYRIGHT 2024  Beijing GuangLun Electronic Technology Co., Ltd.

'''AIOE异常处理模块

该模块定义了AIOE系统的各种异常，以及提供AIOE系统异常处理类的实例`sys_err`
'''

class ConnectionError(Exception):
    '''AIOE通信连接异常
    
    Attributes:
        message (str): 连接错误信息。
    '''

    def __init__(self, message: str):
        '''初始化ConnectionError实例
        
        Args:
            message (str): 连接错误信息。
        '''
        ...
    
    def __str__(self) -> str:
        '''打印ConnectionError对象。

        Returns:
            str: 连接错误信息字符串。
        '''
        ...

class MessageError(Exception):
    '''ERROR_MESSAGE错误码通信帧
    
    Attributes:
        message (str): 错误信息。
        err_function_code (int): 出现错误的请求帧功能码，取值范围为0到255。
        err_code (int): 错误码，取值范围为0到255。
    '''

    def __init__(self, message: str, err_function_code: int, err_code: int):
        '''初始化MessageError实例

        Args:
            message (str): 错误信息。
            err_function_code (int): 出现错误的请求帧功能码，取值范围为0到255(1 byte)。
            err_code (int): 错误码，取值范围为0到255(1 byte)。
        '''
        ...
    
    def __str__(self) -> str:
        '''打印MessageError对象。

        Returns:
            str: 包含错误信息、错误码、出现错误的请求帧功能码的字符串。
        '''
        ...

class SysErr:
    '''AIOE系统错误管理类

    该类用于动态保存和管理运行中出现的异常，防止运行中抛出的异常中断程序。
    '''
    
    def __init__(self):
        '''初始化SysErr实例'''
        ...
        
    def __str__(self) -> str:
        '''打印SysErr对象。

        Returns:
            str: 包含当前错误信息的字符串。
        '''
        ...

    def set_err(self, err: Exception) -> None:
        '''设置当前系统错误
        
        Args:
            err (Exception): 要设置的异常。
        '''
        ...
        
    def set_current_err_changed_callback(self, callback: callable[[Exception], None] | None) -> None:
        '''设置系统错误变化后的回调函数
        
        该方法设置的回调函数会在当前系统错误改变后立即调用

        Args:
            callback (callable[[Exception], None] | None): 要设置的回调函数(含1个Exception类型的参数，返回值为None)，设置为None表示当前系统错误改变后什么也不做。
        '''
        ...

sys_err: SysErr
'''AIOE系统错误管理实例'''

# (C) COPYRIGHT 2024  Beijing GuangLun Electronic Technology Co., Ltd.