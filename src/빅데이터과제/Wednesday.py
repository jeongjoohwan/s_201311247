import requests
r=requests.get('http://openapi.seoul.go.kr:8088/58795458696a6273393255484a5249/json/InfoTrdhlSelng/1/500/201606')
d=r.json()
Wed=[]
for index, data1 in enumerate(d['InfoTrdhlSelng']['row']):
    Wed.append(data1['WED_SELNG_RATE'])
import matplotlib.pyplot as plt
plt.title('Wednesday sales')
plt.plot(Wed,'ro')
plt.xlabel('Avg=16.9732')
plt.show()
#print sum(Wed)/500