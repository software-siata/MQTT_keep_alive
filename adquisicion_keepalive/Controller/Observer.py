import pika
import configparser
from abc import ABC, abstractmethod
from Model.Model import Model
from Assets.Logger import Logger

class Observer(ABC):

    def __init__(self, red_mqtt):
        self.config = configparser.ConfigParser()
        self.config.read('configfile.ini')
        broker_dict = dict(self.config.items('BROKER'))
        red_dict = dict(self.config.items(red_mqtt))
        self.credentials = pika.PlainCredentials(broker_dict['username'], broker_dict['password'])
        self.parameters = pika.ConnectionParameters(credentials=self.credentials, host=broker_dict['host'])
        self.connection = pika.BlockingConnection((self.parameters))
        self.channel = self.connection.channel()
        self.result = self.channel.queue_declare(queue=red_dict['queue'])
        self.queue_name = self.result.method.queue
        self.channel.queue_bind(exchange=red_dict['exchange'], queue=self.queue_name, routing_key=red_dict['topic'])
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.callback, auto_ack=True)
        self.model = Model()
        self.logger = Logger(red_dict['logger_file'], red_dict['data_file'])
        self.logger.write_start()

    @abstractmethod 
    def callback(self, ch, method, properties, body):
        pass
