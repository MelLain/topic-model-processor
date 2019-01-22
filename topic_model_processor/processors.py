__storage = TopicModelStorage()
def get_model_storage():
    global __storage
    return __storage

class Temp(object):
    def temp(self):
        print(get_model_storage())
