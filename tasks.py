'''AIOE任务模块'''

from machine import Timer
import gc
from libraries.AIOE_module_handler import modules
from libraries.AIOE3015 import AIOE3015
from libraries.AIOE6001 import AIOE6001
from utime import localtime, mktime
from globals import snooze_active, snooze_time, current_alarm, set_snooze, stop_alarm, start_alarm

def scan_in_while() -> None:
    '''系统全局任务集合函数'''
    # 所有串口通讯全局任务
    modules.scan_all_uarts()  # 扫描串口
    gc.collect()  # 内存回收

def GlobalTask_EventTimer_scan(timer: Timer) -> None:
    '''全局定时触发事件任务'''
    try:
        aioe3015 = modules.get(AIOE3015)
        aioe6001 = modules.get(AIOE6001)
        
        # 检查贪睡状态
        if snooze_active and mktime(localtime()) >= snooze_time:
            if current_alarm:
                start_alarm()
                aioe3015.set_beep(aioe3015.SPACING_BEEP)
                aioe6001.set_relay(1, True)
        
        # 检查继电器状态
        relay_state = aioe6001.get_relay(1)  # 假设使用第一个继电器
        if current_alarm and not snooze_active and relay_state:
            # 继电器信号为"是"，设置贪睡
            set_snooze()
            aioe3015.set_beep(aioe3015.NOT_BEEP)
            aioe6001.set_relay(1, False)
    except:
        # 忽略初始化期间的错误
        pass