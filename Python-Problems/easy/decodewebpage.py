import requests
import BeautifulSoup

url = 'http://github.com'
r = requests.get(url)
r_html = r.text

print(r_html)
