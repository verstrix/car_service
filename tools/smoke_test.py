import urllib.request
import time
import sys

url = 'http://127.0.0.1:5000'
for i in range(20):
    try:
        r = urllib.request.urlopen(url, timeout=5)
        status = r.getcode()
        data = r.read(2048).decode('utf-8', errors='replace')
        print('STATUS', status)
        print(data[:1000])
        sys.exit(0)
    except Exception as e:
        print('retry', i, str(e))
        time.sleep(0.5)
print('FAILED')
sys.exit(2)
