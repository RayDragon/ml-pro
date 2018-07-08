# doing some unknown stuffs
from django.core.management import execute_from_command_line
import os, django
import builtins
import threading, time

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

#wait for all threads
threads[1].join()

print("I was nice to meet you, exiting!!!!")




