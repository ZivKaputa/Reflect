import sys
import pigpio
import time
from random import randint

P_RED = 17
P_GREEN = 22
P_BLUE = 24
pi = pigpio.pi()

delay = sys.argv[1]
total = sys.argv[2]

def cleanup():
	pi.set_PWM_dutycycle(P_RED, 0)
	pi.set_PWM_dutycycle(P_GREEN, 0)
	pi.set_PWM_dutycycle(P_BLUE, 0)

def random_rgb(delay, total):
    while total != 0:

        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)

        pi.set_PWM_dutycycle(P_RED, red)
        pi.set_PWM_dutycycle(P_GREEN, green)
        pi.set_PWM_dutycycle(P_BLUE, blue)

        time.sleep(delay)
        total += -1
    cleanup()




random_rgb(float(delay), int(total))
