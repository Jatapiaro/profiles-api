from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

## Auth
from rest_framework.authentication import TokenAuthentication

## Filters
from rest_framework import filters

## Oauth
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets

from . import serializers
from . import models
from . import permissions

# Create your views here.

class HelloApiView(APIView):
    """  Test API View. """

    serializer_class = serializers.HelloSerializer

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


class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code.'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles getting an object by its ID."""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handles updating an object."""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating part of an object."""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handles creating and updates of profiles """
    serializer_class = serializers.UserProfileSerializer
    ## SomeModel.objects.all() => returns all entries of a model
    queryset =  models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', "email")


class LoginViewSet(viewsets.ViewSet):
    def create(self, request):
        """ Use the ObtainAuthToken ApiView to validate and create a token """
        return ObtainAuthToken().post(request)

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """ Handles creating and updates of profiles """
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)
