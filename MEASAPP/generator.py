import math
import random
import time
import requests

# laskuri, joka kuvaa myös aikaa sekunteina

# avataan tiedosto mittausten kirjoittamista varten
tiedosto = open("mittaukset", "w")

i = 0
while i < 100:
    # olio mittausta varten
    measurement = {}
    measurement["time"] = i
    measurement["pressure"] = math.sin(i/10) + (random.random() * 2 - 1)
    measurement["temperature"] = math.cos(i/15) + (random.random() * 4 - 2)
    measurement["humidity"] = math.sin(i/20) + (random.random() * 6 - 3)

    #s = str(i) + " " + str(measurement["pressure"]) + " " + str(measurement["temperature"]) + " " + str(measurement["humidity"])
    #tiedosto.write(s + "\n")

    # sarjallista measurement json-muotoon
    # lähetä mittaukset thingspeakiin

    # import requests
    response = requests.post('http://localhost:5000/api/measurements', json=measurement)
    print(response)

    time.sleep(1) # import time
    i += 1

tiedosto.close()