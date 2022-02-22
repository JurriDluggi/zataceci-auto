input.onButtonPressed(Button.A, function () {
    wuKong.setMotorSpeed(wuKong.MotorList.M1, -100)
    wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 125)
})
input.onButtonPressed(Button.B, function () {
    wuKong.setMotorSpeed(wuKong.MotorList.M1, 0)
    wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 90)
    basic.showIcon(IconNames.House)
})
input.onLogoEvent(TouchButtonEvent.Touched, function () {
    basic.showIcon(IconNames.Sword)
    wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 125)
})
basic.forever(function () {
	
})
