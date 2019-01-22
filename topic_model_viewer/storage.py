# Topic Model Viewer (2019)

class Storage(object):
    def __init__(self):
        self.__models = {}
        self.__hierarchical_relations = {}
        self.__datasets = {}

    def add_model(self, name, model):
        if name in self.__models:
            raise Exception('Model {} has already been added into the models list'.format(name))
        self.__models[name] = model

    def remove_model(self, name):
        if name in self.__models:
            raise Exception('Model {} doesn\'t present in the models list'.format(name))
        del self.__models[name]

    def add_hierarchical_relation(self):
        pass

    def remove__hierarchical_relation(self):
        pass

    def add_dataset(self, name, dataset):
        if name in self.__datasets:
            raise Exception('Dataset {} has already been added into the models list'.format(name))
        self.__datasets[name] = dataset

    def remove_dataset(self, name):
        if name in self.__datasets:
            raise Exception('Dataset {} doesn\'t present in the models list'.format(name))
        del self.__datasets[name]
