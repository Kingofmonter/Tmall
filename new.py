import json
import requests
import time
import csv
from pyquery import PyQuery as pq
from selenium import webdriver

class Taobao():

    def __init__(self,page):

        self.loginHeaders = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'keep-alive',
            'Host': 'uniqlo.m.tmall.com',
            'Pragma': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        }

        self.Cookies = '_l_g_	Ug==_m_h5_tk	bdbc55c210586c3f06ca19faa72ea9ff_1548688736773_m_h5_tk_enc	a979aebd8344edcfcd2e24acae8abb7c_nk_	\u5927\u5E08\u51F6\u5F00\u8F66_tb_token_	33eee0ea35e38ck1	""cna	5+rVFBo7QV4CASe6AoWIkBvRcookie1	BxNUPBrMWOoRBp74g4fzDzf+NwUzPxGRxfafMmQ22vQ=cookie17	UUGmvJzxG6Nt/A==cookie2	13334d005ac19fd91f5a5223f881d667csg	ab029b42hng	""isg	BPj4Hjbt0BRsmTyRH1H5qMdLyqZKyUOYq3I-jDJpLzPnTZg32nOneKBnAYXYBhTDlgc	\u5927\u5E08\u51F6\u5F00\u8F66lid	å¤§å¸�å�¶å¼�è½¦login	trueskt	ef0ca7ec4431894ct	dfffcdc8e35517ef29649bf20d00125ctracknick	\u5927\u5E08\u51F6\u5F00\u8F66uc1	cookie16=Vq8l+KCLySLZMFWHxqs8fwqnEw==&cookie21=UIHiLt3xThH8t7YQoFNq&cookie15=Vq8l+KCLz3/65A==&existShop=false&pas=0&cookie14=UoTYPmfkJQU9Cg==&tag=8&lng=zh_CNuc3	vt3=F8dByE7amBarQIGaRZI=&id2=UUGmvJzxG6Nt/A==&nk2=1z87i2MA+r/4Ow==&lg2=UIHiLt3xD8xYTw==unb	2942885169uss	""x5sec	7b227477736d3b32223a223166633866663438316437643565353430343136343239326631343832373039434b7544764f4946454a5757766f58786d75474c5a786f4d4d6a6b304d6a67344e5445324f547332227d'
        self.page = page
        self.uniqlo_url = 'https://uniqlo.m.tmall.com/shop/shop_auction_search.do?p=%s'%self.page
        print(self.uniqlo_url)

    def get_new_headers(self):

        # cookie_list = ''
        # for k in self.Cookies:
        #     cookie_list += k + "=" + self.Cookies[k] + ";"

        self.loginHeaders.update({
            'Cookie': self.Cookies
        })

        return self.loginHeaders

    def get_json_data(self):

        new_headers = self.get_new_headers()

        res = requests.get(self.uniqlo_url,headers=new_headers)

        res_json = json.loads(res.text)

        print(res_json)

        if 'items' in res_json:

            data = []

            for item in res_json['items']:
                i = {}
                i.update({
                    "item_id": item['item_id'],
                    "title": item['title'],
                    "img_url": item['img'],
                    "sold": item['sold'],
                    "quantity": item['quantity'],
                    "url": item['url'],
                    "price": item['price']
                })
                data.append(i)

            print(data)

            return data, res_json['total_page']

        else:
            print('失败')

    def save_data(self):

        data,total_page = self.get_json_data()

        head = ["item_id","title","img_url","sold","quantity","url","price"]

        # with open('data.csv','a+',newline='') as f:
        #     writer = csv.DictWriter(f,head)
        #
        #     for row in data:
        #         writer.writerow(row)


        with open('data.json','a',encoding='utf8') as f:

            for i in data:
                f.write(json.dumps(i,ensure_ascii=False))
        # page_list = []
        # for i in range(self.page+1,int(total_page)+1):
        #
        #     page_list.append(i)
        #
        # print(page_list)


if __name__ == '__main__':
    url = 'https://uniqlo.m.tmall.com/shop/shop_auction_search.do?p=1'
    tb = Taobao(3)
    page = tb.save_data()