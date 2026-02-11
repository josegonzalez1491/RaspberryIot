from datetime import datetime
ruta = "/home/pi/Documents/Github/Test/log.txt"
fechaHora = datetime.now().strftime("%Y-%m-%d %H : %M :%S ")

with open (ruta , "a") as archivo:
    archivo.write(f"ejecucion del cron: {fechaHora}\n")
