import requests
r=requests.get('http://openapi.seoul.go.kr:8088/58795458696a6273393255484a5249/json/InfoTrdhlSelng/1/500/201606')
d=r.json()
Fri=[]
for index, data1 in enumerate(d['InfoTrdhlSelng']['row']):
    Fri.append(data1['FRI_SELNG_RATE'])
import matplotlib.pyplot as plt
plt.title('Friday sales')
plt.plot(Fri,'ro')
plt.xlabel('Avg=14.9556')
plt.show()
#print sum(Fri)/500