import sys

try:
    __import__("secrets")
except ImportError:
    print("no secrets.py file created, please do that with a DATABASE_URI")
    sys.exit(-1)
else:
    print("secrets.py exists!")
