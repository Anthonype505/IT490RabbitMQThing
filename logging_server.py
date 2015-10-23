import pika

creds= pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.106', 5672,'AMERICA', creds))

channel = connection.channel()

channel.queue_declare(queue='log')

def on_request(ch, method, props, body):
	#print "Response from client: " + body
	thing = open("rabbit.log","a")
	thing.write(body+"\n")
	print body+"\n"
	thing.close();
	print body + " was logged."

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='log',no_ack="True")
# Data will listen/receive things here

print " [x] Awaiting Logs"

channel.start_consuming()
