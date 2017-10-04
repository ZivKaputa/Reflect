import sys
import pigpio
import time

P_RED = 17
P_GREEN = 22
P_BLUE = 24

rgb_color = sys.argv[1:]
set_rgb(rgb_color)

def set_rgb(rgb_color):
    red = int(rgb_color[0])
    green = int(rgb_color[1])
    blue = int(rgb_color[2])
    pi.set_PWM_dutycycle(P_RED, red)
    pi.set_PWM_dutycycle(P_GREEN, green)
    pi.set_PWM_dutycycle(P_BLUE, blue)
