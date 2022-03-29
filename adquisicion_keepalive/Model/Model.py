import configparser
from pymongo import MongoClient

class Model:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('configfile.ini')
        self.database_dict = dict(self.config.items('DATABASE'))
        self.client = MongoClient(self.database_dict['url'])
        self.database = self.client["siata"]
        self.collection = self.database["estado_estaciones_estaciones"]

    def update(self, query, values):
        try:
            self.collection.update_one(query, values)
        except Exception as exception:
            raise Exception(exception)