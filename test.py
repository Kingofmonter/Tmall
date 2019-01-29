import json
import requests
import time
import random
from pyquery import PyQuery as pq


loginHeaders = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'keep-alive',
        'Host': 'uniqlo.m.tmall.com',
        'Pragma': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }

Cookies = {
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
        "csg": "f24f4328",
        "skt": "e54c5c99ab77f769",
        "_m_h5_tk": "8a1bd52de17c3e11d57dc9262901d893_1548522921376",
        "_m_h5_tk_enc": "f5ad8ee422bdb934f61a87456d01e580",
    }

isg_list = [
    'BNXVATK9JUTzvwEhdNZRZknQ5NFPepaXW2OIr1d6kcybrvWgHyKZtONofPK9q6Gc',
    'BFVVg7I9pcRzPYGh9FbR5slQZFHP-hYX2-MIL9f6EUwbLnUgn6IZNGPs_HI9KyEc',
    'BCwsfwh7XK-xhkiNy1XlzHv3_gqeTc_8xz7qsIZsFVd4kc6brvfCHlljtZmMAgjn',
    'BJGRzXIgqfArYMX6Ht7wA7a8o53rVhoDusWnZ3Mmjdh2GrFsu04VQD94uC5ZCZ2o',
    'BLOzZSSW6wrF76fAqIjyCajiQbcdQFjZFMuFPWVQD1ILZNMG7bjX-hH2GlQvX5-i',
    'BGhoxpmroFtqaIzBL4FpWNcbOla6OdPou0Ku_CKZnuPWfQjnyqPNKFOzcdUo1oRz',
       ]

isg = random.choice(isg_list)

Cookies.update({
    "isg":isg
})


cookie_list = ''
for k in Cookies:
    cookie_list += k + "=" + Cookies[k] + ";"

loginHeaders.update({
    'cookie': cookie_list
    })

print(loginHeaders)
