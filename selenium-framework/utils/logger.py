import logging
import inspect


class Logger:
    '''
    Create logging instance with create_logger() -> logger
    '''
    # La propiedad __name__ obtiene el nombre del archivo actual
    default_format = '%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(message)s'

    def create_logger(self):
        # Obtiene el nombre del archivo desde el cuál es llamada la función
        origin_name = inspect.stack()[1][3]
        logger = logging.getLogger(origin_name)

        file_handler = logging.FileHandler(
            './reports/logfile.log')
        logger.addHandler(file_handler)
        formatter = logging.Formatter(
            '%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        file_handler.setFormatter(formatter)
        logger.setLevel(logging.DEBUG)
        return logger
