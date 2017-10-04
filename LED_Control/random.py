import sys
import pigpio
import time
import numpy

P_RED = 17
P_GREEN = 22
P_BLUE = 24


delay = sys.argv[1]
total = sys.argv[2]

def random_rgb(delay, total):
    while total != 0:
        pi = pigpio.pi()
        red = numpy.random.randint(0, 255)
        green = numpy.random.randint(0, 255)
        blue = numpy.random.randint(0, 255)

        pi.set_PWM_dutycycle(P_RED, red)
        pi.set_PWM_dutycycle(P_GREEN, green)
        pi.set_PWM_dutycycle(P_BLUE, blue)

        time.sleep(delay)
        total += -1


random_rgb(delay, total)
