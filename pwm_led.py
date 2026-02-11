import  RPi.GPIO as GPIO # LIBRERIA DE LOS PUERTOS PRINCIPALES 
import time # libreria para pausas en el codigo 

LED_PIN = 12 # PIN DONDE ESTA EL LED 

GPIO.setmode(GPIO.BCM) # numeracion bcm 
GPIO.setup(LED_PIN, GPIO.OUT) # PIN 12 COMO SALIDA 

pwm = GPIO.PWM(LED_PIN, 1000) #PERIODO DE 1KHZ 
pwm.start(0)# INICIA EL PUERTO EN 0 
try:
    while True:
        # rutina para aumentar la intensidad del led 
        for duty in range (0 , 101 ,5): # aumenta de 5 en 5 la cuenta 
            pwm.ChangeDutyCycle(duty)
            print( f"BRILLO: {duty}%")
            time.sleep(0.5)

        # programa para disminuir la intencidad del led 
        for duty in range (100 , -1 ,-5): # decrementa de 5 en 5 la cuenta 
            pwm.ChangeDutyCycle(duty)
            print( f"BRILLO: {duty}%")
            time.sleep(0.5)

except KeyboardInterrupt : 
    print("programa detenido")


finally: 
    pwm.stop()
    GPIO.cleanup()

