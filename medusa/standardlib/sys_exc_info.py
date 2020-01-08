import sys
try:
    1/0
except Exception:
    type, value, track = sys.exc_info()
    print(track)
    print(type)
    print(value)
