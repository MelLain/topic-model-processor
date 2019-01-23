#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Topic Model Viewer (2019)

from . import artm_dump_parser

# This class should contain all common routines of model processing, that do not need result caching
class TopicModel(object):
    # read model either from dump or directly from DataFrames and meta-data in dicts
    def __init__(self, model_path=None, phi=None, nwt=None, theta=None, parameters=None, score_tracker=None):
        self.__model_path = model_path
        
        dump_parser = artm_dump_parser.ArtmDumpParser(model_path) if model_path is not None else None

        if dump_parser is not None:
            self.__phi = dump_parser.get_phi_as_df()
            self.__nwt = dump_parser.get_nwt_as_df()

            self.__theta = dump_parser.get_theta_as_df()

            self.__score_tracker = dump_parser.get_score_tracker()
            self.__parameters = dump_parser.get_parameters()
        elif phi is not None: # maybe here should be more strict constrains?
            self.__phi = phi
            self.__nwt = nwt

            self.__theta = theta

            self.__score_tracker = score_tracker
            self.__parameters = parameters
        else:
            raise Exception('Unable to create TopicModel instance without phi matrix')

    # here should be getters for all field and their contents

    # simple examples
    def get_topic_names(self):
        return list(self.__phi.columns.values)

    def get_tokens(self):
        return list(self.__phi.index.values)
