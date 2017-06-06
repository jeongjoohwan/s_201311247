import requests
r=requests.get('http://openapi.seoul.go.kr:8088/58795458696a6273393255484a5249/json/InfoTrdhlSelng/1/500/201606')
d=r.json()
Sat=[]
for index, data1 in enumerate(d['InfoTrdhlSelng']['row']):
    Sat.append(data1['SAT_SELNG_RATE'])
import matplotlib.pyplot as plt
plt.title('Saturday sales')
plt.plot(Sat,'ro')
plt.xlabel('Avg=14.0492')
plt.show()
#print sum(Sat)/500