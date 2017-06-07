import RPi.GPIO as GPIO
import time
import Adafruit_DHT

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

#temperature
sensor=Adafruit_DHT.DHT11
pin=26

 
while True:
  
  humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
  t=temperature
  print(t)

  time.sleep(1)
 
GPIO.cleanup()

