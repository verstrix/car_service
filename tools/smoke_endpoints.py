import urllib.request
import urllib.error
import sys

base='http://127.0.0.1:5000'
endpoints=['/users/','/work-orders/']
for e in endpoints:
    url = base+e
    try:
        r = urllib.request.urlopen(url, timeout=5)
        print(url, r.getcode())
        data = r.read(400).decode('utf-8', errors='replace')
        print(data[:800])
    except urllib.error.HTTPError as he:
        print(url, 'HTTP', he.code)
        try:
            print(he.read(400).decode('utf-8', errors='replace'))
        except Exception:
            pass
    except Exception as ex:
        print(url, 'ERR', ex)
        sys.exit(2)
