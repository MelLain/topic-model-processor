#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Topic Model Viewer (2019)

class Dataset(object):
    def __init__(self, dataset_path):
        self.__dataset_path = dataset_path
        # initialize fields like docs/vocab/stats/etc

    def get_vw_document(self, document_id=None, document_name=None):
        if document_id is None and document_name is None:
            raise Exception('Either document_id or document_name should be set to get a document')
        pass

    def get_src_document(self, document_id=None, document_name=None):
        if document_id is None and document_name is None:
                raise Exception('Either document_id or document_name should be set to get a document')
        pass

    # get all documents or some subsets of documents, meta/stats info etc (depends on input and storage format)
    # simple way is to store the whole dataset in the memory, more complex ways to store part of the data
    # in the memory and part on disk are discussable
