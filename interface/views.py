from django.http import HttpResponse, HttpResponseRedirect
import builtins
from django.template import loader

def home(request):
    builtins.tasks=[]
    if builtins.tasks == None:
        builtins.tasks=[]
    return HttpResponseRedirect("/static/index.html")

def token(request):
    temp = loader.get_template('token.html')
    return HttpResponse(temp.render(None, request))
    
def add_tasks(request):
    data = request.POST.getlist('values[]')
    print(data)
    return HttpResponse(request.POST.get('type','#')+str(data))