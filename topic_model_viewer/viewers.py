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

class Temp(object):
    def temp(self):
        topic_model.TopicModel('/Users/mel-lain/Downloads/kos_model_dump')
        print(get_storage())
        print(messages.SmoothSparsePhiConfig())
