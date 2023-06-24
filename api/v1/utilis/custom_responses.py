

def success_response():
    return {
        'status': True
    }


def serializer_error_response(serializer_errors):
    return {
        "status": False, 
        "errors": {**{
            key: value[0] 
            for key, value in serializer_errors.items()
        }}
    }


def lang_error_response(lang):
    return {
        'status': False,
        'error': "Given language incorrect!"
    }


def lang_not_given_response():
    return {
        'status': False,
        'error': "Language not given!"
    }

def serializer_without_paginator_res(serializer_data):
    return {
        'status': True,
        "data": serializer_data
    }

def params_error_repsonse():
    return {
        'status': False,
        "error": "Given params incorrect or not given"
    }
