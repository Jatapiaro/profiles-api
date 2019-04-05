from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

# Create your views here.

class HelloApiView(APIView):
    """  Test API View. """

    serializers_class = serializers.HelloSerializer

    def get(self, request, format="None"):
        """ Return a list of api view features. """
        an_apiView = [
            'Uses HTTP methods as function (get, post, put, delete)',
            'It is similar to a traditional DJANGO view'
        ]
        return Response({'message': 'Hello', 'an_apiView': an_apiView})

    def post(self, request):
        """ Create a hello message with our name """
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}!'.format(name)
            return Response({'message': message})

        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """ Handles an update """
        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """ Handles an update """
        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """ Handles an update """
        return Response({'method': 'delete'})