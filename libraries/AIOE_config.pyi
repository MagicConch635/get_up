# (C) COPYRIGHT 2024  Beijing GuangLun Electronic Technology Co., Ltd.

'''AIOE配置文件模块，初始化项目配置

该模块提供了单例模式下AIOE全局系统配置，和加载系统配置文件的接口
'''


# 常量定义
SYSTEM_CONFIG_FILE_PATH: str = './libraries/config.json'
'''AIOE系统配置文件路径'''

MODULE_FILE_PATH_PREFIX: str = 'libraries.'
'''AIOE从机模块路径前缀'''

MAINBOARD_MACHINE_CODE: int = 1101
'''2字节，AIOE主机型号机器码'''

MAINBOARD_MACHINE_INFO: int = 0x00000000
'''4字节，AIOE主机型号附加信息'''


class AIOE_CHECK_MODE:
    '''AIOE通信帧校验方式枚举类

    Attributes:
        AIOE_CHECK_NONE (int): 无校验
        AIOE_CHECK_CHECKSUM (int): 校验和(FCS)
        AIOE_CHECK_CRC (int): 循环冗余校验方式(CRC)
    '''

    AIOE_CHECK_NONE: int     =    0
    '''无校验'''
    AIOE_CHECK_CHECKSUM: int =    1
    '''校验和(FCS)'''
    AIOE_CHECK_CRC: int      =    2
    '''循环冗余校验方式(CRC)'''


class UartConfig:
    '''AIOE串口配置类
    
    Attributes:
        port (int): 只读属性，串口id
        baudrate (int): 只读属性，串口波特率
        model_name (str): 只读属性，串口对应的从机模块名称
    '''
    
    def __init__(self, port: int, baudrate: int, model_name: str):
        '''初始化UartConfig实例
        
        Args:
            port (int): 串口id
            baudrate (int): 串口波特率
            model_name (str): 串口对应的从机模块名称
        '''
        ...
        
    @property
    def port(self) -> int:
        '''获取串口号

        Returns:
            int: 串口号
        '''
        ...
        
    @property
    def baudrate(self) -> int:
        '''获取波特率

        Returns:
            int: 波特率
        '''
        ...
        
    @property
    def model_name(self) -> str:
        '''获取该串口对应的从机模块名称

        Returns:
            str: 该串口对应的从机模块名称
        '''
        ...

    def __str__(self) -> str:
        '''获取该data类的字符串形式

        Returns:
            str: 该data类的字符串形式
        '''
        ...
        
        
class SystemConfig:
    '''AIOE系统配置类
    
    Attributes:
        AIOE_CHECK_MODE (int): 只读属性，AIOE通信帧校验方式
        MAX_SERIAL_NUM (int): 只读属性，本AIOE主机最大串口数
        uarts (list[UartConfig]): 只读属性，本主机所有串口配置类列表
    '''
    
    def __init__(self, aioe_check_mode: int, max_serial_num: int, uarts: list[UartConfig]):
        '''初始化SystemConfig实例
        
        Args:
            aioe_check_mode (int): AIOE通信帧校验方式
            max_serial_num (int): 本AIOE主机最大串口数
            uarts (list[UartConfig]): 本主机所有串口配置类列表
        '''
        ...
        
    @property
    def AIOE_CHECK_MODE(self) -> int:
        '''获取AIOE通信帧校验方式

        Returns:
            int: AIOE通信帧校验方式(见libraries.AIOE_config.AIOE_CHECK_MODE)
        '''
        ...
        
    @property
    def MAX_SERIAL_NUM(self) -> int:
        '''获取本AIOE主机最大串口数

        Returns:
            int: 本AIOE主机最大串口数
        '''
        ...
    
    @property
    def uarts(self) -> list[UartConfig]:
        '''获取本主机所有串口配置类列表

        Returns:
            list[UartConfig]: 本主机所有串口配置类列表
        '''
        ...

    def __str__(self) -> str:
        '''获取该data类的字符串形式

        Returns:
            str: 该data类的字符串形式
        '''
        ...
        

def load_system_config(system_config_file_path: str) -> SystemConfig:
    '''加载AIOE系统配置
    Args:
        system_config_file_path (str): AIOE系统配置json文件路径

    Returns:
        libraries.AIOE_config.SystemConfig: 返回加载完配置的SystemConfig系统配置类

    Raises:
        KeyError: 如果config.json系统配置文件中，uarts列表内的串口对象的键没有完全包含'port', 'baudrate'和'model_name'三个必要的值。
        ValueError: 如果config.json系统配置文件中，uarts列表内的串口对象的串口号('port')重复，或是'port', 'baudrate'和'model_name'三个值的类型错误。
    '''
    ...

    
# 单例模式，如果未加载配置或加载配置失败则为默认配置
system_config: SystemConfig
'''AIOE系统配置'''