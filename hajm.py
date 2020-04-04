from bs4 import BeautifulSoup
import requests
import re
url = 'http://panel.hiweb.ir/panel.php?logout='
result = requests.get(url)
soup = BeautifulSoup(result.content, features = 'html5lib')
token_hash = soup.find('input', attrs = {'name' : 'token_hash'})['value']
panel_login = soup.find('input', attrs = {'name' : 'panel_login'})['value']
headers = {
    'Content-type': 'application/json',
}
payload = {
        'user' : '',
        'pass' : '',
        'panel_login' : panel_login,
        'token_hash' : token_hash
        }
page = requests.post('http://panel.hiweb.ir', data=payload, headers=headers)
soup2 = BeautifulSoup(page.content, features = 'html5lib')
mow = str(soup2.find_all('script')[9])
rooz = re.findall('\d+ روز', mow)[0]
rooz = re.findall('\d+', rooz)[0]
mow = int(''.join(re.findall('\d+', mow[2300:2400]))) / 1024 / 4
f_day = int(re.findall('\d+', rooz)[0]) / 30 * 94
print ("hajm baghimande = %.2f GB" % mow)
print ("rooz baghimande = %s rooz" % rooz)
