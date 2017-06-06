import requests
r=requests.get('http://openapi.seoul.go.kr:8088/58795458696a6273393255484a5249/json/InfoTrdhlSelng/1/500/201606')
d=r.json()
Tues=[]
for index, data1 in enumerate(d['InfoTrdhlSelng']['row']):
    Tues.append(data1['TUES_SELNG_RATE'])
import matplotlib.pyplot as plt
plt.title('Tuesday sales')
plt.plot(Tues,'ro')
plt.xlabel('Avg=13.7014')
plt.show()
#print sum(Tues)/500