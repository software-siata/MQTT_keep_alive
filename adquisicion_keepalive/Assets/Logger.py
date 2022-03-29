import logging

class Logger:

    def __init__(self, logger_file, data_file):
        self.logger_file = logging.basicConfig(filename=logger_file, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S %Z', level=logging.ERROR)
        self.data_file = data_file
        self.error_count = 0
        
    
    def write_error(self, error, data):
        self.error_count += 1
        error = "[" + str(self.error_count) + "] " + str(error)
        logging.error(error)
        file = open(self.data_file, "a")
        file.write("[" + str(self.error_count) + "] " + data.decode() + "\n")
        file.close()

    def write_start(self):
        error = "Prueba"
        logging.error(error)