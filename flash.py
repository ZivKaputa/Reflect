import pigpio
import time
import signal
import os
import sys

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
		except:
			pass
	f.close()
	# f = open(fname, 'w+')
	# f.close()


def write_pid():
	f = open(fname, 'a')
	f.write(str(os.getpid()) + '\n')
	f.close()

write_pid()
signal.signal(signal.SIGINT, signal_handler)
kill_existing()



def cleanup():
	pi.set_PWM_dutycycle(P_RED, 0)
	pi.set_PWM_dutycycle(P_GREEN, 0)
	pi.set_PWM_dutycycle(P_BLUE, 0)

pi = pigpio.pi()

while True:

	pi.set_PWM_dutycycle(P_RED, 255)
	pi.set_PWM_dutycycle(P_GREEN, 255)
	pi.set_PWM_dutycycle(P_BLUE, 255)
	time.sleep(0.05)
    	cleanup()
	time.sleep(0.05)

cleanup()
pi.stop()
