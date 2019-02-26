# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
from scrapy import signals

#ip代理池
class Proxy(object):

    def process_request(self,request,spider):

        h = request.url.split(':')[0]

        if h == 'https':
            ip = random.choice(Proxy_https)
            request.meta['proxy'] = 'https://' + ip
            print(ip)
        else:
            ip = random.choice(Proxy_http)
            request.meta['proxy'] = 'http://' + ip
            print(ip)

class TmallSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class TmallDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)



Proxy_http = [
    '60.255.186.169:8888',
    '61.166.153.172:80',
    '62.210.167.3:3128',
    '160.119.104.69:49327',
    '104.248.220.253:8080',
    '101.81.217.191:8060',
    '101.248.64.68:8080'
]

Proxy_https = [
    '172.106.164.151:8082',
    '142.93.63.115:8080',
    '138.197.128.33:8080',
    '178.128.151.123:8080',
    '142.93.57.147:3128',
    '104.248.119.170:3128',
    '165.227.210.53:3128',
    '142.93.120.180:80',
    '206.81.12.97:3128',
    '157.230.9.88:8080',
    '168.216.24.246:8080',
    '192.99.149.31:3128',
    '149.56.46.173:3128',
    '162.223.89.218:8888',
    '165.227.42.21:8080',
    '165.227.35.172:8080',
    '157.230.8.128:8080',
    '157.230.93.201:8080',
    '104.236.17.72:8118',
    '158.69.243.155:18888',
    '167.114.65.232:3128',
    '198.27.67.35:3128',
    '187.188.214.116:3128',
    '157.230.150.101:8080',
    '206.189.162.192:8080',
    '104.168.151.96:3128',
    '104.207.159.34:3128',
    '187.217.188.153:8080',
    '147.135.98.85:80',
    '134.209.13.153:8080',
    '194.88.105.156:3128',
    '137.44.100.1:3128',
    '159.16.106.110:80'
]

