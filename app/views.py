from django.shortcuts import render,HttpResponse

from oauth2_provider.contrib.rest_framework import TokenHasScope
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasScope

# Create your views here.

def test(request):
    return HttpResponse("hello")


class ProtectedView(APIView):
    authentication_classes = [OAuth2Authentication]

    permission_classes = [TokenHasScope]
    required_scopes = ['write']

    def get(self, request):
        
        return Response('hello')


def callback(request):
    try:
        print(request.GET)
    except Exception as e:
        print(e)
    return HttpResponse("hello")    