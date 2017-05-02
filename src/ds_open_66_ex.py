import os
import requests
_url='http://openAPI.seoul.go.kr:8088'
_key=str(key['key'])
_type='xml'
_service='CardSubwayStatisticsService'
_start_index=1
_end_index=5
_use_mon='201306'
_maxIter=2
_iter=0
while _iter<_maxIter:
    _api=os.path.join(_url,_key,_type,_service,str(_start_index),str(_end_index),_use_mon)
    r = requests.get(_api.replace('\\','/')).text
    print r
    _start_index+=5
    _end_index+=5
    _iter+=1