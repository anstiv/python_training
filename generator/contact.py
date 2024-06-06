from model.contact import Contact
import random
import string
import os.path
import getopt
import sys
import jsonpickle


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits+string.punctuation+" "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", address="", home="", mobile="", work="",
            email="", email2="", email3="")] + [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 15),
            address=random_string("address", 30), home=random_string("home", 12),
            mobile=random_string("mobile", 12), work=random_string("work", 12),
            email=random_string("email", 20), email2=random_string("email2", 20),
            email3=random_string("email3", 20)) for i in range(n)]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
