import subprocess

p = subprocess.Popen("ls -a", shell=True)
p.wait()