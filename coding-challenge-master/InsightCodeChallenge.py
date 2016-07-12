import os
import json
import re
import time
import datetime

output = open('output.txt', 'wb')

FLAGS = re.VERBOSE | re.MULTILINE | re.DOTALL
WHITESPACE = re.compile(r'[ \t\n\r]*', FLAGS)


class ConcatJSONDecoder(json.JSONDecoder):
    def decode(self, s, _w=WHITESPACE.match):
        s_len = len(s)

        objs = []
        end = 0
        while end != s_len:
            obj, end = self.raw_decode(s, idx=_w(s, end).end())
            end = _w(s, end).end()
            objs.append(obj)
        return objs
TempVar1=0
TempVar2=0
graphmap= {}
TempArray=[]
file = open(os.path.expanduser("~/Documents/venmo-trans.txt"))
data = json.load(file, cls=ConcatJSONDecoder)
for y in range (0, len(data)):
 try:
  test= data[y]["actor"]["target"]
  test2= data[y]["created_time"]
  UT=time.mktime(datetime.datetime.strptime(test2, "%Y-%m-%dT%H:%M:%SZ").timetuple())
  
  UT2=time.mktime(datetime.datetime.strptime(data[y+1]["created_time"], "%Y-%m-%dT%H:%M:%SZ").timetuple())-UT
  if UT2>=0 and UT2<=60:    
      if len(test)>0:
       TempVar2=TempVar2+1    
       for x in range (0, len(test)):
      
        TempArray.append(test[x]["text"])
        TempVar1=TempVar1+1
       
       graphmap[y]=TempArray
       TempArray=[]
      
 except:
  pass
connectionmap={}
arraymap=[]
      
for key in graphmap:
       
    for y in range(0, len(graphmap[key])):
        if(connectionmap.has_key(graphmap[key][y])==False):
            connectionmap[graphmap[key][y]]=len(graphmap[key])-1
        else:
             t=connectionmap[graphmap[key][y]]
             connectionmap[graphmap[key][y]]=t+len(graphmap[key])-1
            
    sum=0;
    for key in connectionmap:
        sum=sum+connectionmap[key]
    sum1=sum//len(connectionmap)
    output.write("%.2f" %sum1+"\n")

output.close()