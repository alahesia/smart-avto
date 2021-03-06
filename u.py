import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)


TRIG = 23
ECHO = 24
 
print "Distance Measurement In Progress"

GPIO.setwarnings(False)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
 
GPIO.output(TRIG, False)
print "Waiting For Sensor To Settle"
time.sleep(2)
 
 
while True:
  GPIO.output(TRIG, True)
  time.sleep(0.00001)
  GPIO.output(TRIG, False)
 
  while GPIO.input(ECHO)==0:  pulse_start = time.time()
  while GPIO.input(ECHO)==1:  pulse_end = time.time()
 
  distance = round(((pulse_end - pulse_start)*17150), 2)
 
  print "Distance:",distance,"cm"
  time.sleep(2)
 

GPIO.cleanup()
