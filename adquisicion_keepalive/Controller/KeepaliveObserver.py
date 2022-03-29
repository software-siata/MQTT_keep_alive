import json
import pytz
from datetime import datetime
from Controller.Observer import Observer
from datetime import datetime

class KeepaliveObserver(Observer):

    def callback(self, ch, method, properties, body):
        #try:
            message = json.loads((body.decode()))
            colombia_timezone = pytz.timezone('America/Bogota')
            query = {
                "codigo": message["codigo"]
            }
            update_values = {
                "$set": {
                    "estado": message["estado"],
                    "datos_enviados": message["datos_enviados"],
                    "topicos_enviados": message["topicos_enviados"],
                    "datos_recuperados": message["datos_recuperados"],
                    "ultima_actualizacion": colombia_timezone.localize(datetime.strptime(message["ultima_actualizacion"], '%Y-%m-%d %H:%M:%S')),
                }
            }
            self.model.update(query, update_values)
            print(update_values)
        #except Exception as exception:
        #    self.logger.write_error(exception, body)

