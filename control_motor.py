# Fecha : 07 de feebrero 2026 
# Autor : Jose Gonzalez 
# Descripcion : programa para indicar la potencia de un motor CD 
#ENA : pin 12 , IN1 = pin 16 , IN2 = pin 20; 

import  RPi.GPIO as GPIO # LIBRERIA DE LOS PUERTOS PRINCIPALES 
import time # libreria para pausas en el codigo 

# definicion de pines 
ENA = 12 
IN1 = 16 
IN2 = 20 

# Nomenclatura a utilizar 
GPIO.setmode(GPIO.BCM)

# habilitando pines de salida 
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

# DEFINIENDO PINES DE SALIDA
GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2 , GPIO.LOW)

# L298 ES SU LIMITE DE PWM 1000 
pwm = GPIO.PWM(ENA, 1000)
pwm.start(0)

print("Programa para un control de un motor DC")
print("Para salir del Programa preciona las teclas Ctrl +C")

try: 
    while True: 
        print("Ingres la potencia con in entero entre 1 -100")
        valor = input("")   
        if not valor.isdigit(): # regresa un True o un False 
            print("Es una entrada incorrecta")
            continue # es como un return retorna al while 
        
        potencia = int(valor)

        if 0 <= potencia <= 100: # esto solo se puede hacer en python 
            pwm.ChangeDutyCycle(potencia)
            GPIO.output(IN1, GPIO.HIGH)
            GPIO.output(IN2 , GPIO.LOW)

            print(f"La potencia ingresada es {potencia}")

        else: 
            print("La potencia esta fuera de los limites")
        
        time.sleep(0.1)

except KeyboardInterrupt:
    print("programa detenido")

finally:
    pwm.stop()
    GPIO.output(ENA, GPIO.LOW)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2 , GPIO.LOW)
    GPIO.cleanup()
     
