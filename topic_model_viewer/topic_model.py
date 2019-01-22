#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Topic Model Viewer (2019)

import os
import json
import codecs

from . import messages_pb2 as messages
from . import constants

class TopicModel(object):
    # here different init methods can be added, like set of DataFrames or so on

    def __init__(self, model_path):
        self.__model_path = model_path

        # here protobuf messages should be put into DF
        self.__pwt = self.__read_model_file(os.path.join(model_path, 'p_wt.bin'))
        self.__nwt = self.__read_model_file(os.path.join(model_path, 'n_wt.bin'))

        theta_file_path = os.path.join(model_path, 'theta.bin')
        self.__theta = None
        if os.path.exists(theta_file_path):
            self.__theta = self.__read_model_file(theta_file_path)

        # wrap this fields content with getters (like get_topic_name, get_tokens etc)
        self.__parameters = self.__read_parameters(model_path)
        self.__score_tracker = self.__read_score_tracker(model_path)
        print(self.__score_tracker)

    # this function is invalid for large models with 2 or more slices, shoulb upgraded with DF usage
    def __read_model_file(self, filename):
        with open(filename) as fin:
            fin.readline()
            model = messages.TopicModel()
            model.ParseFromString('\n' + fin.read())
        return model

    def __read_parameters(self, model_path):
        with codecs.open(os.path.join(model_path, 'parameters.json')) as fin:
            return json.load(fin)

    # this method is incorrect for now
    def __read_score_tracker(self, model_path):
        score_tracker = {}
        with open(os.path.join(model_path, 'score_tracker.bin')) as fin:
            for i, line in enumerate(fin):
                if i % 2 == 0:
                    continue

                score_data = messages.ScoreData()
                score_data.ParseFromString('\n' + line)
                score_tracker[score_data.name] = self.__parse_score_data(score_data)

        return score_tracker

    def __parse_score_data(self, score_data):
        message = None
        if score_data.type == constants.ScoreType_Perplexity:
            message = messages.PerplexityScore()

        elif score_data.type == constants.ScoreType_SparsityTheta:
            message = messages.SparsityThetaScore()

        elif score_data.type == constants.ScoreType_SparsityPhi:
            message = messages.SparsityPhiScore()

        elif score_data.type == constants.ScoreType_ItemsProcessed:
            message = messages.ItemsProcessedScore()

        elif score_data.type == constants.ScoreType_TopTokens:
            message = messages.TopTokensScore()

        elif score_data.type == constants.ScoreType_ThetaSnippet:
            message = messages.ThetaSnippetScore()

        elif score_data.type == constants.ScoreType_TopicKernel:
            message = messages.TopicKernelScore()

        elif score_data.type == constants.ScoreType_TopicMassPhi:
            message = messages.TopicMassPhiScore()

        elif score_data.type == constants.ScoreType_ClassPrecision:
            message = messages.ClassPrecisionScore()

        elif score_data.type == constants.ScoreType_BackgroundTokensRatio:
            message = messages.BackgroundTokensRatioScore()

        return message
