# -*- coding: utf-8 -*-
import scrapy
import json,requests,time,js2xml,random
from bs4 import BeautifulSoup
from lxml import etree
from scrapy import Request
from urllib import parse
from Tmall.items import *


class UniqloSpider(scrapy.Spider):
    name = 'uniqlo'
    allowed_domains = ['https://uniqlo.m.tmall.com']
    start_urls = ['https://uniqlo.m.tmall.com/shop/shop_auction_search.do']

    url = 'https://uniqlo.m.tmall.com/shop/shop_auction_search.do'

    shop_url_list = [   'https://xiaomi.m.tmall.com/',
                        'https://samsung.m.tmall.com/',
                        'https://sanzhisongshu.m.tmall.com/',
                        'https://dell.m.tmall.com/',
                        'https://aocsm.m.tmall.com/',
                        'https://casio.m.tmall.com/',
                        'https://yamaha.m.tmall.com/',
                        'https://hkcshuma.m.tmall.com/',
                        'https://nanjiren.m.tmall.com/',
                        'https://clarks.m.tmall.com/',
                        'https://ecco.m.tmall.com/',
                        'https://luotuo.m.tmall.com/',
                        'https://aokang.m.tmall.com/',
                        'https://yearcon.m.tmall.com/',
                        'https://oppo.m.tmall.com/',
                        'https://huawei.m.tmall.com/',
                        'https://apple.m.tmall.com/',

                    ]

    def __init__(self):
        '''
        设置请求体
        '''
        self.loginHeaders = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no - cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        }

        self.Cookies = {
            "cna": "3EzDFKJ4vQ4CASe6AWtcsXTO",
            "otherx": "e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0",
            "x": "__ll%3D-1%26_ato%3D0",
            "enc": "XYbWiH79N1WWwGx2KaI4YBLDXcPqp0MFQrCN5vR1tLKt4wLacc8S6jp0uLChfEqEYN%2Fr1Rx4EAsAsUdAU3BPBg%3D%3",
            "hng": "CN%7Czh-CN%7CCNY%7C156",
            "lid": "%E5%A4%A7%E5%B8%88%E5%87%B6%E5%BC%80%E8%BD%A6",
            "sm4": "330300",
            "OZ_1U_2061": "vid=vc49b5519c5445.0&ctime=1548399278&ltime=1548394436",
            "t": "7405b45349652071ba62cf4872d4e794",
            "tracknic": "%5Cu5927%5Cu5E08%5Cu51F6%5Cu5F00%5Cu8F66",
            "lg": "%5Cu5927%5Cu5E08%5Cu51F6%5Cu5F00%5Cu8F66",
            "_tb_token_": "hpOPEuxOa4d8gGUI904N",
            "cookie2": "186acad2b43ea8f50f5fbf5e192469ad",
            "uc1": "cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&cookie21=UIHiLt3xThH8t7YQoFNq&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&existShop=false&pas=0&cookie14=UoTYPmSMpkNNOg%3D%3D&tag=8&lng=zh_CN",
            "uc3": "vt3=F8dByE7Z5vl%2FVL6dL4Q%3D&id2=UUGmvJzxG6Nt%2FA%3D%3D&nk2=1z87i2MA%2Br%2F4Ow%3D%3D&lg2=UIHiLt3xD8xYTw%3D%3D",
            "_l_g_": "Ug%3D%3D",
            "ck1": "",
            "unb": "2942885169",
            "cookie1": "BxNUPBrMWOoRBp74g4fzDzf%2BNwUzPxGRxfafMmQ22vQ%3D",
            "login": "true",
            "cookie17": "UUGmvJzxG6Nt%2FA%3D%3D",
            "_nk_": "%5Cu5927%5Cu5E08%5Cu51F6%5Cu5F00%5Cu8F66",
            "uss": "",
            "csg": "17153f9e",
            "skt": "e54c5c99ab77f769",
            "_m_h5_tk": "8a1bd52de17c3e11d57dc9262901d893_1548522921376",
            # "x5sec" : "7b227477736d3b32223a223732636364363366373234636463643731323330623432353734383634646332434c364f734f4d46454f4f6639372b363234656739674561444449354e4449344f4455784e6a6b374d513d3d227d",
            "_m_h5_tk_enc": "f5ad8ee422bdb934f61a87456d01e580",
            }

        self.isg_list = [
        'BNXVATK9JUTzvwEhdNZRZknQ5NFPepaXW2OIr1d6kcybrvWgHyKZtONofPK9q6Gc',
        'BFVVg7I9pcRzPYGh9FbR5slQZFHP-hYX2-MIL9f6EUwbLnUgn6IZNGPs_HI9KyEc',
        'BCwsfwh7XK-xhkiNy1XlzHv3_gqeTc_8xz7qsIZsFVd4kc6brvfCHlljtZmMAgjn',
        'BJGRzXIgqfArYMX6Ht7wA7a8o53rVhoDusWnZ3Mmjdh2GrFsu04VQD94uC5ZCZ2o',
        'BLOzZSSW6wrF76fAqIjyCajiQbcdQFjZFMuFPWVQD1ILZNMG7bjX-hH2GlQvX5-i',
        'BGhoxpmroFtqaIzBL4FpWNcbOla6OdPou0Ku_CKZnuPWfQjnyqPNKFOzcdUo1oRz',
        'BBsbLT65w_J4cj8fTnS30GOSqn9FWDCBIeEWMQ1Y95ox7DvOlcC_QjluggxHSYfq'
        ]

    def parse(self, response):

        headers = self.get_new_headers()        #获取随机headers

        res = requests.get(url=response.url, headers=headers)

        res_json = json.loads(res.text)         #转换为json格式

        if res_json == None:
            print(False)
        else:
            print(res_json)

        if 'items' in res_json:                 #提取json 数据

            page_num = res_json['total_page']       #总页数

            current_page = res_json['current_page']     #当前页数


            for i in res_json['items']:
                allItem = TmallItem()
                allItem['item_id'] = i['item_id']
                allItem['title'] = i['title']
                allItem['img'] = i['img']
                allItem['sold'] = i['sold']
                allItem['quantity'] = i['quantity']
                allItem['url'] = i['url']
                allItem['price'] = i['price']

                print(allItem)
                return allItem

            # for i in res_json['items']:
            #     time.sleep(10)
            #     yield scrapy.Request(url=parse.urljoin("https:", i['url']), headers=headers, dont_filter=True,
            #                          callback=self.parse_detail)  # 爬取商品详情

            if current_page < page_num:                 #判断页数是否到底

                time.sleep(10)
                yield scrapy.Request(url=parse.urljoin(response.url,'?p=%s'%(int(current_page)+1)),callback=self.parse,dont_filter=True)    #下一页爬取

        else:
            print('Cookies失效，请手动更新Cookies')

        for url in self.shop_url_list:

            time.sleep(10)
            print(url)
            yield scrapy.Request(url=parse.urljoin(url,'shop/shop_auction_search.do'),callback=self.parse,dont_filter=True)    #下一页爬取






    def get_new_headers(self):          #随机更新cookies

        isg = random.choice(self.isg_list)

        self.Cookies.update({
            "isg": isg
        })

        cookie_list = ''                    #cookies转化为str
        for k in self.Cookies:
            cookie_list += k + "=" + self.Cookies[k] + ";"

        self.loginHeaders.update({
            'cookie': cookie_list
        })

        return self.loginHeaders


    def parse_detail(self,response):        #商品详情爬取

        goodsItem = GoodsDetail()

        name = response.css('.module-title .share-warp .main::text').extract()[0]

        soup = BeautifulSoup(response.text, 'lxml')

        scr = soup.select('script')[-6].string          #利用Bs4抓取script中的数据

        scr_text = js2xml.parse(scr, debug=False)       #利用js2xml转换script为html树

        scr_tree = js2xml.pretty_print(scr_text)

        selector = etree.HTML(scr_tree)

        content = selector.xpath("//property[@name='基本信息']/array//object/property/string/text()")       #商品基本信息

        print(content)

        goodsItem['name'] = name
        goodsItem['brand'] = content[0]
        goodsItem['size'] = content[1]
        goodsItem['color'] = content[2]
        goodsItem['num'] = content[3]
        goodsItem['style'] = content[4]
        goodsItem['season'] = content[5]
        goodsItem['listing_year'] = content[6]
        goodsItem['scenario'] = content[7]
        goodsItem['type'] = content[8]
        goodsItem['composition'] = content[9]

        yield goodsItem