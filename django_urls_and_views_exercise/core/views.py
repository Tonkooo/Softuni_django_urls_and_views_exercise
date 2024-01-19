from django.http import HttpResponse
from django.shortcuts import render

def index(request,  *args, **kwargs):
    content = f"It works with:<br/>"
    f"args={args} and kwargs={kwargs}, <br/>"
    f"path={request.path}, <br/>"
    f"method={request.method}<br/>"
    f"user={request.user}<br/>"

    return HttpResponse(content)

