#example 3-2. encoding a python datetime to json 
import datetime 
from dateutil import parser 
import json   

class JSONDateTimeEncoder(json.JSONEncoder): 
    def default(self, obj):  
        if isinstance(obj, (datetime.date,datetime.datetime)):
            return obj.isoformat()  
        else:  
            return json.JSONEncoder.default(self, obj)  
        
def dumps(obj):  
    return json.dumps(obj, cls=JSONDateTimeEncoder)

now_str = dumps({'time': datetime.datetime.now()})

print(now_str)
