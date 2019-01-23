import os
import json
import codecs

from . import messages_pb2 as messages
from . import constants

# this class should parse binary files of dump and return DataFrames and dicts with score tracker and params
class ArtmDumpParser(object):
    def __init__(self, model_dump_path):
        pass

    def get_phi_as_df(self):
        return None

    def get_nwt_as_df(self):
        return None

    # this method should return None in case of model without theta
    def get_theta_as_df(self):
        return None

    def get_score_tracker(self):
        return {}

    def get_parameters(self):
        return {}


    # this function is invalid for large models with 2 or more slices, shoulb upgraded with DF usage
    def __read_model_file(self, filename):
        return None

        #with open(filename) as fin:
        #    fin.readline()
        #    model = messages.TopicModel()
        #    model.ParseFromString('\n' + fin.read())
        #return model

    def __read_parameters(self, model_path):
        with codecs.open(os.path.join(model_path, 'parameters.json')) as fin:
            return json.load(fin)

    # this method is incorrect for now
    def __read_score_tracker(self, model_path):
        return None

        #score_tracker = {}
        #with open(os.path.join(model_path, 'score_tracker.bin')) as fin:
        #    for i, line in enumerate(fin):
        #        if i % 2 == 0:
        #            continue

        #        score_data = messages.ScoreData()
        #        score_data.ParseFromString('\n' + line)
        #        score_tracker[score_data.name] = self.__parse_score_data(score_data)

        #return score_tracker

    def __parse_score_data(self, score_data):
        return None

        #message = None
        #if score_data.type == constants.ScoreType_Perplexity:
        #    message = messages.PerplexityScore()

        #elif score_data.type == constants.ScoreType_SparsityTheta:
        #    message = messages.SparsityThetaScore()

        #elif score_data.type == constants.ScoreType_SparsityPhi:
        #    message = messages.SparsityPhiScore()

        #elif score_data.type == constants.ScoreType_ItemsProcessed:
        #    message = messages.ItemsProcessedScore()

        #elif score_data.type == constants.ScoreType_TopTokens:
        #    message = messages.TopTokensScore()

        #elif score_data.type == constants.ScoreType_ThetaSnippet:
        #    message = messages.ThetaSnippetScore()

        #elif score_data.type == constants.ScoreType_TopicKernel:
        #    message = messages.TopicKernelScore()

        #elif score_data.type == constants.ScoreType_TopicMassPhi:
        #    message = messages.TopicMassPhiScore()

        #elif score_data.type == constants.ScoreType_ClassPrecision:
        #    message = messages.ClassPrecisionScore()

        #elif score_data.type == constants.ScoreType_BackgroundTokensRatio:
        #    message = messages.BackgroundTokensRatioScore()

        #return message