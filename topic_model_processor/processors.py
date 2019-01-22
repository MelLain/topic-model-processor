# Topic Model Processor (2019)
from . import storage

__storage = storage.Storage()
def get_model_storage():
    global __storage
    return __storage

class Temp(object):
    def temp(self):
        print(get_model_storage())
