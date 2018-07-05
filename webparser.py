#*-* coding: utf-8 *-*
import urllib.request
import re
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0"
 
req = urllib.request.Request('https://proufu.ru/', headers = headers)
html = urllib.request.urlopen(req).read()
html = html.decode('utf-8')

paragraphs = re.findall(r'<p>(.*?)</p>',str(html))

for html1 in paragraphs:
    print(html1)
