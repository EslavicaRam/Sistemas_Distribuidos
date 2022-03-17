import pika
'''
         Parámetros de conexión host, puerto (predeterminado 5672), virtual_host, credenciales (verificación)
         credentials = pika.PlainCredentials ('shampoo', '123456') # mq verificación de nombre de usuario y contraseña
         La cola virtual necesita especificar el parámetro virtual_host, si es el predeterminado, puede dejarlo en blanco.
'''
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarar cola (nombrar la cola)
channel.queue_declare(queue='hello world')

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
# Envío básico
channel.basic_publish(exchange='', 
                      routing_key='hello', # nombre de la cola
                      body='Hello World!') # Contenido enviado
print("Mensaje enviado")
connection.close()