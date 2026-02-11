print ("buscando el archivo datos.txt")
archivo = open("datos.txt", "a") # LA A ES APPEND  BUSCA SI ESTA EL ARCHIVO SI NO LO ENCUENTRA LO CREA Y LA A ES PARA AGREGARLE INFORMACION A LO QUE AHI ESTA 

print(" el archivo 'datos.txt' ha sido abierto")
archivo.write("se ejecuto el programa\n ")
print("se agrego el mensaje archivo  'datos.txt'")
archivo.close()
print("se cerro el archivo 'datos.txt'")