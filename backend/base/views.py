from django.shortcuts import render
from rest_framework.response import Response
# from .models import Person, Musician, Car
from .models import User, Role, Rule
from rest_framework.decorators import api_view
# from .serializer import PersonSerializer, MusicianSerializer
from .serializer import UserSerializer, RoleSerializer, RuleSerializer
import logging
from rest_framework import status
#
# # Create your views here.
#
#


@api_view(['GET'])
def get_routes(request):
    routes = [
        '/api/person/',
    ]
    return Response(routes)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def get_user(request):
    # logging.warning(request)
    if request.method == 'GET':
        """List all users"""
        user = User.objects.all()
        # logging.warning('here')
        # logging.warning(user)
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        """ create a new user """
        logging.warning(request.data)
        serializer = UserSerializer(data=request.data)
        logging.warning('POST')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        """ Update user data """
        user_obj = User.objects.get(pk=6)
        serializer = UserSerializer(user_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        """ Delete user """
        user_obj = User.objects.get(pk=9)
        user_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def rule_list(request):
    logging.warning("Here")
    logging.warning(request)
    if request.method == 'GET':
        rule = Rule.objects.all()
        serializer = RuleSerializer(rule, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        """ create a new rule """
        logging.warning(request.data)
        serializer = RuleSerializer(data=request.data)
        logging.warning('POST')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        rule_obj = Rule.objects.get(pk=3)
        serializer = RuleSerializer(rule_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        rule_obj = Rule.objects.get(pk=3)
        rule_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def role_list(request):
    # logging.warning(request.query_params['_id'])
    # role_object = Role.objects.get('_id')
    # logging.warning(role_object.data)
    if request.method == 'GET':
        role_obj = Role.objects.all()
        # logging.warning(role_obj)
        serializer = RoleSerializer(role_obj, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        """ create a new role """
        logging.warning(request.data)
        serializer = RoleSerializer(data=request.data)
        logging.warning('POST')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        role_obj = Role.objects.get(pk=3)
        serializer = RoleSerializer(role_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        role_obj = Role.objects.get(pk=4)
        role_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET'])
# def getRoutes(request):
#     person = Person.objects.all()
#     serializer = PersonSerializer(person, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def getPerson(request):
#     person_obj = Person.objects.all()
#     print(type(person_obj))
#     person_serializer = PersonSerializer(person_obj, many=True)
#     print(type(person_serializer))
#     logging.warning('here')
#     car = Car('Civic', 'Honda')
#     print(car)
#     return Response(person_serializer.data)
#
#
# @api_view(['GET'])
# def getMusician(request):
#     musician_obj = Musician.objects.all()
#     musician_serializer = MusicianSerializer( musician_obj, many=True)
#     return Response(musician_serializer.data)
