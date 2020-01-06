import subprocess

p = subprocess.Popen("ls -a", shell=True)
p.wait()
p = subprocess.Popen(args=['ls', '-l'])
p.wait()

