#ARCHIVO CLIENTE

import socket
import time
import random
from datetime import datetime, timedelta 
Como hago que mi objeto ClienteBerkeley tenga el atributo hora_desfasada que sera asignado a simismo una vez 
que se ejecuta el metodo getHoraCliente
class ClienteBerkeley:
    def __init__(self, servidor_ip, servidor_puerto):
        """
        Inicializa el objeto ClienteBerkeley. 
        """
        self.servidor_ip = servidor_ip
        self.servidor_puerto = servidor_puerto #puerto del servidor al que se conectará el cliente.
        self.cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def conectar_servidor(self):
        """
        Conecta el cliente al servidor utilizando la dirección IP y el puerto especificados.
        """
        self.cliente_socket.connect((self.servidor_ip, self.servidor_puerto))

    def getHoraCliente(): 
        """Genera hora del cliente con un desfase aleatorio de milisegundos""" 
        desfase_ms = random.randint(700, 5000)  # Desfase aleatorio en milisegundos
        hora_actual = datetime.now()  # Obtener la hora actual
        hora_desfasada = hora_actual + timedelta(milliseconds=desfase_ms)  # Agregar el desfase
        return hora_desfasada  
     

    
    def enviar_tiempo_al_servidor(self, tiempo):
        """
        Envía el tiempo actual al servidor.

        Args:
            tiempo (datetime): El tiempo actual del sistema.
        """
        tiempo_str = tiempo.strftime("%Y-%m-%d %H:%M:%S.%f")  # Convertir el objeto datetime a una cadena de texto
        self.cliente_socket.send(tiempo_str.encode())


    def recibir_diferencia_tiempo(self):
        """
        Recibe la diferencia de tiempo calculada por el servidor.

        Returns:
            float: La diferencia de tiempo calculada por el servidor.
        """
        return float(self.cliente_socket.recv(1024).decode())

    def cerrar_conexion(self):
        """
        Cierra la conexión del cliente con el servidor.
        """
        self.cliente_socket.close()
