import os
import threading
import secrets

from rest import rnn
from config_variable import logger
from flask_restplus.resource import Resource
from flask import request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from service_rnn import RNNService
from time import gmtime, strftime

@rnn.route('/', methods=['GET'])
class ReturnAllURL(Resource):
    '''
    존재하는 모든 api 접근 url 반환하는 서비스
    '''
    @rnn.doc(description='존재하는 모든 api의 접근 url을 반환합니다.')
    def get(self):
        result_allurl = {
            'all_services': "/rnn",
        }
        return result_allurl

@rnn.route('/rnn', methods=['GET'])
class ReturnAllChallenges(Resource):
    @rnn.doc(description='rnn service')

    def get(self):
        rnnservice = RNNService()
        result_rnnservice = rnnservice.test()
        return result_rnnservice