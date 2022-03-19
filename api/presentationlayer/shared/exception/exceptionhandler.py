
from http.client import BAD_REQUEST, INTERNAL_SERVER_ERROR, NOT_FOUND
from typing import Final
from flask import jsonify

class NotFoundException(Exception):
    
    def __init__(self, message: str):
        self.message = message

    @staticmethod
    def error_response(e):
        if hasattr(e, 'message'):
            response = {'code': NOT_FOUND, 'message': e.message}

        response = {
            'code': NOT_FOUND,
            'message': '指定したリソースがみつかりません。'
        }
        return jsonify(response), NOT_FOUND


class BadRequestException(Exception):

    def __init__(self, value: str):
        self.value = value
        
    @staticmethod
    def error_response(e):
        return jsonify({
            'code' : BAD_REQUEST, 'message' : e.value
            }), BAD_REQUEST


class InternalServerException(Exception):

    @staticmethod
    def error_response(e):
        return jsonify({
            'code' : INTERNAL_SERVER_ERROR,
            'message' : "エラーが発生しました"
        }), INTERNAL_SERVER_ERROR
