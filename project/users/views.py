from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.models import User, SerializeClass


# Create your views here.

@api_view(['GET'])
def fetch_users(req):
    users = User.objects.all()
    serializer = SerializeClass(users, many=True)
    return Response({"status": "success", "data": {"user": serializer.data}}, status=status.HTTP_200_OK)

@api_view(['GET'])
def fetch_user(req, id):
    try:
        user = User.objects.get(id=id)
        serializer = SerializeClass(user)
        return Response({"status": "success", "data": {"user": serializer.data}}, status=status.HTTP_200_OK)
    except Exception as e:
        print('Error : ' + e.__str__())
        return Response({"status": "fail", "message": 'user not found'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def save_user(req):
    serializer = SerializeClass(data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": {"user": serializer.data}}, status=status.HTTP_201_CREATED)
    else:
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_user(req, id):
    user = get_user(req, id)
    serializer = SerializeClass(user, data=req.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": {"user": serializer.data}}, status=status.HTTP_200_OK)
    else:
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_user(req, id):
    try:
        user = get_user(req, id)
        user.delete()
        return Response({"status": "success", "message": "success"}, status=status.HTTP_200_OK)
    except Exception as e:
        print('Error : ' + e)
        return Response({"status": "fail", "message": "deletion failed"}, status=status.HTTP_400_BAD_REQUEST)


############ INTERNAL FUNCTIONS ############

def get_user(req, id):
    try:
        return User.objects.get(id=id)
    except Exception as e:
        print('error : ' + e)
        return None
