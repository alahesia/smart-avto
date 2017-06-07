import RPi.GPIO as GPIO
import time
import urllib2

baseurl = 'http://api.q1q2.net?api=ok'


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


r1=16 #dveri
#svitlo
r2=20
#povorotu
r3=21

GPIO.setup(r1,GPIO.OUT)
GPIO.setup(r2,GPIO.OUT)
GPIO.setup(r3,GPIO.OUT)


TRIG = 23
ECHO = 24
 
print "Distance Measurement In Progress"


GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
 
GPIO.output(TRIG, False)
print "Waiting For Sensor To Settle"
time.sleep(2)
 


# http://api.q1q2.net?api=ok&rip=1&temp=24
def urlf(name,value):
    return "&"+name+"="+str(value)





 
while True:
  GPIO.output(TRIG, True)
  time.sleep(0.00001)
  GPIO.output(TRIG, False)
 
  while GPIO.input(ECHO)==0:  pulse_start = time.time()
  while GPIO.input(ECHO)==1:  pulse_end = time.time()
 
  distance = round(((pulse_end - pulse_start)*17150), 2)
 
  print "Distance:",distance,"cm"

  url=baseurl+str(urlf("d",distance))
  print url
 
  f = urllib2.urlopen(url)
  print (f.read())
  f.close()


  r=input('Vvedit komandu: ')
  r=int(r)

  if r==1:
    print('1 door opened -> ok')
    GPIO.output (r1, GPIO.HIGH)
  elif r==2:
    print('2 door closed -> ok')
    GPIO.output (r1, GPIO.LOW)
  elif r==3:
    GPIO.output (r2, GPIO.HIGH)
  elif r==4:
    GPIO.output (r2, GPIO.LOW)
  elif r==5:
    GPIO.output (r3, GPIO.HIGH)
  elif r==6:
    GPIO.output (r3, GPIO.LOW)


  time.sleep(2)
 

GPIO.cleanup()
