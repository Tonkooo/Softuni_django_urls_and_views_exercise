from django.http import HttpResponse
from django.shortcuts import render

def index(request,  *args, **kwargs):
    content = f"It works with:<br/>"
    f"args={args} and kwargs={kwargs}, <br/>"
    f"path={request.path}, <br/>"
    f"method={request.method}<br/>"
    f"user={request.user}<br/>"

    return HttpResponse(content)

def index(request, *args, **kwargs):
    context = {
        "title": "Request data",
        "args": args,
        "kwargs": request.path,
        "method": request.method,
        "user": request.user,
    }
    return render(request, 'core/index.html', context)
