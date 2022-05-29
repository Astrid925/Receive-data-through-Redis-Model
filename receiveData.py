"""
Author: cxy
Date: 2022/03/24
"""
import redis
import datetime
import os

class DataReceive():

    def __init__(self, inputPath, host,port,subName):
        self.inputPath = inputPath
        self.host = host
        self.port=port
        self.subName=subName

    def openFile(self):
        ISOTIMEFORMAT = '%Y%m%d%H%M%S'
        theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
        writePath = os.path.join(self.inputPath, theTime+'.raw')
        self.writeFile = open(writePath, mode='wb')

    def closeFile(self):
        self.writeFile.close()

    def recDatafromServe(self):
        pool = redis.ConnectionPool(host=self.host, port=self.port)  # 遥测数传前端软件IP地址， 遥测数传前端软件端口号port
        rc=redis.StrictRedis(connection_pool=pool)
        ps=rc.pubsub()
        ps.subscribe(self.subName)   # 订阅数据
        for item in ps.listen():
            if item['type'] == 'message':
                print(item['channel'])
                print(item['data'])
                a=item['data']
                self.writeFile.write(item['data'])
                self.writeFile.flush()