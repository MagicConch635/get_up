'''AIOE主场景模块'''

import machine
from tasks import *
from globals import *
from libraries import AIOE_application
from libraries.AIOE_module_handler import modules
from libraries.AIOE3015 import AIOE3015
from libraries.AIOE6001 import AIOE6001
from utime import localtime
from sub_scene.sub_scene_G1 import time_setting_scene, alarm_setting_scene, alarm_list_scene, alarm_ringing_scene

def initial_scene():
    '''初始场景'''
    aioe3015 = modules.get(AIOE3015)
    aioe3015.clear_screen()
    aioe3015.show_text((0, 0), "Initializing...")
    # 初始化蜂鸣器
    aioe3015.set_beep(aioe3015.SHORT_BEEP)
    # 显示初始化完成
    aioe3015.clear_screen()
    aioe3015.show_text((0, 0), "Alarm Clock")
    aioe3015.show_text((0, 2), "Press OK to start")

def main_scene():
    '''主场景'''
    aioe3015 = modules.get(AIOE3015)
    aioe6001 = modules.get(AIOE6001)
    
    # 主场景初始化
    aioe3015.clear_screen()
    aioe3015.show_time((0, 0), has_sec=True)  # 显示时间
    aioe3015.show_text((0, 2), "1:Time 2:Alarms")
    aioe3015.show_text((0, 4), "OK:Add Alarm")
    
    # 主场景循环
    while True:
        scan_in_while()
        
        # 检查是否有闹钟触发
        if check_alarm_trigger():
            alarm_ringing_scene()
            # 重置显示
            aioe3015.clear_screen()
            aioe3015.show_time((0, 0), has_sec=True)
            aioe3015.show_text((0, 2), "1:Time 2:Alarms")
            aioe3015.show_text((0, 4), "OK:Add Alarm")
        
        # 按键处理
        if aioe3015.keyval_changed:
            if aioe3015.keyval == aioe3015.KEY1:  # 时间设置
                time_setting_scene()
                aioe3015.clear_screen()
                aioe3015.show_time((0, 0), has_sec=True)
                aioe3015.show_text((0, 2), "1:Time 2:Alarms")
                aioe3015.show_text((0, 4), "OK:Add Alarm")
            elif aioe3015.keyval == aioe3015.KEY2:  # 闹钟列表
                alarm_list_scene()
                aioe3015.clear_screen()
                aioe3015.show_time((0, 0), has_sec=True)
                aioe3015.show_text((0, 2), "1:Time 2:Alarms")
                aioe3015.show_text((0, 4), "OK:Add Alarm")
            elif aioe3015.keyval == aioe3015.KEY6:  # 添加闹钟
                alarm_setting_scene()
                aioe3015.clear_screen()
                aioe3015.show_time((0, 0), has_sec=True)
                aioe3015.show_text((0, 2), "1:Time 2:Alarms")
                aioe3015.show_text((0, 4), "OK:Add Alarm")
            elif aioe3015.keyval == aioe3015.KEY5:  # ESC键停止当前闹钟
                if current_alarm:
                    stop_alarm()
                    aioe3015.set_beep(aioe3015.NOT_BEEP)
                    aioe6001.set_relay(1, False)

# 系统主程序运行
if __name__ == '__main__':
    # 系统初始化
    AIOE_application.system_init()
    # 初始化系统定时器，每1000ms执行一次GlobalTask_EventTimer_scan函数
    machine.Timer(-1).init(period=1000, mode=machine.Timer.PERIODIC, callback=GlobalTask_EventTimer_scan)
    # 初始场景
    initial_scene()
    # 主场景
    main_scene()