# (C) COPYRIGHT 2024  Beijing GuangLun Electronic Technology Co., Ltd.

'''AIOE通信协议模块

该模块提供了AIOE通信协议对外调用接口，包括：
    - 握手帧构造和处理
    - 连续读多个字节帧构造和处理
    - 连续写多个字节帧构造和处理
    - 连续写多个字节帧构造和处理
    - 错误码帧构造和处理
    - 通用数据帧处理函数：AIOEcp_Parse_Message(message)
    - TODO：结构体直接读取，写入
    - TODO：参数有效性检查
    
注意：本版本通信数据采用大端模式。
'''

from libraries import AIOE_config


class Message:
    '''AIOE数据帧类

    该类用于封装AIOE通信协议中的数据帧。所有数据帧均包含function_code(功能码)和checksum(校验码)(对于空对象这两个参数为None)，其他属性对于不同类型的数据帧其参数内容不一样(不存在的参数为None)，参数列表如下：
        - ERR帧: function_code(功能码),err_function_code(请求错误功能码),err_code(错误码),checksum(校验码)
        - HANDSHAKE帧: function_code(功能码),machine_code(机器码),additional_information(附加信息),checksum(校验码)
        - READ_REQUEST读取请求帧: function_code(功能码),DEB_id(数据块地址),read_length(数据区字节数),checksum(校验码)
        - READ_RESPONSE读取应答帧: function_code(功能码),DEB_id(数据块地址),read_length(数据区字节数),DEB_data(数据区),checksum(校验码)
        - WRITE_REQUEST写入请求帧: function_code(功能码),DEB_id(数据块地址),read_length(数据区字节数),DEB_data(数据区),checksum(校验码)
        - WRITE_REQUEST写入应答帧: function_code(功能码),checksum(校验码)
        - 功能码不存在: 所有属性置为None (isEmpty()=True)

    Attributes:
        function_code (int | None): 功能码
        checksum (int | None): 校验码
        err_function_code (int | None): 请求错误功能码
        err_code (int | None): 错误码
        machine_code (int | None): 机器码
        additional_information (int | None): 附加信息
        DEB_id (int | None): 数据块地址
        read_length (int | None): 数据区字节数
        DEB_data (bytes | None): 数据区
    '''
    def __init__(self, function_code: int | None, checksum: int | None, err_function_code: int | None=None, err_code: int | None=None, machine_code: int | None=None, additional_information: int | None=None, DEB_id: int | None=None, read_length: int | None=None, DEB_data: bytes | None=None) -> None:
        '''初始化Message对象。

        Args:
            function_code (int | None): 功能码
            checksum (int | None): 校验码
            err_function_code (int | None, optional): 请求错误功能码。默认为None。
            err_code (int | None, optional): 错误码。默认为None。
            machine_code (int | None, optional): 机器码。默认为None。
            additional_information (int | None, optional): 附加信息。默认为None。
            DEB_id (int | None, optional): 数据块地址。默认为None。
            read_length (int | None, optional): 数据区字节数。默认为None。
            DEB_data (bytes | None, optional): 数据区。默认为None。
        '''
        ...

    def isEmpty(self) -> bool:
        '''判断该对象是否为空。

        Returns:
            bool: 如果function_code和checksum都为None，返回True；否则返回False。
        '''
        ...
        
    def __print_hex(self, obj: int | bytes) -> str:
        '''以Hex形式将int或bytes对象转为字符串。

        Args:
            obj (int | bytes): 需要转换的对象，可以是整数或字节类型。

        Returns:
            str: 转换后的十六进制字符串。
        '''
        ...
    
    def __str__(self) -> str:
        '''打印Message对象。

        Returns:
            str: 包含所有属性信息的字符串。
        '''
        ...


class FuncCodeEnum:
    '''通信帧功能码枚举
    
    Attributes:
        AIOE_FUNC_ERROR_MESSAGE_RESPONSE (int): 错误码(响应)，功能码为0x20。
        AIOE_FUNC_HANDSHAKE_REQUEST (int): 通讯握手(请求)，功能码为0x21。
        AIOE_FUNC_HANDSHAKE_RESPONSE (int): 通讯握手(响应)，功能码为0x22。
        AIOE_FUNC_READ_DEB_REQUEST (int): 读取一个数据交换缓冲区(DEB)(请求)，功能码为0x23。
        AIOE_FUNC_READ_DEB_RESPONSE (int): 读取一个数据交换缓冲区(DEB)(响应)，功能码为0x24。
        AIOE_FUNC_WRITE_DEB_NEED_RES_REQUEST (int): 写一个数据交换缓冲区DEB【须应答】(请求)，功能码为0x25。
        AIOE_FUNC_WRITE_DEB_NEED_RES_RESPONSE (int): 写一个数据交换缓冲区DEB【须应答】(响应)，功能码为0x26。
        AIOE_FUNC_WRITE_DEB_REQUEST (int): 写一个数据交换缓冲区(DEB)【无须应答】(请求)，功能码为0x27。
    '''
    # 注意：响应的功能码，都是偶数！------
    AIOE_FUNC_ERROR_MESSAGE_RESPONSE: int      =    0x20
    '''错误码 -- 响应'''

    AIOE_FUNC_HANDSHAKE_REQUEST: int           =    0x21
    '''通讯握手 -- 请求'''
    AIOE_FUNC_HANDSHAKE_RESPONSE: int          =    0x22
    '''通讯握手 -- 响应'''

    AIOE_FUNC_READ_DEB_REQUEST: int            =    0x23
    '''读取一个数据交换缓冲区(DEB) -- 请求'''
    AIOE_FUNC_READ_DEB_RESPONSE: int           =    0x24
    '''读取一个数据交换缓冲区(DEB) -- 响应'''

    AIOE_FUNC_WRITE_DEB_NEED_RES_REQUEST: int  =    0x25
    '''写一个数据交换缓冲区DEB【须应答】 -- 请求'''
    AIOE_FUNC_WRITE_DEB_NEED_RES_RESPONSE: int =    0x26
    '''写一个数据交换缓冲区DEB【须应答】 -- 响应'''

    AIOE_FUNC_WRITE_DEB_REQUEST: int           =    0x27
    '''写一个数据交换缓冲区(DEB)【无须应答】(大量使用) -- 请求'''

class AIOEcp_ErrCode:                     # TODO：ERR错误码需要分的细一点，如从机写入错误
    '''应答错误码枚举

    该类定义了AIOE通信协议中的应答错误码，每个错误码对应一个具体的错误情况。
    
    Attributes:
        AIOE_EX_NONE (int): 表示无错误.
        AIOE_EX_ILLEGAL_REQ_FRAME (int): 表示请求帧构造错误.
        AIOE_EX_CRC_ERR (int): 表示CRC校验错误.
        AIOE_EX_ERR3 (int): 用户自定义错误码.
        AIOE_EX_ERR4 (int): 用户自定义错误码.
        AIOE_EX_ERR5 (int): 用户自定义错误码.
        AIOE_EX_ERR6 (int): 用户自定义错误码.
        AIOE_EX_ERR7 (int): 用户自定义错误码.
    '''
    AIOE_EX_NONE: int = 0x00
    '''无错误'''
    AIOE_EX_ILLEGAL_REQ_FRAME: int = 0x01
    '''请求帧构造错误'''
    AIOE_EX_CRC_ERR: int = 0x02
    '''CRC校验错误'''
    AIOE_EX_ERR3: int =0x03
    '''用户自定义错误'''
    AIOE_EX_ERR4: int =0x04
    '''用户自定义错误'''
    AIOE_EX_ERR5: int =0x05
    '''用户自定义错误'''
    AIOE_EX_ERR6: int =0x06
    '''用户自定义错误'''
    AIOE_EX_ERR7: int =0x07
    '''用户自定义错误'''


def AIOEcp_Parse_Message(message: bytes) -> Message:
    '''解析bytes格式的AIOE通信协议数据帧，根据不同的功能码提取相应信息并返回Message对象。

    Args:
        message (bytes): 待解析的字节数据帧。

    Returns:
        一个Message对象，包含解析后的相关信息。具体字段取决于消息的功能码，可能包括：
            - function_code (int): 消息的功能码。
            - checksum (int): 收到的消息校验和。
            - 对于ERR帧：err_function_code (int), err_code (int)
            - 对于HANDSHAKE帧：machine_code (int), additional_information (int)
            - 对于READ_REQUEST帧：DEB_id (int), read_length (int)
            - 对于READ_RESPONSE帧：DEB_id (int), read_length (int), DEB_data (bytes)
            - 对于WRITE_REQUEST和WRITE_NEED_RES_REQUEST帧：DEB_id (int), read_length (int), DEB_data (bytes)
            - 对于WRITE_NEED_RES_RESPONSE帧：无额外字段
            - 若功能码不正确(不存在)则返回空的Message对象。

    Raises:
        ValueError: 如果消息长度不足、校验和不匹配或数据字节数与实际长度不一致。
    '''
    ...


def AIOEcp_Construct_Err_Msg(reqFuncCode: int, errCode: int) -> bytes:
    '''构造错误应答帧

    该函数用于构造一个错误应答帧，以告知请求方其发送的请求帧存在错误。

    Args:
        reqFuncCode (int): 出现错误的请求帧的功能码，取值范围为0到255。
        errCode (int): 错误码(参见AIOE_cp.AIOEcp_ErrCode定义)，用于指示具体的错误类型，取值范围为0到255。

    Returns:
        bytes: 构造好的错误应答数据帧。

    Raises:
        ValueError: 如果输入参数超出预期的取值范围。
    '''
    ...


def AIOEcp_Construct_Handshake(func_code: int, mCode: int, info: int) -> bytes:
    '''构造握手请求帧

    该函数根据给定的功能码、机器码和附加信息构建一个握手帧。

    Args:
        func_code (int): 功能码，取值必须是 AIOE_cp.FuncCodeEnum 枚举中的 AIOE_FUNC_HANDSHAKE_REQUEST 或 AIOE_FUNC_HANDSHAKE_RESPONSE，1字节。
        mCode (int): 机器码，取值范围为0到65535。
        info (int): 附加信息，取值范围为0到0xFFFFFFFF(4字节)。

    Returns:
        bytes: 构建好的握手请求或响应的数据帧。

    Raises:
        ValueError: 如果输入参数超出预期的取值范围。
    '''
    ...


def AIOEcp_Construct_Read_Request(DEB_id: int, ReadLen: int) -> bytes:
    '''构造读取请求帧。

    该函数根据给定的DEB_id和读取长度构建一个读取请求帧。

    Args:
        DEB_id (int): 要读取的数据块地址，范围为0到65535(2字节)。
        ReadLen (int): 要读取的数据块长度，范围为0到255(1字节)。

    Returns:
        bytes: 构造的读取请求数据帧。

    Raises:
        ValueError: 如果输入参数超出预期的取值范围。
    '''
    ...


def AIOEcp_Construct_Read_Response(DEB_id: int, DEB_data: bytes | None) -> bytes:
    '''构造读取应答帧。

    该函数根据给定的DEB_id和读取数据构建一个读取应答帧。

    Args:
        DEB_id (int): 读取的数据块地址，范围为0到65535(2字节)。
        DEB_data (bytes | None): 读取的数据块数据，(长度必须介于0到255之间)，如果不存在数据区，则为None。

    Returns:
        bytes: 构造的读取应答数据帧。

    Raises:
        ValueError: 如果输入参数超出预期的取值范围。
    '''
    ...


def AIOEcp_Construct_Write_Request(DEB_id: int, DEB_data: bytes | None, IfNeedResponse: bool=False) -> bytes:
    '''构造写入请求帧。

    该函数根据给定的DEB_id和数据构建一个写入请求帧。

    Args:
        DEB_id (int): 写入的数据块地址，范围为0到65535(2字节)。
        DEB_data (bytes | None): 要写入的数据块的数据，(长度必须介于0到255之间)，如果不存在数据区，则为None。
        IfNeedResponse (bool, optional): 是否需要应答，为True表示需要应答，为False表示无需应答(默认值)。

    Returns:
        bytes: 构造的写入请求帧。

    Raises:
        ValueError: 如果输入参数超出预期的取值范围。
    '''
    ...
    

def AIOEcp_Construct_Write_Response(SrcFrameBuf: bytes) -> bytes:
    '''构造写入应答帧。

    写入应答帧除了功能码和CRC校验外，其余数据与原始写入请求帧相同。

    Args:
        SrcFrameBuf (bytes): 接收到的写入请求帧。

    Returns:
        bytes: 构造的写入应答帧。
    '''
    ...


# ***** (C) COPYRIGHT 2024  Beijing GuangLun Electronic Technology Co., Ltd.****
