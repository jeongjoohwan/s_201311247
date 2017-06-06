import requests
r=requests.get('http://openapi.seoul.go.kr:8088/58795458696a6273393255484a5249/json/InfoTrdhlSelng/1/500/201606')
d=r.json()
Thur=[]
for index, data1 in enumerate(d['InfoTrdhlSelng']['row']):
    Thur.append(data1['THUR_SELNG_RATE'])
import matplotlib.pyplot as plt
plt.title('Thursday sales')
plt.plot(Thur,'ro')
plt.xlabel('Avg=17.673')
plt.show()
#print sum(Thur)/500