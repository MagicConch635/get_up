'''全局变量模块'''

from utime import localtime, mktime

# 全局变量
alarms = []  # 闹钟列表
current_alarm = None  # 当前响铃的闹钟
snooze_active = False  # 是否处于贪睡状态
snooze_time = 0  # 贪睡结束时间

def check_alarm_trigger():
    '''检查是否有闹钟触发'''
    global current_alarm
    
    now = localtime()
    current_hour = now[3]
    current_minute = now[4]
    weekday = now[6]  # 0-6, 0是周一
    
    for alarm in alarms:
        if not alarm['active']:
            continue
            
        if alarm['hour'] == current_hour and alarm['minute'] == current_minute:
            # 检查重复模式
            if alarm['repeat'] == 'once':
                alarm['active'] = False
                current_alarm = alarm
                return True
            elif alarm['repeat'] == 'daily':
                current_alarm = alarm
                return True
            elif alarm['repeat'] == 'weekdays' and weekday < 5:  # 周一到周五
                current_alarm = alarm
                return True
    return False

def start_alarm():
    '''启动闹钟'''
    global snooze_active
    snooze_active = False

def stop_alarm():
    '''停止闹钟'''
    global current_alarm, snooze_active
    current_alarm = None
    snooze_active = False

def set_snooze():
    '''设置贪睡'''
    global snooze_active, snooze_time
    snooze_active = True
    snooze_time = mktime(localtime()) + 30  # 30秒后再次响铃