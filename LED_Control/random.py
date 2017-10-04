import sys
import pigpio
import time
import randint

P_RED = 17
P_GREEN = 22
P_BLUE = 24


delay = sys.argv[1]
total = sys.argv[2]

def random_rgb(delay, total):
    while total != 0:
        pi = pigpio.pi()
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)

        pi.set_PWM_dutycycle(P_RED, red)
        pi.set_PWM_dutycycle(P_GREEN, green)
        pi.set_PWM_dutycycle(P_BLUE, blue)

        time.sleep(delay)
        total += -1


set_rgb(delay, total)
