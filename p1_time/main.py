#Archivo main
from servidor import ServidorBerkeley
from cliente import ClienteBerkeley

# Configuración del servidor y el cliente
SERVIDOR_IP = 'localhost'
SERVIDOR_PUERTO = 12345

# Creación de objetos servidor y clientes
servidor = ServidorBerkeley(SERVIDOR_IP, SERVIDOR_PUERTO)
clientes = [ClienteBerkeley(SERVIDOR_IP, SERVIDOR_PUERTO) for _ in range(3)]  # Crea 3 objetos clientes

# Iniciar el servidor
servidor.iniciar_servidor()

# Aceptar conexiones de los clientes
clientes_sockets = [servidor.aceptar_conexion_cliente() for _ in range(3)]  # Acepta conexiones de los 3 clientes

# Recibir el tiempo actual de cada cliente
tiempos_clientes = [servidor.recibir_tiempo_cliente(cliente_socket) for cliente_socket in clientes_sockets]

# Calcular la diferencia de tiempo entre cada cliente y el servidor
diferencias_tiempo = [servidor.calcular_diferencia_tiempo(tiempo_cliente) for tiempo_cliente in tiempos_clientes]

# Ajustar el reloj de cada cliente según la diferencia de tiempo calculada
for cliente_socket, diferencia_tiempo in zip(clientes_sockets, diferencias_tiempo):
    servidor.ajustar_reloj_cliente(cliente_socket, diferencia_tiempo)

# Cerrar conexiones de los clientes
for cliente_socket in clientes_sockets:
    cliente_socket.close()

# Cerrar conexión del servidor 
servidor.cerrar_servidor()
