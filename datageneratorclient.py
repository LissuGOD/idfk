import requests    
import json   
import math   
import time                               

i = 0
while i < 200:
    measurement = { }
    measurement['id'] = i
    measurement['pressure'] = 1024 + math.sin(i/10.0)
    measurement['temperature'] = 300 + 3 * math.cos(i/5.0)
    measurement['humidity'] = 33 + math.cos(i/6.0)

    # muunna json-muotoon 
    s = json.dumps(measurement)
    # TODO: lähetä data HTTP Postilla serverille
    response = requests.post('http://localhost:5000/newmeasurement/', data = s)
    print(response)

    #print(s)
    time.sleep(1)

    i += 1
