import RPi.GPIO as GPIO
import time
import Adafruit_DHT

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

#temperature
sensor=Adafruit_DHT.DHT11
pin=26

TRIG = 23
ECHO = 24
 
print "Distance Measurement In Progress"
 
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

  humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
  t=temperature
  print(t)


  time.sleep(2)
 
GPIO.cleanup()

