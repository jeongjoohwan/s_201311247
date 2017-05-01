import os
import src.mylib

keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
key=src.mylib.getKey(keyPath)
KEY=str(key['key'])
TYPE='xml'
SERVICE='SearchSTNBySubwayLineService'
START_INDEX=str(1)
END_INDEX=str(10)
LINE_NUM=str(2)

params=os.path.join(KEY,TYPE,SERVICE,START_INDEX,END_INDEX,LINE_NUM)


import urlparse
_url='http://openAPI.seoul.go.kr:8088/'
url=urlparse.urljoin(_url,params)
print url