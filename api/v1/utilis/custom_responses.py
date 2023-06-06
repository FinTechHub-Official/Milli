

def success_response():
    return {
        'status': True
    }


def serializer_error_response(serializer_errors):
    return {"status": False, "errors": {**{key: value[0] for key, value in serializer_errors.items()}}}
