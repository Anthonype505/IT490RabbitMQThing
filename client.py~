import pika
import uuid

class clientThing(object):
	def __init__(self):
		creds= pika.PlainCredentials('guest', 'guest')
		self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, 'AMERICA', creds))
		self.channel = self.connection.channel()
		result = self.channel.queue_declare(exclusive=True)
		self.callback_queue = result.method.queue
		print self.callback_queue
		self.channel.basic_consume(self.on_response, no_ack="True", queue=self.callback_queue)

	def on_response(self, ch, method, props, body):
		if self.corr_id == props.correlation_id:
			self.response = body

	def call(self, n):
		self.response = None
		self.corr_id = str(uuid.uuid4())
		self.channel.basic_publish(exchange='testExchange', 
					   routing_key='test',
					   properties=pika.BasicProperties(
						reply_to = self.callback_queue, 
						correlation_id = self.corr_id,
						),
					   body = str(n))
		while self.response is None:
			self.connection.process_data_events()
		return str(self.response)


client = clientThing()

print " Sending a hello!"
response = client.call("hello!")
print "made it!"
print "Response: "  + response
