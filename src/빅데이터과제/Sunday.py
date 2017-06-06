import requests
r=requests.get('http://openapi.seoul.go.kr:8088/58795458696a6273393255484a5249/json/InfoTrdhlSelng/1/500/201606')
d=r.json()
Sun=[]
for index, data1 in enumerate(d['InfoTrdhlSelng']['row']):
    Sun.append(data1['SUN_SELNG_RATE'])
import matplotlib.pyplot as plt
plt.title('Sunday sales')
plt.plot(Sun,'ro')
plt.xlabel('Avg=9.2536')
plt.show()
#print sum(Sun)/500