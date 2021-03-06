import os
import threading
import secrets

from rest import ml
from configVariable import logger
from flask_restplus.resource import Resource
from flask import request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from serviceML import MachineLearningService
from time import gmtime, strftime

@ml.route('/', methods=['GET'])
class ReturnAllURL(Resource):
    '''
    존재하는 모든 api 접근 url 반환하는 서비스
    '''
    @ml.doc(description='존재하는 모든 api의 접근 url을 반환합니다.')
    def get(self):
        result_allurl = {
            'all_services': "/ml",
        }
        return result_allurl

@ml.route('/ml', methods=['GET'])
class ReturnAllChallenges(Resource):
    @ml.doc(description='rnn service')

    def get(self):
        mlservice = MachineLearningService()
        result_mlservice = mlservice.test()
        return result_mlservice

@ml.route('/dnn', methods=['GET'])
class ReturnAllURL(Resource):
    '''
    Deep Neural Network를 활용한 서비스
    '''
    @ml.doc(description='Deep Neural Network를 활용한 서비스의 모든 url을 반환합니다.')
    def get(self):
        result_allurl = {
            'dnn_services': "/ml",
        }
        return result_allurl