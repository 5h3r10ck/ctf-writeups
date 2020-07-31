import requests
path="http://jh2i.com:50011/site/flag.php"
s=requests.Session()
out=s.get(path).text
print(out)
