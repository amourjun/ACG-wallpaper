# -*- coding: utf8 -*-
import urllib2
import urllib
import re
import os
import threading
from concurrent import futures

#抓取acg12 壁纸排行榜
class spider():
    #获取网页html源代码
    def __init__(self, url = None, paramList = None):
        self.filePath = None
        self.url = url
        self.num = paramList['num']
        self.month = paramList['month']
        self.year = 2017
        self.headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/56.0.2924.87 Safari/537.36'
        }

    def save_img(self, imgUri, filePath, fileName):
        try:
            request = urllib2.Request(imgUri, None, self.headers)
            response = urllib2.urlopen(request)
            fileUrl = '{}/{}'.format(filePath,fileName)
            f = open(fileUrl, 'wb')
            f.write(response.read())
            f.close()
        except IOError as e:
            print '文件操作失败',e
        except Exception as e:
            print '错误 ：',e
    
    #获取资源url列表,通过输入规则
    def get_urls(self):
        fmt = 'http://pic1.acg12.net/wp-content/uploads/{0}/{1}/Konachan-{2}.jpg'        
        urls = [fmt.format(self.year, self.month, self.num) for self.num in range(1,10)]
        return urls
    #每个将uri资源下载到指定目录下，path默认为root目录下acg12文件夹,path请合法输入
    def crawl(self, uri):
        #获取uri最后文件名
        jpgName = os.path.basename(uri)
        fileName = 'acg12-' + self.month + '-' + jpgName
        self.save_img(uri, self.filePath, fileName)

    def run(self):
        #获取网站中资源url列表
        urls = self.get_urls()
        print urls
        curdir = os.path.abspath(os.curdir)
        self.filePath = curdir + '/acg12'
        print self.filePath
        if not os.path.exists(self.filePath):
            print '创建文件夹' + filePath + ':\n'
            os.makedirs(self.filePath)
        with futures.ThreadPoolExecutor(64) as executor:
            executor.map(self.crawl, urls)

if __name__ == '__main__' :
    #初始化要抓取的网址地址，以及参数列表
    #直接查询7月的前num-10张图片
    paramList = {
        'month' : '06',
        'num'   : 10
    }
    
    spider1 = spider(None, paramList)
    spider1.run()
