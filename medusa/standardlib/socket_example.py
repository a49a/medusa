import os
import socket
import tempfile

sock = socket.socket(socket.AF_UNIX)
sock.settimeout(40)

temp_dir = tempfile.mkdtemp(prefix="foo_", dir="/tmp")
print(temp_dir)
address = os.path.join(temp_dir, "python_socket")
sock.bind(address)
sock.listen(4)

os.rmdir(temp_dir)
sock.close()