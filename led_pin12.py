import  RPi.GPIO as GPIO # LIBRERIA DE LOS PUERTOS PRINCIPALES 
import time # libreria para pausas en el codigo 

LED_PIN = 12 # NUMERO DE PIN DONDE ESTA CONECTADO EL LED 

GPIO.setmode(GPIO.BCM)# ESCOGIENDO NUMERACION BCM PARA SELECCIONAR LOS PINES 
GPIO.setup(LED_PIN, GPIO.OUT) # ESTABLECIENDO EL LED_PIN COMO SALIDAA 

try: 
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH) # estableciendo el estado alto 
        print("led encecido ") 
        time.sleep(1)

        GPIO.output(LED_PIN, GPIO.LOW) # apagando el estado alto 
        print("led apagado ") 
        time.sleep(1)


except KeyboardInterrupt:
    print("programa detenido")

finally:
    GPIO.cleanup()
    
