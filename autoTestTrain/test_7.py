#coding=utf-8

#利用多线程下载文件，参数是文件的url地址 http://10.16.16.17/performance/mutifile.rar
import threading,sys
import requests
import time

class MulThreadDownload(threading.Thread):
    def __init__(self,url,startpos,endpos,f):
        super(MulThreadDownload,self).__init__()
        self.url = url
        self.startpos = startpos
        self.endpos = endpos
        self.fd = f

    def download(self):
        print("start thread:%s at %s" % (self.getName(), time.time()))
        headers = {"Range":"bytes=%s-%s"%(self.startpos,self.endpos)}
        #request下载大文件时，用stream模式
        res = requests.get(self.url,headers=headers,stream=True)
        lock.acquire()
        self.fd.seek(self.startpos)
        for chunk in res.iter_content(chunk_size=512):
            if chunk:
                self.fd.write(chunk)
        lock.release()
        print("stop thread:%s at %s" % (self.getName(), time.time()))

    def run(self):
        self.download()

if __name__ == "__main__":
    url = "http://10.16.16.17/performance/mutifile.rar"
    #获取文件的大小和文件名
    filename = url.split('/')[-1]
    filesize = int(requests.head(url).headers['Content-Length'])
    print("%s filesize:%s"%(filename,filesize))

    #线程数
    threadnum =10

    lock = threading.Lock()
    step = filesize // threadnum
    mtd_list = []
    start = 0
    end = -1

    # wb+ ，二进制打开，可任意位置读写
    with open(filename,'wb+') as  f:
        while end < filesize -1:
            start = end +1
            end = start + step -1
            if end > filesize:
                end = filesize
            # print("start:%s, end:%s"%(start,end))
            t = MulThreadDownload(url,start,end,f)
            mtd_list.append(t)
            t.start()

        for i in  mtd_list:
            i.join()