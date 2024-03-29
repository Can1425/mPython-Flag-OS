from mpython import *
import urequests
import Flag_OS.system.core

plugins_num = 0

while not button_a.is_pressed():
    gc.enable()
    gc.collect()
    Flag_OS.system.ui.app('Flag 线上插件')
    oled.DispChar(str('正在尝试获取应用信息'), 5, 18, 1, True)
    oled.show()
    _response = urequests.get('https://gitee.com/can1425/mPython_Flag-OS_Radient/raw/plugins/list.fos', headers={})
    plugins_list = (_response.text.split(';'))
    _response = urequests.get('https://gitee.com/can1425/mPython_Flag-OS_Radient/raw/plugins/tip.fos', headers={})
    plugins_tip = (_response.text.split(';'))
    print(len(plugins_list))
    print(plugins_tip)
    gc.collect()
    break
while not button_a.is_pressed():
    Flag_OS.system.ui.app('Flag 线上插件')
    oled.DispChar(str(('作者:' + str(plugins_tip[plugins_num]))), 5, 18, 1, True)
    oled.DispChar(str(plugins_list[plugins_num]), 5, 45, 1)
    oled.DispChar(str((''.join([str(x) for x in [plugins_num, '/', len(plugins_list)]]))), 105, 45, 1)
    oled.show()
    if touchpad_p.is_pressed() and touchpad_y.is_pressed():
        plugins_num = plugins_num - 1
        time.sleep(0.5)
    if touchpad_o.is_pressed() and touchpad_n.is_pressed():
        plugins_num = plugins_num + 1
        time.sleep(0.5)
    if plugins_num < 0:
        plugins_num = 0
        time.sleep(0.5)
    if plugins_num > len(plugins_list):
        plugins_num = len(plugins_list)
        time.sleep(0.5)
    if touchpad_t.is_pressed() and touchpad_h.is_pressed():
        Flag_OS.system.core.consani(64, 64, 0, 0, 0, 0, 128, 64)
        Flag_OS.system.core.ui_app('Flag 线上插件')
        oled.DispChar(str('请稍等，正在获取源码'), 5, 18, 1, True)
        oled.DispChar(str('如A键无法退出，重启'), 5, 45, 1, True)
        oled.show()
        _response = urequests.get((''.join([str(x) for x in ['https://gitee.com/can1425/mPython_Flag-OS_Radient/raw/plugins/Flag_plugins/', Flag_plugins_num, '.fos']])), headers={})
        Flag_OS.system.core.consani(64, 64, 0, 0, 0, 0, 128, 64)
        oled.fill(0)
        exec(_response.text)
        Flag_OS.system.core.consani(0, 0, 0, 0, 0, 0, 128, 64)