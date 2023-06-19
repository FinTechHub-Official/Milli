from rest_framework.response import Response
from api.v1.utilis.custom_responses import (
    lang_error_response,
    lang_not_given_response
)
from .not_lang_apis import get_not_lang_api
from rest_framework.renderers import JSONRenderer


class LanguageMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        if not any(request.path.startswith(endpoint) for endpoint in get_not_lang_api()):
            if not request.META.get('HTTP_ACCEPT_LANGUAGE'):
                response = Response(lang_not_given_response())
                response.accepted_renderer = JSONRenderer()
                response.accepted_media_type = "application/json"
                response.renderer_context = {}
                response.render()
                return response

            language = request.META.get('HTTP_ACCEPT_LANGUAGE')
            if language not in ['uz-LN', 'uz-KR', 'ru-RU', 'en-US']:
                response = Response(lang_error_response(lang=language))
                response.accepted_renderer = JSONRenderer()
                response.accepted_media_type = "application/json"
                response.renderer_context = {}
                response.render()
                return response

            request.lang = language
        response = self.get_response(request)
        return response

