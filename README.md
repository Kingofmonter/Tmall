#Tmall<br>

1.使用 <br>
依赖库: scrapy requests time js2xml random bs4 lxml urllib <br>
启用: 运行main.py

##2.思路

1).网页登陆手机版淘宝，找到店铺全部商品页面<br>
2).打开开发者工具，找到商品请求的地址'https://uniqlo.m.tmall.com/shop/shop_auction_search.do'<br>
3).打开请求地址,获取浏览器发送请求的请求头<br>
4).根据请求地址进行传入参数测试，发现只有后跟参数'?p=数字'会进行跳转翻页<br>
5).数据格式{<br>
	"shop_id":'xxx',	<br>
	"user_id":'xxx',<br>
	"shop_title":'xxx',<br>
	"total_page":'',		#总页数<br>
	"shop_Url":'xxx',<br>
	"items":[				#商品列表<br>
		{<br>
		xxx		<br>
		}		<br>
	],	<br>
	"current_page":'xxx',	#当前页数<br>
	"page_size":'xxx',		<br>
	total_results:'xxx'		#商品总数<br>
	}<br>
6).获取页面数据，并根据total_page给参数p赋值进行循环爬取<br>
7).储存数据<br>
##3.注意点 <br>
1.淘宝天猫PC版的cookies和手机版的cookies不一样，所以不能用PC版的cookies请求手机版的页面 <br>
2.可多取几个cookies中的isg的值进行随机组合cookies和设置ip代理池,以免ip被封 <br>
3.各个商品的详情信息在各自页面的script中，可用bs4和js2xml库进行数据的转换，将script数据转换为HTML树再进行爬取<br>

##2019.2.25 
添加商店列表爬取 <br>
如无法连接主机请在middlewares中间件中更新https的ip地址 <br>
ip地址运行test.py文件可获取
