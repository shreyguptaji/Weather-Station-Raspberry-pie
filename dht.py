import Adafruit_DHT
from time import sleep, strftime, time

sensor = Adafruit_DHT.DHT11

pin = 4



with open("cpu_temp.csv","a") as log:     
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
            log.write("{0},{1},{2}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temperature),str(humidity)))
            sleep(30)
        else:
            print('Failed to get reading. Try again!')
    
    

                        
