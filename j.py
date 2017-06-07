import json
import urllib2


f = urllib2.urlopen("http://api.q1q2.net?api=ok")
text=f.read()
print (text)


b = json.loads(text)
print b['status']
