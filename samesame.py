import subprocess
import sys

def samesame(string):
    s = subprocess.Popen(["./samesame"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    s.stdin.write(bytes(string, 'utf8'))
    s.stdin.close()
    s.wait()
    return str(s.stdout.read(), 'utf8')

if __name__ == '__main__':
    print(samesame(sys.argv[1]))
