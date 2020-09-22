#!/bin/python
import json
import requests
from config import username, password

#disable warning for not using ssl!
requests.packages.urllib3.disable_warnings()

url = 'https://panel.hiweb.ir/login'
api_url = 'https://panel.hiweb.ir/bundle/ActiveProduct_Read'

payload = {
    'Username': username,
    'Password': password,
    'Captcha': '0000'
}

api_payload = {
    "JsonString": '{"draw":1,"columns":[{"data":0,"name":"","searchable":false,"orderable":false,"search":{"value":"","regex":false}},{"data":1,"name":"","searchable":false,"orderable":false,"search":{"value":"","regex":false}},{"data":2,"name":"","searchable":false,"orderable":false,"search":{"value":"","regex":false}},{"data":3,"name":"","searchable":false,"orderable":false,"search":{"value":"","regex":false}},{"data":4,"name":"","searchable":false,"orderable":false,"search":{"value":"","regex":false}},{"data":5,"name":"","searchable":false,"orderable":false,"search":{"value":"","regex":false}},{"data":6,"name":"","searchable":false,"orderable":false,"search":{"value":"","regex":false}}],"order":[{"column":0,"dir":"asc"}],"start":0,"length":10,"search":{"value":"","regex":false},"advanceSearch":[{"name":"CustomerServiceId","value":"1cf678ad-fe5e-40ac-9b14-da32e31120ab"}]}'
}

s = requests.session()
s.post(url, data=payload, verify=False)
res = s.post(api_url, data=api_payload, verify=False)
js = json.loads(res.content)
service_name = json.loads(js['data'][0][2])['ProductName']
expire_date = json.loads(js['data'][0][-1])['ExpirationDate']
remain_traffic = int(json.loads(js['data'][0][-3])['RemainTraffic']) / 4096

print('Expire date: %s' % expire_date)
print('Available volume to use: %.2f GB' % remain_traffic)
print("Service name: %s" % service_name)

# This code belong to current version of hiweb\
# website application that implemented with seleinum\
# that have lower speed versus current version!
#
# import re
# import os
# import time
# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options

# driver_path = '%s/.wdm/drivers/chromedriver/linux64/80.0.3987.106/chromedriver' % os.getenv('HOME')
# chrome_options = Options()
# chrome_options.add_argument("headless")
# chrome_options.add_argument("--disable-images")
# browser = webdriver.Chrome(driver_path, options=chrome_options)
# browser.get('https://panel.hiweb.ir/login')
# browser.find_element_by_id('Username').send_keys(username)
# browser.find_element_by_id('Password').send_keys(password)
# browser.find_element_by_css_selector('input.btn').send_keys(Keys.ENTER)
# browser.get('https://panel.hiweb.ir/bundle/list')
# notfound = True
# while notfound:
#     try:
#         time.sleep(0.75)
#         soup = BeautifulSoup(browser.page_source, features='lxml')
#         res = soup.findAll('td', attrs={'class': ['fanum', 'ltr', 'text-center']})
#         volume = re.findall('\d+', res[3].getText())[0]
#         real_vol = int(volume) / 1024 / 4
#         expire_date = res[5].getText().split(' ')[2]
#         notfound = False
#     except:
#         pass
# browser.stop_client()
# browser.close()
# print('Expire date: %s' % expire_date)
# print('Available volume to use: %.2f GB' % real_vol)


# THIS CODE BELONG TO PREVIOUS VERSION OF HIWEB 
#
#
# url = 'http://panel.hiweb.ir/panel.php?logout='
# result = requests.get(url)
# soup = BeautifulSoup(result.content, features = 'html5lib')
# token_hash = soup.find('input', attrs = {'name' : 'token_hash'})['value']
# panel_login = soup.find('input', attrs = {'name' : 'panel_login'})['value']
# headers = {
#     'Content-type': 'application/json',
# }
# payload = {
#         'user' : username,
#         'pass' : password,
#         'panel_login' : panel_login,
#         'token_hash' : token_hash
#         }
# page = requests.post('http://panel.hiweb.ir', data=payload, headers=headers)
# soup2 = BeautifulSoup(page.content, features = 'html5lib')
# mow = str(soup2.find_all('script')[9])
# rooz = re.findall('\d+ روز', mow)[0]
# rooz = re.findall('\d+', rooz)[0]
# pack = re.finditer('مگابایت', mow)
# hajm = []
# for vol in pack:
#     hajm.append((vol.start() - 30, vol.end() + 30))
# #start_s = pack[0].start() - 50
# #end_s = pack[0].end() + 50
# for counter in range(len(hajm)):
#     volume =''.join(re.findall('\d+', mow[hajm[counter][0]:hajm[counter][1]]))
#     cal_volume = int(volume) / 1024 / 4
#     if counter == len(hajm) - 1:
#         print ("Hajm baghimade Kol = %.2f GB" % cal_volume)
#     else:
#         print ("hajm baghimande = %.2f GB" % cal_volume)
# print ("rooz baghimande = %s rooz" % rooz)
