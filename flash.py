import pigpio
import time

P_RED = 17
P_GREEN = 22
P_BLUE = 24

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