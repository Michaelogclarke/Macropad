import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

keyboard = Keyboard(usb_hid.devices)

consumer = ConsumerControl(usb_hid.devices)
#App Shortcuts
notion = Keycode.SHIFT, Keycode.ALT, Keycode.S
discord = Keycode.SHIFT, Keycode.ALT, Keycode.K
brave = Keycode.SHIFT, Keycode.ALT, Keycode.L
spotify = Keycode.SHIFT, Keycode.ALT, Keycode.H
# Key assaignments

# Top left 
btn1_pin = board.GP19
# Up arrow
btn2_pin = board.GP20
# Top right
btn3_pin = board.GP21
# Left arrow
btn4_pin = board.GP6
# Down arrow
btn5_pin = board.GP8
# Right arrow
btn6_pin = board.GP7

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN

btn5 = digitalio.DigitalInOut(btn5_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.DOWN

btn6 = digitalio.DigitalInOut(btn6_pin)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.DOWN



while True:
    if btn1.value:
        print("Button 1 pressed!")
        consumer.send(ConsumerControlCode.PLAY_PAUSE)
        time.sleep(0.1)
       
    if btn2.value:
        print("Button 2 pressed!")
        consumer.send(ConsumerControlCode.SCAN_PREVIOUS_TRACK)
        time.sleep(0.1)
     
    if btn3.value:
        print("Button 3 pressed!")
        consumer.send(ConsumerControlCode.SCAN_NEXT_TRACK)
        time.sleep(0.1)
      
    if btn4.value:
        print("Button 4 pressed!")
        keyboard.send(Keycode.SHIFT, Keycode.ALT, Keycode.H)
        time.sleep(0.1)
       
    if btn5.value:
        print("Button 5 pressed!")
        keyboard.send(Keycode.SHIFT, Keycode.ALT, Keycode.S)
        time.sleep(0.1)
       
    if btn6.value:
        print("Button 6 pressed!")
        keyboard.send(Keycode.SHIFT, Keycode.ALT, Keycode.L)
        time.sleep(0.1)
     
      