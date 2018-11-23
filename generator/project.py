from model.project import Project
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of projects", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/projects.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_strings(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_boolean():
    return random.choice([False, True])


def random_status():
    list = ['development', 'release', 'stable', 'obsolete']
    return random.choice(list)


def random_view_status():
    list = ['public', 'private']
    return random.choice(list)


testdata = [Project(name=random_strings("name", 10), status=random_status(), view_state=random_view_status(),
                    inherit_global=random_boolean(), description=random_strings("description", 30))
    for name in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))