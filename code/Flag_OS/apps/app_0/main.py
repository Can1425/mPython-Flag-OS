from mpython import *
import Flag_OS.system.core as core
import Flag_OS.system.ui as ui
import Flag_OS.apps.app_0 as core
import Flag_OS.system.pages as pages

time.sleep_ms(5)
settings_list = ['重连网络', '同步时间', '清理内存', '系统信息', '- Flag OS -', '- End -', ' ']
settings_num = 0
while not button_a.is_pressed():
    if touchpad_o.is_pressed() and touchpad_n.is_pressed():
        settings_num = settings_num + 1
        if settings_num > len(settings_list) - 3:
            settings_num = len(settings_list) - 3
    if touchpad_p.is_pressed() and touchpad_y.is_pressed():
        settings_num = settings_num + -1
        if settings_num < 1:
            settings_num = 1
    Flag_OS.system.ui.app("Setting")
    oled.DispChar(str('暂无简介'), 5, 18, 1, True)
    oled.DispChar(str(settings_list[settings_num]), 5, 45, 1)
    oled.DispChar(''.join([settings_num,'/',settings_list]), 105, 45, 1)
    oled.show()
    if touchpad_t.is_pressed() and touchpad_h.is_pressed():
        if settings_num == 0:
            ui.consani(64, 64, 0, 0, 0, 0, 128, 64)
            pages.wifi_page()
        elif settings_num == 1:
            ui.consani(64, 64, 0, 0, 0, 0, 128, 64)
            core.core.time()
        elif settings_num == 2:
            ui.consani(64, 64, 0, 0, 0, 0, 128, 64)
            core.core.collect()
        elif settings_num == 3:
            ui.consani(64, 64, 0, 0, 0, 0, 128, 64)
            pages.about()
ui.consani(0, 0, 0, 0, 0, 0, 128, 64)