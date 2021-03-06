import json
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
# from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from seekrapi.models import User

@csrf_exempt
def login_user(request):
    req_body = json.loads(request.body.decode())

    if request.method == 'POST':
        username = req_body['username']
        password = req_body['password']
        authenticated_user = authenticate(username=username, password=password)

        if authenticated_user is not None:
            token = Token.objects.get(user=authenticated_user)
            current_user = authenticated_user
            data = json.dumps({"valid": True, "token": token.key, "user_id": current_user.id, "is_seeker": current_user.is_seeker})
            return HttpResponse(data, content_type='application/json')
        else:
            data = json.dumps({"valid": False})
            return HttpResponse(data, content_type='application/json')


@csrf_exempt
def register_user(request):
    req_body = json.loads(request.body.decode())

    new_user = User.objects.create_user(
        username=req_body['email'],
        email=req_body['email'],
        password=req_body['password'],
        first_name=req_body['first_name'],
        last_name=req_body['last_name'],
        is_seeker=req_body['is_seeker']
    )

    token = Token.objects.create(user=new_user)
    data = json.dumps({"token": token.key, "user_id": new_user.id, "is_seeker": new_user.is_seeker})
    return HttpResponse(data, content_type='application/json')
