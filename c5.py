import RPi.GPIO as GPIO
import time
import urllib2
import json
import math

baseurl = 'http://api.q1q2.net?api=ok'


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


r1=16 #svitlo
r2=20 #povorotu
r3=21 #dveri

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



b=0
t=0
temp_r = 3
 
while True:

  GPIO.output(TRIG, True)
  time.sleep(0.00001)
  GPIO.output(TRIG, False)
 
  while GPIO.input(ECHO)==0:  pulse_start = time.time()
  while GPIO.input(ECHO)==1:  pulse_end = time.time()
 
  distance = round(((pulse_end - pulse_start)*17150), 1)
  
  if(math.fabs(t-distance)>0.7):
    #print '%02d' % some_float  # 1234
    print "Distance:",'%02d' % distance,"cm";
  t=distance

  url=baseurl+str(urlf("d",distance))
#  print url
 
  f = urllib2.urlopen(url)
  result = f.read()  
#  print (result)
  f.close()
  temp = json.loads(result)
#  print temp['status']

  if temp_r!=temp['r3']:
    temp['r2']=0;

#  print "temp_r",temp_r," s_r3", temp['r3']

  temp_r = temp['r3']

  #r=input('Vvedit komandu: ')
  #r=int(r)

  if temp['status']=='ok':

#   svitlo
    if temp['r1']:
      GPIO.output (r1, GPIO.HIGH)
    else:
      GPIO.output (r1, GPIO.LOW);

#   povorotu
    if temp['r2']:
#     blink led :)
      GPIO.output (r2, GPIO.HIGH)
    else:
      if b==1:
        GPIO.output (r2, GPIO.LOW)
      else:
        GPIO.output (r2, GPIO.HIGH);

#   dveri
    if temp['r3']:
      GPIO.output (r3, GPIO.HIGH)
    else:
      GPIO.output (r3, GPIO.LOW);

#  print(' ')
  time.sleep(1)
  if b==0 :
    b=1
  else:
    b=0
 

GPIO.cleanup()
