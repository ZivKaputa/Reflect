import pigpio
import time
import signal
import os
import sys

rgb_color = sys.argv[1:3]
strobe_delay = int(sys.argv[4]) / 100.0

P_RED = 17
P_GREEN = 22
P_BLUE = 24

fname = "pids.log"

def signal_handler(signal, frame):
	print("Dying...")
	sys.exit(0)


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



def write_pid():
	f = open(fname, 'a')
	f.write(str(os.getpid()) + '\n')
	f.close()


signal.signal(signal.SIGINT, signal_handler)
kill_existing()
write_pid()



def cleanup():
	pi.set_PWM_dutycycle(P_RED, 0)
	pi.set_PWM_dutycycle(P_GREEN, 0)
	pi.set_PWM_dutycycle(P_BLUE, 0)

pi = pigpio.pi()

def set_rgb(rgb_color):
    red = int(rgb_color[0])
    green = int(rgb_color[1])
    blue = int(rgb_color[2])
    pi.set_PWM_dutycycle(P_RED, red)
    pi.set_PWM_dutycycle(P_GREEN, green)
    pi.set_PWM_dutycycle(P_BLUE, blue)

while True:
	set_rgb(rgb_color)
	time.sleep(0.05)
    	cleanup()
	time.sleep(strobe_delay)

cleanup()
pi.stop()
