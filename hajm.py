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
pack=list(re.finditer('مگابایت', mow))
start_s = pack[0].start() - 50
end_s = pack[0].end() + 50
volume =''.join(re.findall('\d+', mow[start_s:end_s]))
cal_volume = int(volume) / 1024 / 4
print ("hajm baghimande = %.2f GB" % cal_volume)
print ("rooz baghimande = %s rooz" % rooz)
