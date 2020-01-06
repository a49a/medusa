import os, sys

r, w = os.pipe()

processid = os.fork()

if processid:
    os.close(w)
    r = os.fdopen(r)
    print("parent read")
    string = r.read()
    print("parent read :", string)
    r.close()
    sys.exit(0)
else:
    os.close(r)
    w = os.fdopen(w, 'w')
    print("child w")
    w.write("hello ha")
    w.close()
    sys.exit(0)
