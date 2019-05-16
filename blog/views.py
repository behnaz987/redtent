from django.http import HttpResponse
from django.http import FileResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import *
import json
import hashlib
import os
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser


STATIC_FILE_PATH = "/home/ali/upload"
parser_class = (FileUploadParser,)

rt_static_path = "mnt/d/Self/Projects/University/SE/redtent/files/"

#login
@api_view(['POST'])
def get_token_for_login(request):
    response_data = {}
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            user = UserAccount.objects.get(username=data["user_name"])
            response_data = {"token": user.token}
        except:
            response_data = {"error": "this user does not exist"}

    return Response(response_data)


#signup
@api_view(['POST', 'GET'])
def get_token_for_signup(request):
    response_data = {}
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            token = hashlib.md5(data["user_name"].encode()).hexdigest()
            user = UserAccount.objects.create(username=data["user_name"], password=data["password"], token=token)
            response_data = {"user_name": user.username, "token": token}
        except :
            response_data = {"error": "this user is exist"}
    return Response(response_data, content_type='application/json')


#design_list
@api_view(['POST', 'GET'])
def list_of_design(request,*args, **kwargs):
    if request.method == 'POST':
        data = json.loads(request.body)
        design = Design.objects.create(**data)
        return Response({"id": design.pk, "pic": design.pic})
    elif request.method == 'GET':
        designs = []
        _from = 0
        _row = 10
        if "_from" in kwargs.keys() and kwargs["_from"]:
            _from = int(kwargs["_from"])
        if "_row" in kwargs.keys() and kwargs["_row"]:
            _row = int(kwargs["_row"])
        if "_order_by" in kwargs.keys() and kwargs["_order_by"]:
            designs = Design.objects.filter().order_by('-'+kwargs["_order_by"])[_from:_row]
        else:
            designs = Design.objects.all()[_from:_row]
        return_data = []
        for design in designs:
            return_data.append({"id": design.pk, "path": design.pic, "view": design.view, "rate": design.total_rate})
        return Response(return_data)
    return Response({})


#one_design_function
@api_view(['GET', 'PUT ', 'DELETE'])
def get_design(request, design_id):
    response_data = {}
    try:
        design = Design.objects.get(id=design_id)
        if request.method == 'GET':
            design.view+=1
            design.save()
            response_data = {"design_id": design.pk, "design_picture": design.pic,
                             "total_rate": design.total_rate, "view": design.view}

        elif request.method == 'DELETE':
            id = design.pk
            design.delete()
            response_data = {"id": id}
        elif request.method == 'PUT':
            Design.objects.update_or_create(pk=design.pk)
    except Design.DoesNotExist:
        response_data = {"error": "this design is not exist"}
    return Response(response_data)


@api_view(['POST', 'GET'])
def image(request,**kwargs):
    if request.method == 'POST':
        if 'file' not in request.data:
            raise ParseError("Empty content")

        f = request.data['file']
        image = Image.objects.create(pic=f)
        return Response({"id": image.pk, "path": image.pic.name})

    elif request.method=='GET':
        a = rt_static_path + request.path.split('/')[-1]
        response = FileResponse(open(a, 'rb'))
        return response


@api_view(['POST', 'GET'])
def test(request,**kwargs):
    if request.method == 'GET':
        a = rt_static_path + request.path.split('/')[-1]
        response = FileResponse(open(a , 'rb'))
        return response
    file_name = json
    return Response({"asd":"hoora"})


#tags_of_design
@api_view(['GET', 'POST'])
def list_of_design_tags(request, **kwargs):
    if request.method == 'GET':
        design = Design.objects.get(pk=kwargs["design_id"])
        tags = design.tag.all()
        return_data = []
        for tag in tags:
            return_data.append({"tag_id": tag.pk, "tag_body": tag.body})

        return Response(return_data)

    elif request.method == 'POST':
        data = json.loads(request.body)
        design = Design.objects.get(pk=kwargs['design_id'])
        tag = Tag.objects.get_or_create(body=data["body"])[0]
        design.tag.add(tag)
        return Response({"tag_id": tag.pk, "body": data["body"]})


#delete tag from the certain design
@api_view(['DELETE', 'GET'])
def delete_design_tag(request,*args,**kwargs):
    if request.method == 'DELETE':
        design = Design.objects.get(pk=kwargs["design_id"])
        tag = Tag.objects.get(pk=kwargs['tag_id'])
        tag_id = tag.pk
        design.tag.remove(tag)
        return Response({"tag was deleted": tag_id})


#get rate of certain design
@api_view(['GET'])
def get_myrate(request,design_id, **kwargs):
    token = request.headers["Authorization"]
    user = UserAccount.objects.get(token=token)
    rate = RateForDesign.objects.filter(design=design_id).filter(user=user.pk)[0]
    return Response({"rate": rate.rate})


@api_view(['GET', 'POST'])
def list_of_rates_for_design(request, **kwargs):
    if request.method == 'GET':
        _from = 0
        _row = 10
        if "_from" in kwargs.keys():
            _from = kwargs["_from"]
        if "_row" in kwargs.keys():
            _row = kwargs["_row"]
        rates = RateForDesign.objects.all(design=kwargs["design_id"])[_from:_row]
        return_data = []
        for rate in rates:
            return_data.append({"rate": rate.rate, "design": rate.design, "user": rate.user})
            return Response(return_data)
    elif request.method == 'POST':
        try:
            rateNo = json.loads(request.body)["rate"]
            headers = request.headers
            token = headers["Authorization"]
            user = UserAccount.objects.get(token=token)
            design = Design.objects.get(pk=kwargs["design_id"])
            rate_for_design = RateForDesign.object.create(rate=rateNo, design=design, user=user)
            return Response({"rate": rateNo, "user_account": user.pk, "design": design.pk})
        except:
            return {"This Rate Does Not Exist"}


@api_view(["GET"])
def all_rate_for_user(request, **kwargs):
    headers = request.headers
    token = headers["Authorization"]
    user = UserAccount.objects.get(token=token)
    rates = RateForDesign.objects.all(user=user.pk)
    return_date = []
    for rate in rates:
        return_date.append({"rate": rate.rate, "design": rates.design.pic})
    return Response(return_date)


#
@api_view(["GET", "PUT", "DELETE"])
def rate_for_design_operations(request,rate_for_design_Id,*args,**kwargs):
    if request.method == "GET":
        rate = RateForDesign.objects.get(id=rate_for_design_Id)
        user = rate.user
        design = rate.design
        return Response({"rate": rate.rate, "user": user.pk, "design": design.pk})
    if request.method == "PUT":
        newrate = json.loads(request.body)["rate"]
        rate = RateForDesign.objects.get(id=rate_for_design_Id)
        rate.rate = newrate
        rate.save()
        return Response({"rate_id": rate_for_design_Id, "rate": rate.rate})
    if request.method == "DELETE":
        rate = RateForDesign.objects.get(id=rate_for_design_Id)
        rate_id = rate.pk
        rate.delete()
        return Response({"deleted_rate": rate_id})


#
@api_view(['POST', 'GET'])
def list_of_comments_for_design(request, **kwargs):
    if request.method == 'GET':
        _from = 0
        _row = 10
        if "_from" in kwargs.keys():
            _from = kwargs["_from"]
        if "_row" in kwargs.keys():
            _row = kwargs["_row"]
        comments = CommentForDesign.objects.all(design=kwargs["design_id"])[_from:_row]
        return_data = []
        for comment in comments:
            if comment.isValid:
                return_data.append({"body": comment.body, "design": comment.design, "user": comment.user})
                return Response(return_data)

    elif request.method == 'POST':
        data = json.loads(request.body)["body"]
        try:
            design = Design.objects.get(pk=kwargs['design_id'])
            headers = request.headers
            token = headers["Authorization"]
            user = UserAccount.objects.get(token=token)
            comment = CommentForDesign.objects.create(body=data, isValid=False, user=user, design=design)
            return Response({"body": comment.body, "isValid": comment.isValid, "design": design.pk, "user": user.pk})
        except:
            return Response({"error": "design is not exist"})
'''
    elif request.method == 'PUT':
        data = json.loads(request.body)["body"]
        try:
            design = Design.objects.get(pk=kwargs['design_id'])
            headers = request.headers
            token = headers["Authorization"]
            user = UserAccount.objects.get(token=token)
            comment = CommentForDesign.objects.filter(user=user).filter(design=design)[0]
            
            return Response({"body": comment.body, "isValid": comment.isValid, "design": design.pk, "user": user.pk})
'''


@api_view(['GET', 'DELETE'])
def comment_for_design_operations(request, **kwargs):
    if request.method == "GET":
        try:
            comment = CommentForDesign.objects.get(pk=kwargs['comment_Id'])
            if comment:
                return Response({"body": comment.body, "isValid": comment.isValid, "design": comment.design, "user": comment.user})
        except:
            return Response({"this comment is not exist"})
    if request.method == "DELETE":
        try:
            headers = request.headers
            token = headers["Authorization"]
            user = UserAccount.objects.get(token=token)
            comment = CommentForDesign.objects.get(pk=kwargs['comment_Id'])
            if comment:
                if comment.user.pk == user.pk:
                    comment.delete()
                    return Response({"Comment was deleted"})
                else:
                    return Response({"This user cannot delete this comment"})
        except:
            raise ("this comment is not exist")


@api_view(['GET', 'POST'])
def list_of_a_post_designers(request, design_id, **kwargs):
    if request.method == "GET":
        try:
            design = Design.objects.get(pk=design_id)
            if design:
                designers = Design.designer.objects.all()
                return_data = []
                for designer in designers:
                    return_data.append({"designer": os.path.join("designers", str(designer.pk))})
                return Response(return_data)
        except:
            raise ("this design is not exist")
    if request.method == "POST":
        data = json.loads(request.body)
        design = None
        try:
            design = Design.objects.get(pk=design_id)
        except:
            if design:
                headers = request.header
                token = headers["Authorization"]
                user = UserAccount.objects.get(token=token)
                if user.isDesigner:
                    designer = Designer.objects.get_or_create(**data)
                    design.designer.add(designer)
                    return Response({"designer_id": designer.pk})
                else:
                    return Response({"Access Denied"})


@api_view(["GET", "POST"])
def list_of_all_designers(request, **kwargs):
    if request.method == "GET":
        _from = 0
        _row = 10
        if _from in kwargs.keys():
            _from = kwargs["_from"]
        if _row in kwargs.keys():
            _row = kwargs["_row"]
        designers = Designer.objects.all()
        return_data = []
        for designer in designers:
            return_data.append({"designer": designer.pk})
        return Response(return_data)
    '''
    if request.method == "POST":
        designer = Designer.objects.create(**data)
        design.designer.add(designer)
        return Response({"designer_id": designer.pk})
    '''
@api_view(["GET", "PUT", "DELETE"])
def designer_operation(request, **kwargs):
    if request.method == "GET":
        headers = request.header
        token = headers["Authorization"]
        designer = Design.objects.get(pk=kwargs['designer_id'])
        if designer:
            return Response({"firstname": designer.firstname, "lastname": designer.lastname, "username": designer.username,
                             "password": designer.password, "tag": designer.tag, "token": token,
                             "phonenumber": designer.phoneNumber
                           , "city": designer.city, "address": designer.address, "comments": designer.comments,
                             "rates": designer.rates})


@api_view(['GET', 'POST'])
def user_collection_of_designs(request, **kwargs):
    headers = request.header
    token = headers["Authorization"]
    user = UserAccount.objects.get(token=token)
    if request.method == "GET":
        try:
            _from = 0
            _row = 10
            if _from in kwargs.keys():
                    _from = kwargs["_from"]
            if _row in kwargs.keys():
                    _row = kwargs["_row"]
            collections = CollectionOfDesign.objects.all(user=user.pk)[_from:_row]
            return_data = []
            for collection in collections:
                return_data.append({"title": collection.title, "pic": collection.callPic.pk, "useraccount": collection.userAccount.pk})
            return Response(return_data)
        except:
            return Response({"error":"this user is not exist"})
    elif request.method == "POST":
        data = json.loads(request.body)
        data["user"] = user.pk
        collection = CollectionOfDesign.objects.create(**data)
        return Response({"id":collection.pk})

'''
@api_view(['GET','PUT', 'DELETE'])
def collection_of_design_operations(requset, **kwargs):
    collection =None
    collection = CollectionOfDesign.objects.get(pk=kwargs['collection_of_design_id'])
    if collection:
        if requset.method == "GET":
            try:
                if collection:
                    return Response({"title": collection.title, "collpic":collection.callPic, "useraccount": collection.user})
            except:
                raise ("This collection is not exist")
        if requset.method == "PUT":
            collection =CollectionOfDesign.objects.create(????)
        if requset.method == "DELETE":
            collection.delete()
            return Response({"Collection was deleted"})

'''
@api_view(['GET', 'POST'])
def user_collection_of_designers(request, UserID ,**kwargs):
    headers = request.header
    token = headers["Authorization"]
    user = UserAccount.objects.get(token=token)
    if request.method == "GET":
        try:
            _from = 0
            _row = 10
            if _from in kwargs.keys():
                    _from = kwargs["_from"]
            if _row in kwargs.keys():
                    _row = kwargs["_row"]
            collections = CollectionOfDesigner.objects.all(user=user.pk)[_from:_row]
            return_data = []
            for collection in collections:
                return_data.append({"title": collection.title, "pic": collection.callPic.pk,
                                    "useraccount": collection.user.pk})
            return Response(return_data)
        except:
            return Response({"error": "this user is not exist"})
    elif request.method == "POST":
        data = json.loads(request.body)
        data["user"] = user.pk
        collection = CollectionOfDesigner.objects.create(**data)
        return Response({"id": collection.pk})


@api_view(['GET', 'PUT', 'DELETE'])
def CollectionOfDesign(request, UserID, CollectionOfDesignsID):
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
