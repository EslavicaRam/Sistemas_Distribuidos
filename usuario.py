import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Aquí está la razón de hola mundo. Si el consumidor se ejecuta primero, se informará un error si el productor hola aún no existe.
# Si se determina que el servidor se inicia primero, se determina que el nombre de la cola es hola. También se puede omitir lo siguiente (se recomienda escribir !!! Hermano)
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    '''
         : param ch: el objeto de memoria de la tubería
    :param method:
    :param properties:
    :param body:
    :return:
    '''
    import time
    print("Comienzo")
    time.sleep(10)
    print("Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


# Consumo de mensajes, si se recibe un mensaje, llame a la devolución de llamada para procesar el mensaje. Recibe mensajes de la cola de saludo.
# auto_ack Confirmación automática, envíe un mensaje al servidor después de procesar el mensaje
channel.basic_consume('hello', callback, True)

print('En espera de recibir un mensaje, cierre y presione CTRL + C')
channel.start_consuming()