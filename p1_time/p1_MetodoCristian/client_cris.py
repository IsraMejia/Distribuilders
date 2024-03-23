from socket import *
#esta librería sirve para calcular el tiempo de ejecución
#nos permite crear dos variables una donde empezamos a medir el tiempo inicial y la otra el tiempo final
import time
#para hacer uso de la función de la hora
import datetime

#creamos una funcion para convertir una cadena de caracteres a tipo datetime
def convertir_cadena_a_hora(cadena):
    #seleccionamos el formato en que queremos convertir la cadena
    formato = '%Y%m%d %H:%M:%f'
    #recibimos el objeto de tipo datetime
    hora_cadena = datetime.datetime.strptime(cadena,formato)
    #regresamos el objeto creado
    return hora_cadena

IPServidor = "localhost"
puertoServidor = 9099
#se declaran e inicilaizan los valores el socket del cliente
socketCliente = socket(AF_INET, SOCK_STREAM)

#comenzamos a medir el tiempo
inicio = time.time()
socketCliente.connect((IPServidor, puertoServidor))

#recibimos la hora en forma de cadena
hora_cadena = socketCliente.recv(4096).decode()

#Observamos el tiempo de ejecucion desde el momento en que nos conectamos al servidor hasta el momento de obtener respuesta
final = time.time()
#hacmos la resta para saber el tiempo total
tiempo = final - inicio

#convertimos la cadena que se nos regresa por medio de la siguiente funcion a un objeto datetime para poder operar con el
hora = convertir_cadena_a_hora(hora_cadena)

#imprimimos el tiempo que tardo desde la conexion con el servidor y la recepcion de la respuesta del sevidor
print("El tiempo total de ida y vuelta fue:", tiempo)
#dividimos entre dos el resultado del tiempo entre dos ya que es el aproximado desde que el servidor envio la hora a nuestra computadora
#tomando en cuenta que empezamos a contar el tiempo desde que pedimos conexion con el servidor
mitadTiempo =tiempo/2
print("El tiempo total de ida :", mitadTiempo)
#le sumamos la diferencia por medio del objeto (timedelta) a nuestra hora para tenerla lo mas acercada posible a la hora del sevidor e imprimimos
print("Hora servidor: ", hora_cadena)
print("La hora exacta es :", hora + datetime.timedelta(seconds=mitadTiempo))
#cerramos socket
socketCliente.close() 