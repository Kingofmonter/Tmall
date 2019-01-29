import requests
import js2xml
import json
from bs4 import BeautifulSoup
from lxml import etree
url = 'https://detail.m.tmall.com/item.htm?id=575606465103'

res = requests.get(url=url)

soup = BeautifulSoup(res.text,'lxml')

scr = soup.select('script')[-6].string

scr_text = js2xml.parse(scr,debug=False)

scr_tree = js2xml.pretty_print(scr_text)

# print(scr_tree)

selector = etree.HTML(scr_tree)

content = selector.xpath("//property[@name='基本信息']/array//object/property/string/text()")

print(content)