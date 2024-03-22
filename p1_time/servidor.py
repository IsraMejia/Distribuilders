#Archivo Servidor
import socket
import time

class ServidorBerkeley:
    def __init__(self, ip, puerto):
        """
        Inicializa el objeto ServidorBerkeley.

        Args:
            ip (str): La dirección IP del servidor.
            puerto (int): El puerto en el que el servidor escuchará las conexiones entrantes.
        """
        self.ip = ip
        self.puerto = puerto
        self.servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def iniciar_servidor(self):
        """
        Inicia el servidor y lo pone en modo de escucha para aceptar conexiones entrantes.
        """
        self.servidor_socket.bind((self.ip, self.puerto))
        self.servidor_socket.listen(5)
        print("Servidor en ejecución...")

    def aceptar_conexion_cliente(self):
        """
        Acepta la conexión entrante de un cliente y devuelve el socket de cliente correspondiente.

        Returns:
            socket.socket: El socket de cliente aceptado.
        """
        cliente_socket, _ = self.servidor_socket.accept()
        print("Cliente conectado.")
        return cliente_socket

    def recibir_tiempo_cliente(self, cliente_socket):
        """
        Recibe el tiempo actual enviado por el cliente.

        Args:
            cliente_socket (socket.socket): El socket del cliente del que se recibirá el tiempo.

        Returns:
            float: El tiempo actual enviado por el cliente.
        """
        tiempo_cliente = float(cliente_socket.recv(1024).decode())
        return tiempo_cliente

    def calcular_diferencia_tiempo(self, tiempo_cliente):
        """
        Calcula la diferencia de tiempo entre el cliente y el servidor.

        Args:
            tiempo_cliente (float): El tiempo actual enviado por el cliente.

        Returns:
            float: La diferencia de tiempo entre el cliente y el servidor.
        """
        tiempo_servidor = time.time()
        return tiempo_servidor - tiempo_cliente

    def ajustar_reloj_cliente(self, cliente_socket, diferencia_tiempo):
        """
        Ajusta el reloj del cliente según la diferencia de tiempo calculada.

        Args:
            cliente_socket (socket.socket): El socket del cliente al que se ajustará el reloj.
            diferencia_tiempo (float): La diferencia de tiempo entre el cliente y el servidor.
        """
        tiempo_cliente_ajustado = time.time() + diferencia_tiempo
        cliente_socket.send(str(tiempo_cliente_ajustado).encode())

    def cerrar_servidor(self):
        """
        Cierra el socket del servidor.
        """
        self.servidor_socket.close()
