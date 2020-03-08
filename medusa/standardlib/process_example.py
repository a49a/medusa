import subprocess

p = subprocess.Popen("ls", shell=True)
a = p.poll()
print(a)
# p = subprocess.Popen(args=['ls', '-l'])
p.wait()

