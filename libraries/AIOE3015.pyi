# (C) COPYRIGHT 2024  Beijing GuangLun Electronic Technology Co., Ltd.

'''AIOE3015: 12864LCD 人机交互模块

该从机模块包含128*64LCD屏显示功能，以及6个按键控制功能。
'''

from libraries.AIOE_base_module import AIOE_BaseModule


class AIOE3015(AIOE_BaseModule):
    '''AIOE3015: 12864LCD 人机交互模块从机类。继承自 AIOE_BaseModule。

    该类包含128*64LCD屏显示功能，以及6个按键控制功能。

    Attributes:
        MACHINE_CODE (int): AIOE3015模块机器码。

        KEY1 (int): 按键1编号
        KEY2 (int): 按键2编号
        KEY3 (int): 按键3编号
        KEY4 (int): 按键4编号
        KEY5 (int): 按键5编号
        KEY6 (int): 按键6编号

        KEY_UP (int): 复用按键上编号
        KEY_DOWN (int): 复用按键下编号
        KEY_LEFT (int): 复用按键左编号
        KEY_RIGHT (int): 复用按键右编号
        KEY_ESC (int): 复用按键ESC编号
        KEY_OK (int): 复用按键OK编号

        NOT_BEEP (int): 蜂鸣器状态枚举: 关闭
        LONG_BEEP (int): 蜂鸣器状态枚举: 长鸣一声
        SHORT_BEEP (int): 蜂鸣器状态枚举: 短鸣一声
        SPACING_BEEP (int): 蜂鸣器状态枚举: 间隔短鸣

        keyval (int): 只读属性，获取按键短按触发状态。为KEY1表示按键1短按，为KEY2表示按键2短按，为KEY3表示按键3短按，为KEY4表示按键4短按，为KEY5表示按键5短按，为KEY6表示按键6短按。支持辨别双键同时短按，例如 KEY1 | KEY2 表示同时短按KEY1和KEY2按键。
        longkeyval (int): 只读属性，获取按键长按触发状态。为KEY1表示按键1长按，为KEY2表示按键2长按，为KEY3表示按键3长按，为KEY4表示按键4长按，为KEY5表示按键5长按，为KEY6表示按键6长按。支持辨别双键同时长按，例如 KEY1 | KEY2 表示同时长按KEY1和KEY2按键。
        keyval_changed (bool): 只读属性，获取模块按键触发状态是否变化。若keyval或longkeyval变化了则为True，**读取该值后该值会置为False。**

        on_function_call (bool): 只读属性，表示从机是否处于内置功能调用状态。**注意：若该值为True则请勿用代码操作显示屏。**
        date_time (tuple[int, ...]): 只读属性，获取从机时钟时间，该值为7参数元组，其中包含：(year(ex:2014), month(1-12), mday(1-31), hour(0-23), minute(0-59), second(0-59), weekday(0-6))
    '''
    MACHINE_CODE: int = 3015
    '''AIOE模块机器码'''

    KEY1: int = 0x01
    '''按键1编号'''
    KEY2: int = 0x08
    '''按键2编号'''
    KEY3: int = 0x02
    '''按键3编号'''
    KEY4: int = 0x10
    '''按键4编号'''
    KEY5: int = 0x04
    '''按键5编号'''
    KEY6: int = 0x20
    '''按键6编号'''
    
    KEY_UP: int    = KEY1
    '''复用按键上编号'''
    KEY_DOWN: int  = KEY2
    '''复用按键下编号'''
    KEY_LEFT: int  = KEY3
    '''复用按键左编号'''
    KEY_RIGHT: int = KEY4
    '''复用按键右编号'''
    KEY_ESC: int   = KEY5
    '''复用按键ESC编号'''
    KEY_OK: int    = KEY6
    '''复用按键OK编号'''
    
    NOT_BEEP: int = 0
    '''蜂鸣器状态: 关闭'''
    LONG_BEEP: int = 1
    '''蜂鸣器状态: 长鸣一声'''
    SHORT_BEEP: int = 2
    '''蜂鸣器状态: 短鸣一声'''
    SPACING_BEEP: int = 3
    '''蜂鸣器状态: 间隔短鸣'''

    def __init__(self) -> None:
        '''初始化AIOE3015实例'''
        ...


    @property
    def keyval(self) -> int:
        '''获取按键短按触发状态。

        为KEY1表示按键1短按，为KEY2表示按键2短按，为KEY3表示按键3短按，为KEY4表示按键4短按，为KEY5表示按键5短按，为KEY6表示按键6短按。支持辨别双键同时短按，例如 KEY1 | KEY2 表示同时短按KEY1和KEY2按键。

        Returns:
            int: 按键短按触发状态。
        '''
        ...
    
    @property
    def longkeyval(self) -> int:
        '''获取按键长按触发状态。

        为KEY1表示按键1长按，为KEY2表示按键2长按，为KEY3表示按键3长按，为KEY4表示按键4长按，为KEY5表示按键5长按，为KEY6表示按键6长按。支持辨别双键同时长按，例如 KEY1 | KEY2 表示同时长按KEY1和KEY2按键。

        Returns:
            int: 按键长按触发状态。
        '''
        ...

    @property
    def keyval_changed(self) -> bool:
        '''获取模块按键触发状态是否变化。

        若keyval或longkeyval变化了则为True，**读取该值后该值会置为False。**

        Returns:
            bool: 按键触发状态是否变化。

        Examples:
            在场景循环或全局任务扫描（scan_in_while）中扫描keyval_changed的值以判断按键是否按下：
            ```python
            def main_scene():
                # 主场景初始化
                aioe3015 = modules.get(AIOE3015)
                # 主场景循环
                while True:
                    # 全局任务扫描：每个场景必配
                    scan_in_while()
                    if(aioe3015.keyval_changed):
                        if aioe3015.keyval == aioe3015.KEY1:
                            pass  # 按键1按下后处理的内容
                        elif aioe3015.keyval == aioe3015.KEY2:
                            pass  # 按键2按下后处理的内容
                        elif aioe3015.keyval == aioe3015.KEY3:
                            pass  # 按键3按下后处理的内容
                        elif aioe3015.keyval == aioe3015.KEY4:
                            pass  # 按键4按下后处理的内容
                        elif aioe3015.keyval == aioe3015.KEY5:
                            pass  # 按键5按下后处理的内容
                        elif aioe3015.keyval == aioe3015.KEY6:
                            pass  # 按键6按下后处理的内容
                        elif aioe3015.keyval == aioe3015.KEY1 | aioe3015.KEY2:
                            pass  # 按键1和按键2同时按下后处理的内容
            ```
        '''
        ...

    @property
    def on_function_call(self) -> bool:
        '''表示从机是否处于内置功能调用状态。

        **注意：若该值为True则请勿用代码操作显示屏。**

        Returns:
            bool: 从机是否处于内置功能调用状态。
        '''
        ...
    
    @property
    def date_time(self) -> tuple[int, ...]:
        '''获取从机时钟时间
        
        Returns:
            tuple[int, ...]: 从机时钟时间。该值为7参数元组，其中包含：(year(ex:2014), month(1-12), mday(1-31), hour(0-23), minute(0-59), second(0-59), weekday(0-6))
        '''
        ...
    

    def set_beep(self, beep_type: int) -> None:
        '''设置蜂鸣器动作状态

        Args:
            beep_type (int): 蜂鸣器工作状态，可能的值范围为[0, 3]。其中: NOT_BEEP(即0)表示关闭蜂鸣器，LONG_BEEP(即1)表示蜂鸣器长鸣一声，SHORT_BEEP(即2)表示蜂鸣器短鸣一声，SPACING_BEEP(即3)表示蜂鸣器间隔短鸣。

        Raises:
            ValueError: 如果beep_type值超出范围[0, 3]
        '''
        ...


    def set_led(self, led_id:int, onoff:bool) -> None:
        '''设置led指示灯亮灭状态

        Args:
            led_id (int): led指示灯编号，可能的值范围为2和3。
            onoff (bool): led指示灯亮灭状态，True为点亮led指示灯，False为熄灭led指示灯。

        Raises:
            ValueError: 如果led_id值超出范围[2, 3]
        '''
        ...
        
    def toggle_led(self, led_id:int) -> None:
        '''翻转单个led指示灯状态

        Args:
            led_id (int): led指示灯编号，可能的值范围为2和3。

        Raises:
            ValueError: 如果led_id值超出范围[2, 3]
        '''
        ...
        
    def modify_datetime(self, date_time:tuple[int, ...]) -> None:
        '''修改该模块时钟芯片的时间值。

        Args:
            date_time (tuple[int, ...]): 时间值，7参数元组，其中包含：(year(ex:2014), month(1-12), mday(1-31), hour(0-23), minute(0-59), second(0-59), weekday(0-6))

        Raises:
            ValueError: 如果date_time[0]值超出范围[2000, 2099]，或date_time[1]值超出范围[1, 12]，或date_time[2]值超出范围[1, 31]，或date_time[3]值超出范围[0, 23]，或date_time[4]值超出范围[0, 59]，或date_time[5]值超出范围[0, 59]，或date_time[6]值超出范围[0, 6]

        Examples:
            可通过micropython标准库utime.localtime([secs])生成时间元组，如：`aioe3015.modify_datetime(utime.localtime())`表示设置该模块时钟芯片的时间值为当前时间。
        '''
        ...
        
    def clear_screen(self, isBlack:bool=False) -> None:
        '''显示屏清屏

        Args:
            isBlack (bool): 表示是否用黑色清屏。为True表示用黑色填充整个屏幕，为False表示将整个屏幕清空为白色。
        '''
        ...
        
    def clear_row(self, row_num:int, isBlack:bool=False) -> None:
        '''显示屏清空一行

        注意：一个字符占2行，因此若要清除一行字符串，需要清空两行

        Args:
            row_num (int): 要清空的行号，范围[0, 7]。
            isBlack (bool): 表示是否用黑色清空一行。为True表示用黑色填充该行，为False表示将该行清空为白色。
        '''
        ...
        
    def show_text(self, posi:tuple[int, int], text:str, reverse:bool=False) -> None:
        '''在显示屏上显示字符串，一行最多显示16个ASCII字符。

        注意：一个字符占2行

        Args:
            posi (tuple[int, int]): 显示位置起点坐标(x,y)，其中x范围[0, 15], y范围[0, 7]。
            text (str): 要显示的字符串。
            reverse (bool): 表示是否反显文本。为True表示反显文本，为False表示不反显文本。

        Raises:
            ValueError: 如果posi[0]值超出范围[0, 15]，或posi[1]值超出范围[0, 7]
        '''
        ...
        
    def show_date(self, posi:tuple[int, int], reverse:bool=False, erase:bool=False) -> None:
        '''在显示屏指定位置显示或擦除该模块当前日期，格式为：20xx-xx-xx。

        注意：每次调用该函数会重新显示最新的当前日期，建议把该函数放到GlobalTask_EventTimer_scan中，每隔固定时间调用一次。显示一个字符占2行。
        注意：同一时间只能同时显示一个日期值，若要修改显示位置则需要先关闭上一个位置显示的日期值，例如关闭上一个位置显示的日期值:`aioe3015.show_date((1,1), erase=True)`

        Args:
            posi (tuple[int, int]): 显示位置起点坐标(x,y)，其中x范围[0, 15], y范围[0, 7]。
            reverse (bool): 表示是否反显文本。为True表示反显文本，为False表示不反显文本。
            erase (bool): 表示是开启显示日期还是关闭显示日期。为True表示关闭该位置显示的日期，为False表示在该位置显示日期。

        Raises:
            ValueError: 如果posi[0]值超出范围[0, 15]，或posi[1]值超出范围[0, 7]
        '''
        ...
    
    def show_time(self, posi:tuple[int, int], has_sec:bool=True, reverse:bool=False, erase:bool=False) -> None:
        '''在显示屏指定位置显示或擦除从机当前时间，格式：xx:xx[:xx]。

        注意：每次调用该函数会重新显示最新的当前时间，建议把该函数放到GlobalTask_EventTimer_scan中，每隔固定时间调用一次。显示一个字符占2行。
        注意：同一时间只能同时显示一个时间值，若要修改显示位置则需要先关闭上一个位置显示的时间值，例如关闭上一个位置显示的时间值:`aioe3015.show_time((1,1), erase=True)`

        Args:
            posi (tuple[int, int]): 显示位置起点坐标(x,y)，其中x范围[0, 15], y范围[0, 7]。
            has_sec (bool): 指示显示内容是否包含秒。为True表示显示时分秒，为False表示显示时分（不显示秒）。
            reverse (bool): 表示是否反显文本。为True表示反显文本，为False表示不反显文本。
            erase (bool): 表示是擦除时间还是显示时间。为True表示擦除该位置时间，为False表示在该位置显示时间。

        Raises:
            ValueError: 如果posi[0]值超出范围[0, 15]，或posi[1]值超出范围[0, 7]
        '''
        ...
      
    def show_bmp(self, posi:tuple[int, int], bmp_num:int, reverse:bool=False) -> None:
        '''在显示屏指定位置显示bmp图片。

        注意：目前只支持部分已导入的图片，参见说明书。

        Args:
            posi (tuple[int, int]): 显示位置起点坐标(x,y)，其中x范围[0, 15], y范围[0, 7]。
            bmp_num (int): 要显示的bmp图片编号。
            reverse (bool): 表示是否反显图片。为True表示反显图片，为False表示不反显图片。

        Raises:
            ValueError: 如果posi[0]值超出范围[0, 15]，或posi[1]值超出范围[0, 7]
        '''
        ...
    
    def show_chinese(self, posi:tuple[int, int], chinese_num:int, reverse:bool=False):
        '''在显示屏指定位置显示一个16*16点阵汉字（一个汉字占2行）。

        注意：目前只支持部分已导入的中文，参见说明书。

        Args:
            posi (tuple[int, int]): 显示位置起点坐标(x,y)，其中x范围[0, 15], y范围[0, 7]。
            chinese_num (int): 要显示的中文编号。
            reverse (bool): 表示是否反显文本。为True表示反显文本，为False表示不反显文本。

        Raises:
            ValueError: 如果posi[0]值超出范围[0, 15]，或posi[1]值超出范围[0, 7]
        '''
        ...
    
    def set_date_time_manually(self, callback: callable | None=None):
        '''调用从机的“手动输入时间”功能。

        此时用户可以通过AIOE3015从机上的按键来修改AIOE3015内部时钟芯片的时间值。
        注意：调用该函数系统会自动设置on_function_call的值为True，关闭“手动输入时间功能”时该值会被置为False。
        注意：在用户输入期间，应当禁止对AIOE3015显示屏上的一切操作（例如清屏，显示字符串等等），待用户输入完毕后（用户输入完毕后从机会自动更新on_function_call的值为False，通过扫描该值来判断用户是否完成输入）才可操作AIOE3015显示屏。
        
        Args:
            callback (callable | None): 本次用户“手动输入时间”事件完成后执行的回调函数，具有0个参数。

        Examples:
            在场景循环或全局任务扫描（scan_in_while）中扫描on_function_call的值并根据用户输入状态执行代码：
            ```python
            if not aioe3015.on_function_call:  # 表示用户输入完毕
                # 操作显示屏或其他关于显示屏的操作
            ```
        '''
        ...
        
    def set_HHMM_manually(self, posi:tuple[int, int], init_time:tuple[int, int], callback: callable[[int, int], None] | None=None):
        '''调用从机的“手动输入时:分”功能。
        
        此时用户可以通过AIOE3015从机上的按键来输入一个“时：分”的时间值。用户输入完毕后会调用callback，用户输入结果会以参数形式传入callback中
        注意：调用该函数系统会自动设置on_function_call的值为True，关闭“手动输入时:分”时该值会被置为False。
        注意：在用户输入期间，应当禁止对AIOE3015显示屏上的一切操作（例如清屏，显示字符串等等），待用户输入完毕后（用户输入完毕后从机会自动更新on_function_call的值为False，通过扫描该值来判断用户是否完成输入）才可操作AIOE3015显示屏。
        
        Args:
            posi (tuple[int, int]): 显示输入框起点坐标(x,y)，其中x范围[0, 15], y范围[0, 7]。
            init_time (tuple[int, int]): 输入框中显示的初始时间。
            callback (callable[[int, int], None] | None): 本次用户“手动输入时:分”事件完成后执行的回调函数。该函数应有2个参数，参数1：int 表示用户输入的“时”；参数2：int 表示用户输入的“分”

        Raises:
            ValueError: 如果posi[0]值超出范围[0, 15]，或posi[1]值超出范围[0, 7]，或init_time[0]值超出范围[0, 23]，或init_time[1]值超出范围[0, 59]

        Examples:
            在场景循环或全局任务扫描（scan_in_while）中扫描on_function_call的值并根据用户输入状态执行代码：
            ```python
            if not aioe3015.on_function_call:  # 表示用户输入完毕
                # 操作显示屏或其他关于显示屏的操作
            ```
        '''
        ...
        
    def input_digit_manually(self, posi:tuple[int, int], init_num:int | float, callback=None):
        '''调用从机的“手动输入实数”功能。
        
        此时用户可以通过AIOE3015从机上的按键来输入一个实数值。用户输入完毕后会调用callback，用户输入结果会以参数形式传入callback中
        注意：调用该函数系统会自动设置on_function_call的值为True，关闭“手动输入时:分”时该值会被置为False。
        注意：在用户输入期间，应当禁止对AIOE3015显示屏上的一切操作（例如清屏，显示字符串等等），待用户输入完毕后（用户输入完毕后从机会自动更新on_function_call的值为False，通过扫描该值来判断用户是否完成输入）才可操作AIOE3015显示屏。
        
        Args:
            posi (tuple[int, int]): 显示输入框起点坐标(x,y)，其中x范围[0, 15], y范围[0, 7]。
            init_num (int | float): 输入框中显示的初始值。
            callback (callable[[str], None] | None): 本次用户“手动输入实数”事件完成后执行的回调函数。该函数应有1个参数，参数1：str 表示用户输入的实数的字符串形式

        Raises:
            ValueError: 如果posi[0]值超出范围[0, 15]，或posi[1]值超出范围[0, 7]，或init_num不为int或float

        Examples:
            在场景循环或全局任务扫描（scan_in_while）中扫描on_function_call的值并根据用户输入状态执行代码：
            ```python
            if not aioe3015.on_function_call:  # 表示用户输入完毕
                # 操作显示屏或其他关于显示屏的操作
            ```
        '''
        ...
        

    def set_keypress_callback(self, callback:callable[[int, int],None] | None):
        '''设置按键短按后触发的回调函数。

        该函数只用在初始化中设置一次，只要按键按下可以一直触发。
        
        Args:
            callback (callable[[int, int],None] | None): 按键短按后触发的回调函数。该函数应有2个参数，参数1：int 按键短按状态值；参数2：int 按键长按状态值；可选的参数值有：KEY1表示按键1按下，KEY2表示按键2按下，KEY3表示按键3按下，KEY4表示按键4按下，KEY5表示按键5按下，KEY6表示按键6按下。支持辨别双键同时按下，例如 KEY1 | KEY2 表示同时按下KEY1和KEY2按键。

        Examples:
            在场景循环或全局任务扫描（scan_in_while）中扫描on_function_call的值并根据用户输入状态执行代码：
            ```python

            ...
            # 在场景初始化中
            aioe3015.set_keypress_callback(on_keypress)

            ...

            def on_keypress(keyval: int, longkeyval: int) -> None:
                aioe3015 = modules.get(AIOE3015)
                if keyval == aioe3015.KEY1:
                    pass  # 按键1按下后处理的内容
                elif keyval == aioe3015.KEY2:
                    pass  # 按键2按下后处理的内容
                elif keyval == aioe3015.KEY3:
                    pass  # 按键3按下后处理的内容
                elif keyval == aioe3015.KEY4:
                    pass  # 按键4按下后处理的内容
                elif keyval == aioe3015.KEY5:
                    pass  # 按键5按下后处理的内容
                elif keyval == aioe3015.KEY6:
                    pass  # 按键6按下后处理的内容
                elif keyval == aioe3015.KEY1 | aioe3015.KEY2:
                    pass  # 按键1和按键2同时按下后处理的内容
            ```
        '''
        ...
