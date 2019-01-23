# Topic Model Viewer (2019)

class Storage(object):
    def __init__(self):
        self.__models = {}
        self.__hierarchical_relations = {}
        self.__datasets = {}
        # here also can be topics banks

    def get_models_list(self):
        return self.__models.keys()

    def add_model(self, name, model):
        if name in self.__models:
            raise Exception('Model {} has already been added into the models list'.format(name))
        self.__models[name] = model

    def remove_model(self, name):
        if name in self.__models:
            raise Exception('Model {} doesn\'t present in the models list'.format(name))
        del self.__models[name]

    def get_model(self, name):
        if name not in self.__models:
            raise Exception('Model {} is not in the models list'.format(name))
        return self.__models[name]

    def add_hierarchical_relation(self):
        pass

    def remove_hierarchical_relation(self):
        pass

    # Some methods for getting/checking hierarchical relations

    def get_datasets_list(self):
        return self.__datasets.keys()

    def add_dataset(self, name, dataset):
        if name in self.__datasets:
            raise Exception('Dataset {} has already been added into the datssets list'.format(name))
        self.__datasets[name] = dataset

    def remove_dataset(self, name):
        if name in self.__datasets:
            raise Exception('Dataset {} doesn\'t present in the datasets list'.format(name))
        del self.__datasets[name]

    def get_dataset(self, name):
        if name not in self.__datasets:
            raise Exception('Dataset {} is not in the datasets list'.format(name))
        return self.__datasets[name]
