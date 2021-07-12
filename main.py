def on_button_pressed_a():
    global intervalOne
    intervalOne += 1
    timerTotal()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pin_pressed_p2():
    pass
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def clearTimer():
    global intervalOne, intervalTwo, totalTime
    intervalOne = 0
    intervalTwo = 0
    totalTime = 0
    basic.show_number(totalTime)
    basic.pause(500)
    basic.clear_screen()
def timerTotal():
    global totalTime
    totalTime = intervalOne + intervalTwo
    basic.show_number(totalTime)

def on_button_pressed_ab():
    global totalTime
    while totalTime >= 0:
        basic.show_number(totalTime)
        music.play_tone(440, music.beat(BeatFraction.QUARTER))
        basic.pause(60000)
        totalTime += -1
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global intervalTwo
    intervalTwo += 5
    timerTotal()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    clearTimer()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    timerTotal()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

totalTime = 0
intervalTwo = 0
intervalOne = 0
clearTimer()