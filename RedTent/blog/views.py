from django.http import HttpResponse
from django.http import FileResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import *
import json
import hashlib
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
import os

STATIC_FILE_PATH = "/home/ali/upload"
parser_class = (FileUploadParser,)


@api_view(['GET'])
def users_list(request):
    if request.method == 'GET':
        users = UserAccount.objects.all()
        data = []
        for user in users:
            data.append({"user_name": user.username, "password": user.password, "token": user.token})
    return Response(data)


@api_view(['GET'])
def get_token_for_login(request):
    data = json.loads(request.body)
    response_data = {}
    try:
        user = UserAccount.objects.get(username=data["user_name"])
        response_data = {"token": user.token}
    except:
        response_data = {"error": "this user does not exist"}
    return Response(response_data)


@api_view(['POST'])
def get_token_for_signup(request):
    response_data = {}
    try:
        data = json.loads(request.body)
        token = hashlib.md5(data["user_name"].encode()).hexdigest()
        user = UserAccount.objects.create(username=data['user_name'], password=data['password'], token=token)
        response_data ={"user_name": user.username, "token": token}
    except:
        response_data= {"error": "this user is exist"}
    return Response(response_data)


@api_view(['POST', 'GET'])
def list_of_design(request, **kwargs):
    if request.method == 'POST':
        return Response({""})

    elif request.method == 'GET':
        designs = Design.objects.all()
        return_data = []
        for design in designs:
            return_data.append({"id": design.pk, "path": design.pic})
        return Response(return_data)
    return Response({})


@api_view(['GET', 'PUT ', 'DELETE'])
def get_design(request, design_id):
    response_data = {}
    try:
        design = Design.objects.get(id=design_id)
        if request.method == 'GET':
            return Response({"design_id": Design.pk, "design_picture": Design.pic,
                             "total_rate": Design.total_rate, "view": Design.view})
        elif request.method == 'DELETE':
            id = design.pk
            design.delete()
        return Response({"id": id})
    except Design.DoesNotExist:
        response_data = {"error": "this design is not exist"}
    return Response(response_data)


@api_view(['GET', 'PUT', 'DELETE'])
def user(request, user_id):
    try:
        user = UserAccount.objects.get(pk=user_id)

    except UserAccount.DoesNotExist:
        fake_data_for_not_response = {"Fake_data": "User Does Not exist"}
        return HttpResponse(fake_data_for_not_response)
        #return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        '''
        serializer = UserSerializer(user)
        return Response(serializer.data)
        '''
        fake_user = {"Fake": "user get"}
        return HttpResponse(fake_user)

    elif request.method == 'PUT':
        '''
        serializer = UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        '''
        fake_user = {"Fake": "user_put"}
        return HttpResponse(fake_user)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST', 'GET'])
def image(request,**kwargs):
    print(kwargs)
    if request.method == 'POST':
        if 'file' not in request.data:
            raise ParseError("Empty content")

        f = request.data['file']
        image = Image.objects.create(pic=f)
        return Response({"id": image.pk, "path": image.pic.name})

    elif request.method=='GET':
        a = "/home/alibashari/PycharmProjects/red_tnet5/" + request.path.split('/')[-1]
        response = FileResponse(open(a, 'rb'))
        return response


@api_view(['POST','GET'])
def test(request,**kwargs):
    if request.method == 'GET':
        a ="/home/alibashari/PycharmProjects/red_tnet5/"+ request.path.split('/')[-1]
        response = FileResponse(open(a , 'rb'))
        return response
    file_name = json
    return Response({"asd":"hoora"})












@api_view(['GET', 'POST'])
def ListOfCollectionOfDesign(requset, UserID ):
    data ={}
    return HttpResponse(data)



@api_view(['GET', 'PUT', 'DELETE'])
def CollectionOfDesign(request, UserID, CollectionOfDesignsID):
    data = {}
    return HttpResponse(data)


@api_view(['GET','POST'])
def ListOfCommentForDesigner(requset, UserID):
    data = {}
    return HttpResponse(data)


@api_view(['GET','POST'])
def ListOfCommentForDesign(requset, UserID):
    data = {}
    return HttpResponse(data)


@api_view(['GET','POST'])
def ListOfTags(request,UserID):
    data = {}
    return HttpResponse(data)


@api_view(['GET','POST'])
def GetUserOfTag(request,TagID):
    data = {}
    return HttpResponse(data)

