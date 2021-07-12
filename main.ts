input.onButtonPressed(Button.A, function () {
    intervalOne += 1
    timerTotal()
})
input.onPinPressed(TouchPin.P2, function () {
	
})
function clearTimer () {
    intervalOne = 0
    intervalTwo = 0
    totalTime = 0
    basic.showNumber(totalTime)
    basic.pause(500)
    basic.clearScreen()
}
function timerTotal () {
    totalTime = intervalOne + intervalTwo
    basic.showNumber(totalTime)
}
input.onButtonPressed(Button.AB, function () {
    while (totalTime >= 0) {
        basic.showNumber(totalTime)
        music.playTone(440, music.beat(BeatFraction.Quarter))
        basic.pause(60000)
        totalTime += -1
    }
})
input.onButtonPressed(Button.B, function () {
    intervalTwo += 5
    timerTotal()
})
input.onGesture(Gesture.Shake, function () {
    clearTimer()
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    timerTotal()
})
let totalTime = 0
let intervalTwo = 0
let intervalOne = 0
clearTimer()
