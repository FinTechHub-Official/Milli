import jwt
from django.conf import settings
from django.contrib.auth import user_logged_in
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework_jwt.serializers import jwt_payload_handler

from api.v1.user.models import User


# Create your views here.


class LoginView(GenericAPIView):
    def post(self, requests, *args, **kwargs):
        data = requests.data

        if data is None:
            return Response({
                "Error": "Data to`ldirilmagan"
            })

        nott = 'phone_number' if 'phone_number' not in data else 'password' if 'password' not in data else None
        if nott:
            return Response({
                "Error": f"{nott} to`ldirilmagan"
            })
        user = User.objects.filter(phone_number=data['phone_number']).first()

        if not user:
            return Response({
                "Error": "Bunday foydalanuvchi mavjud emas"
            })
        if not user.check_password(data['password']):
            return Response({
                "Error": "Parol notog`ri kiritilgan"
            })
        print("asad,sdasasdasas")
        token = Token.objects.get_or_create(user=user)[0]

        return Response({
            "Success": token.key,
            "user": user.format()
        })


    def authenticate_user(request):
        try:
            email = request.data['email']
            password = request.data['password']
            user = User.objects.get(email=email, password=password)
            if user:
                try:
                    payload = jwt_payload_handler(user)
                    token = jwt.encode(payload, settings.SECRET_KEY)
                    user_details = {}
                    user_details['name'] = "%s %s" % (
                        user.first_name, user.last_name)
                    user_details['token'] = token
                    user_logged_in.send(sender=user.__class__,
                                        request=request, user=user)
                    return Response(user_details, status=status.HTTP_200_OK)
                except Exception as e:
                    raise e
            else:
                res = {
                    'error': 'can not authenticate with the given credentials or the account has been deactivated'}
                return Response(res, status=status.HTTP_403_FORBIDDEN)
        except KeyError:
            res = {'error': 'please provide a email and a password'}
            return Response(res)
