from django.http import HttpResponse, HttpResponseRedirect
import builtins, json
from django.template import loader
from tasks import Task
import numpy as np
def home(request):
    builtins.tasks=[]
    if builtins.tasks == None:
        builtins.tasks=[]
    return HttpResponseRedirect("/static/index.html")

def token(request):
    temp = loader.get_template('token.html')
    return HttpResponse(temp.render(None, request))
    
def add_tasks(request):
    if request.method=='GET':
        print('get all add_tasks called ')
        builtins.tasks.append(Task('get_all',{}))
        return HttpResponse('Welcome to HomeAutomation')
    data = request.POST.getlist('values[]', None)
    print(request.POST)
    builtins.tasks.append(Task(request.POST.get('name', '#'),data))
    return HttpResponse(request.POST.get('name','#')+str(data))


def get_tasks(request):
    tasks = builtins.tasks
    val=[]
    for t in tasks:
        if t.type == Task.TYPE_StoC:
            tasks.remove(t)
            print('---',t.name)
            val.append({'name':t.name, 'values':t.values})
    return HttpResponse(json.dumps(val))

def file_upload(request):
    handle_uploaded_file(request.FILES['file'])
    return HttpResponseRedirect('/')

def handle_uploaded_file(f):
    with open('data/temp.csv', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def predict(request):
    models = builtins.models
    name = request.GET.get('outcome_name')
    cols = request.GET.get('cols').split(',')
    vals = np.reshape(request.GET.get('val').split(','), (-1,1))

    for m in models:
        if m['name']==name:
            print(str(m))
            return HttpResponse(json.dumps(m['model'].predict(vals).tolist()))
        else:print(name, "!=", m['name'])