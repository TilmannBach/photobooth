# Import standard Python time library.
import datetime
import time

# Import GPIO and FT232H modules.
import board
import digitalio
import keyboard

# Configure digital inputs and outputs using the setup function.
# Note that pin numbers 0 to 15 map to pins D0 to D7 then C0 to C7 on the board.
pin = digitalio.DigitalInOut(board.C0)
pin.direction = digitalio.Direction.INPUT

# Loop turning the LED on and off and reading the input state.
print('Press Ctrl-C to quit.')
save_until = datetime.datetime.now() - datetime.timedelta(seconds=10)
old_state = not pin.value

while True:
    # Sleep for 1 second.
    # Sleep for 1 second.
    time.sleep(0.01)
    # Read the input on pin D7 and print out if it's high or low.
    now = datetime.datetime.now()
    current_state = not pin.value
    # if now > (save_until + datetime.timedelta(seconds=10)):
    #     save_until = now
    #     pin = level
    #     if level == GPIO.LOW:
    #         # pin = GPIO.LOW
    #         # keyboard.write('Hello World')
    #         print('setting pin low')
    #     else:
    #         # pin = GPIO.HIGH
    #         print('setting pin high')
    if old_state is False and current_state is True:
        print('take a picture')
        keyboard.press_and_release('space')

    old_state = current_state
