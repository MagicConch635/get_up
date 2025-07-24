'''一级子场景模块'''

from libraries.AIOE_module_handler import modules
from libraries.AIOE3015 import AIOE3015
from utime import localtime
from globals import alarms, current_alarm, stop_alarm

def time_setting_scene():
    '''时间设置场景'''
    aioe3015 = modules.get(AIOE3015)
    
    # 场景初始化
    aioe3015.clear_screen()
    aioe3015.show_text((0, 0), "Set Time:")
    aioe3015.show_text((0, 2), "Press OK to edit")
    aioe3015.show_text((0, 6), "ESC:Back")
    
    # 场景循环
    while True:
        scan_in_while()
        
        if aioe3015.keyval_changed:
            if aioe3015.keyval == aioe3015.KEY6:  # OK键
                aioe3015.set_date_time_manually()
                return
            elif aioe3015.keyval == aioe3015.KEY5:  # ESC键
                return

def alarm_setting_scene():
    '''闹钟设置场景'''
    aioe3015 = modules.get(AIOE3015)
    new_alarm = {
        'hour': 7,
        'minute': 0,
        'repeat': 'once',  # 'once', 'daily', 'weekdays'
        'active': True
    }
    
    # 场景初始化
    aioe3015.clear_screen()
    aioe3015.show_text((0, 0), "New Alarm:")
    aioe3015.show_text((0, 2), f"Time: {new_alarm['hour']:02d}:{new_alarm['minute']:02d}")
    aioe3015.show_text((0, 4), f"Repeat: {new_alarm['repeat']}")
    aioe3015.show_text((0, 6), "OK:Save ESC:Cancel")
    
    # 场景循环
    while True:
        scan_in_while()
        
        if aioe3015.keyval_changed:
            if aioe3015.keyval == aioe3015.KEY6:  # OK键
                def set_time_callback(h, m):
                    new_alarm['hour'] = h
                    new_alarm['minute'] = m
                    aioe3015.clear_screen()
                    aioe3015.show_text((0, 0), "New Alarm:")
                    aioe3015.show_text((0, 2), f"Time: {h:02d}:{m:02d}")
                    aioe3015.show_text((0, 4), f"Repeat: {new_alarm['repeat']}")
                    aioe3015.show_text((0, 6), "OK:Save ESC:Cancel")
                
                aioe3015.set_HHMM_manually((0, 2), (new_alarm['hour'], new_alarm['minute']), set_time_callback)
            elif aioe3015.keyval == aioe3015.KEY1:  # KEY1切换重复模式
                if new_alarm['repeat'] == 'once':
                    new_alarm['repeat'] = 'daily'
                elif new_alarm['repeat'] == 'daily':
                    new_alarm['repeat'] = 'weekdays'
                else:
                    new_alarm['repeat'] = 'once'
                aioe3015.show_text((0, 4), f"Repeat: {new_alarm['repeat']}")
            elif aioe3015.keyval == aioe3015.KEY5:  # ESC键取消
                return
            elif aioe3015.keyval == aioe3015.KEY4:  # KEY4保存
                alarms.append(new_alarm)
                aioe3015.set_beep(aioe3015.SHORT_BEEP)
                return

def alarm_list_scene():
    '''闹钟列表场景'''
    aioe3015 = modules.get(AIOE3015)
    current_index = 0
    
    # 场景初始化
    display_alarm_list(current_index)
    
    # 场景循环
    while True:
        scan_in_while()
        
        if aioe3015.keyval_changed:
            if aioe3015.keyval == aioe3015.KEY_UP:  # 上移
                if current_index > 0:
                    current_index -= 1
                    display_alarm_list(current_index)
            elif aioe3015.keyval == aioe3015.KEY_DOWN:  # 下移
                if current_index < len(alarms) - 1:
                    current_index += 1
                    display_alarm_list(current_index)
            elif aioe3015.keyval == aioe3015.KEY6:  # OK键编辑
                if alarms:
                    edit_alarm(current_index)
                    display_alarm_list(current_index)
            elif aioe3015.keyval == aioe3015.KEY5:  # ESC键返回
                return

def display_alarm_list(selected_index):
    '''显示闹钟列表'''
    aioe3015 = modules.get(AIOE3015)
    aioe3015.clear_screen()
    aioe3015.show_text((0, 0), "Alarm List:")
    
    if not alarms:
        aioe3015.show_text((0, 2), "No alarms")
        aioe3015.show_text((0, 6), "ESC:Back")
        return
    
    start_idx = max(0, selected_index - 1)
    end_idx = min(len(alarms), start_idx + 3)
    
    for i in range(start_idx, end_idx):
        alarm = alarms[i]
        y_pos = 2 + (i - start_idx) * 2
        prefix = ">" if i == selected_index else " "
        aioe3015.show_text((0, y_pos), f"{prefix}{alarm['hour']:02d}:{alarm['minute']:02d} {alarm['repeat']}")
    
    aioe3015.show_text((0, 6), "OK:Edit ESC:Back")

def edit_alarm(index):
    '''编辑闹钟'''
    aioe3015 = modules.get(AIOE3015)
    alarm = alarms[index]
    
    # 场景初始化
    aioe3015.clear_screen()
    aioe3015.show_text((0, 0), f"Edit Alarm {index+1}:")
    aioe3015.show_text((0, 2), f"Time: {alarm['hour']:02d}:{alarm['minute']:02d}")
    aioe3015.show_text((0, 4), f"Repeat: {alarm['repeat']}")
    aioe3015.show_text((0, 6), "1:Del 4:Save ESC:Back")
    
    # 场景循环
    while True:
        scan_in_while()
        
        if aioe3015.keyval_changed:
            if aioe3015.keyval == aioe3015.KEY1:  # 删除
                del alarms[index]
                aioe3015.set_beep(aioe3015.SHORT_BEEP)
                return
            elif aioe3015.keyval == aioe3015.KEY6:  # OK键编辑时间
                def set_time_callback(h, m):
                    alarm['hour'] = h
                    alarm['minute'] = m
                    aioe3015.clear_screen()
                    aioe3015.show_text((0, 0), f"Edit Alarm {index+1}:")
                    aioe3015.show_text((0, 2), f"Time: {h:02d}:{m:02d}")
                    aioe3015.show_text((0, 4), f"Repeat: {alarm['repeat']}")
                    aioe3015.show_text((0, 6), "1:Del 4:Save ESC:Back")
                
                aioe3015.set_HHMM_manually((0, 2), (alarm['hour'], alarm['minute']), set_time_callback)
            elif aioe3015.keyval == aioe3015.KEY2:  # KEY2切换重复模式
                if alarm['repeat'] == 'once':
                    alarm['repeat'] = 'daily'
                elif alarm['repeat'] == 'daily':
                    alarm['repeat'] = 'weekdays'
                else:
                    alarm['repeat'] = 'once'
                aioe3015.show_text((0, 4), f"Repeat: {alarm['repeat']}")
            elif aioe3015.keyval == aioe3015.KEY4:  # KEY4保存
                aioe3015.set_beep(aioe3015.SHORT_BEEP)
                return
            elif aioe3015.keyval == aioe3015.KEY5:  # ESC键返回
                return

def alarm_ringing_scene():
    '''闹钟响铃场景'''
    aioe3015 = modules.get(AIOE3015)
    aioe6001 = modules.get(AIOE6001)
    
    # 场景初始化
    aioe3015.clear_screen()
    aioe3015.show_text((0, 0), "ALARM!")
    aioe3015.show_text((0, 2), f"{current_alarm['hour']:02d}:{current_alarm['minute']:02d}")
    aioe3015.show_text((0, 4), "Press OK to stop")
    
    # 启动响铃/震动
    aioe3015.set_beep(aioe3015.SPACING_BEEP)
    aioe6001.set_relay(1, True)  # 假设继电器1控制震动
    
    # 场景循环
    while True:
        scan_in_while()
        
        if aioe3015.keyval_changed:
            if aioe3015.keyval == aioe3015.KEY6:  # OK键停止
                stop_alarm()
                aioe3015.set_beep(aioe3015.NOT_BEEP)
                aioe6001.set_relay(1, False)
                return