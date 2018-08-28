# doing some unknown stuffs
from django.core.management import execute_from_command_line
import os, django
import builtins
import threading, time
from data.derived import Derived
from data.sources import Source
from data.outcome import Outcome
from tasks import Task
from mlalgo import Runner
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "interface.settings")
# variable
builtins.info={
    "ml_server_running":False
}
builtins.tasks = []

class Interface_runner(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        "Nothing decided yet"

    def run(self):
        execute_from_command_line(['main.py', 'runserver', '0.0.0.0:8000'])

class ml_looper(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        "Nothing decided yet"

    def run(self):
        "Nothing decided yet"

threads = [None,None]
threads[0]=Interface_runner()
threads[1]=ml_looper()

#start all threads
for t in threads:
    t.start()

source = Source()
derived = Derived()
outcome=Outcome()

rn = Runner()
rn.find_derived()
rn.get_models()
builtins.models = rn.md
# infinite loop for tasks management
i=1
while True:
    
    #print('running once')

    # checking if any task for adding source/derived
    for t in builtins.tasks:
        if t.type == Task.TYPE_CtoS:
            if t.name == 'add_source':
                source.add_source(t.values)
                source.save()
                builtins.tasks.remove(t)
                # now add task to send updated sources
                builtins.tasks.append(Task("source_updated", source.get_all(), Type=Task.TYPE_StoC))
            elif t.name == 'add_derived':
                derived.add_derived(t.values)
                derived.save()
                builtins.tasks.remove(t)
                builtins.tasks.append(Task("derived_updated", derived.get_all(), Type=Task.TYPE_StoC))
            elif t.name == 'add_outcome':
                outcome.add_outcome(t.values)
                outcome.save()
                builtins.tasks.remove(t)
                builtins.tasks.append(Task("outcome_updated", outcome.get_all(), Type=Task.TYPE_StoC))
            elif t.name == 'get_all':
                builtins.tasks.remove(t)
                builtins.tasks.append(Task("source_updated", source.get_all(), Type=Task.TYPE_StoC))
                builtins.tasks.append(Task("derived_updated", derived.get_all(), Type=Task.TYPE_StoC))
                builtins.tasks.append(Task("outcome_updated", outcome.get_all(), Type=Task.TYPE_StoC))
    
    print('tasks remeining:', len(builtins.tasks))
    time.sleep(i)



#wait for all threads

print("I was nice to meet you, exiting!!!!")




