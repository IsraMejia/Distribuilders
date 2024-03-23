#importamos librerias
from socket import *
#librerias que nos proporciona la hora
from datetime import *

direccionServidor = "localhost"
puertoServidor = 9099

#Generamos un nuevo socket
socketServidor = socket( AF_INET, SOCK_STREAM )
#Establecemos la conexion
socketServidor.bind(( direccionServidor, puertoServidor ))
socketServidor.listen()

while True:
    #establecemos la conexion
    socketConexion, addr = socketServidor.accept()

    print("Conectado con cliente", addr)
    #claculamos la hora despues de la peticion
    #esta funcion nos regresa un objeto tipo datetime
    hora = datetime.now()
    #lo convertimos a cadena collocando con cuidado sus respectivos valores en la cadena
    horaCadena = hora.strftime("%Y%m%d %H:%M:%f")
    #Notificamos que enviamos la hora y la fecha
    print("Envio hora al cliente", addr)
    print(hora)
    #mandamos hora al cliente
    socketConexion.send(horaCadena.encode())
    #cerramos conexion
    socketConexion.close()