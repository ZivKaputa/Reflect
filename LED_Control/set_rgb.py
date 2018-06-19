import sys
import pigpio
import time
import os

fname = "pids.log"

P_RED = 17
P_GREEN = 22
P_BLUE = 24

rgb_color = sys.argv[1:3]

def kill_existing():
	f = open(fname, 'r')
	for line in f:
		pid = int(line)
		print("Killing " + str(pid) + " (I am " + str(os.getpid()) + ")")
		try:
			os.kill(pid,signal.SIGINT)
		except SystemExit:
			f = open(fname, 'w+')
			f.close()
			sys.exit(0)
		except:
			pass
	f = open(fname, 'w+')
	f.close()
	f.close()

def set_rgb(rgb_color):
    pi = pigpio.pi()
    red = int(rgb_color[0])
    green = int(rgb_color[1])
    blue = int(rgb_color[2])
    pi.set_PWM_dutycycle(P_RED, red)
    pi.set_PWM_dutycycle(P_GREEN, green)
    pi.set_PWM_dutycycle(P_BLUE, blue)




set_rgb(rgb_color)
