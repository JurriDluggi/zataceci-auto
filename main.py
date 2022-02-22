def on_button_pressed_a():
    wuKong.set_motor_speed(wuKong.MotorList.M1, -100)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 125)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    wuKong.set_motor_speed(wuKong.MotorList.M1, 0)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 90)
    basic.show_icon(IconNames.HOUSE)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_touched():
    basic.show_icon(IconNames.SWORD)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 125)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def on_forever():
    pass
basic.forever(on_forever)
