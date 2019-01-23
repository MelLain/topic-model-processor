#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Topic Model Viewer (2019)

from . import storage
from . import topic_model
from . import dataset
from . import messages_pb2 as messages

__storage = storage.Storage()
def get_storage():
    global __storage
    return __storage

# Classes from this module should implement all heavy operations over models and their relations
# They can cache final and intermediate results for processing speed-up

# Maybe all viewers should implement the same interface?

# In near future this file should be replaced with directory of files, one per each viewer

# simple examples
class TopicsViewer(object):
    def __init__(self, model_name):
        self.__model = get_storage().get_model(model_name)

    def view(self):
        return self.__model.get_topic_names()


# example with result caching
class TokensViewer(object):
    def __init__(self, model_name):
        self.__model = get_storage().get_model(model_name)
        self.__tokens_cache = None

    def view(self, reset_cache=False):
        if reset_cache or self.__tokens_cache is None:
        	self.__tokens_cache = self.__model.get_tokens()
        return self.__tokens_cache