import requests
r=requests.get('http://openapi.seoul.go.kr:8088/58795458696a6273393255484a5249/json/InfoTrdhlSelng/1/500/201606')
d=r.json()
Mon=[]
for index, data1 in enumerate(d['InfoTrdhlSelng']['row']):
    Mon.append(data1['MON_SELNG_RATE'])
import matplotlib.pyplot as plt
plt.title('Monday sales')
plt.plot(Mon,'ro')
plt.xlabel('Avg=13.4242')
plt.show()
#print sum(Mon)/500