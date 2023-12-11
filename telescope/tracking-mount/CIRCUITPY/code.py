import board
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import time

kit = MotorKit(i2c=board.I2C())

style = stepper.DOUBLE
def forward():
    return kit.stepper2.onestep(style=style, direction=stepper.FORWARD)

def backward():
    return kit.stepper2.onestep(style=style, direction=stepper.BACKWARD)

pos = 0
step = None
while True:
    if pos >= 2000:
        step = backward
    if pos <= 0:
        step = forward
    pos = step()
    print(f"Stepping {pos}")
    # time.sleep(0.01)

kit.stepper2.release()
