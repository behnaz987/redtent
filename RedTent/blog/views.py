from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import  UserAccount


@api_view(['GET', 'POST'])
def users_list(request):
    if request.method == 'GET':
        users = UserAccount.objects.all()
        #serialize to json
        #return respons
        fake_data= {"Fake : UsersList"}
        return Response(fake_data)

