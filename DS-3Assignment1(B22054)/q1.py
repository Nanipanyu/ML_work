import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
f1=pd.read_csv('landslide_data_original.csv')
f2=pd.read_csv('landslide_data_miss.csv')
# g1=f1.dropna(axis='index',how='any')
# g2=f2.dropna(axis='index',how='any')
F1=f1['temperature'].tolist()
F2=f2['temperature'].tolist()
F3=[]
for k in F2:
    if str(k) != 'nan':
        F3.append(k)    

S1=[float(i) for i in F1]
S2=[float(i) for i in F3]
# mean
s1=0
for i in S1:
    s1=s1+i
m1=round(s1/len(S1),2)
# mean
s2=0
for j in S2:
    s2=s2+j
m2=round(s2/len(S2)) 

# minimum values
min1=S1[0]
for b in S1:
    if b<min1:
        min1=b
min2=S2[0]
for c in S2:
    if c<min2:
        min2=c 

# max values
max1=S1[0]
for d in S1:
    if d>max1:
        max1=d
max2=S2[0]
for e in S2:
    if e>max2:
        max2=e  

# Median
S1.sort()
if len(S1)%2!=0:
    median1=S1[(len(S1)+1)//2]
else:
    median1=(S1[(len[S1]//2)]  +S1[(len(S1)//2)+1])//2 
S2.sort()
if len(S2)%2!=0:
    median2=S2[(len(S2)+1)//2]
else:
    median2=(S2[(len[S2]//2)]  +S2[(len(S2)//2)+1])//2 

# standard deviation
val1=0
for t in S1:
    val1=(t-m1)**2+val1
std1=round(((val1/len(S1))**0.5 ),2)   

val2=0
for h in S2:
    val2=(h-m2)**2+val2
std2=round(((val2/len(S2))**0.5 ),2)   



print(f"The statistical measures of temperature attribute are: mean={m1,m2},minimum={min1,min2},maximum={max1,max2},median={median1,median2},STD={std1,std2}")

# (ii)
tag=0
d={'count':0}
stn=f1['stationid'].tolist()
for i in range (0,len(stn)):
    if stn[i]=='t12':
        tag=i
        d['count']+=1
strt=tag-(d['count']-1)
end=tag
print(strt,end,d["count"]) 
hum=f1['humidity'].iloc[strt:end+1].tolist()
hum.sort()
bin=np.arange(hum[0],hum[len(hum)-1]+5,5)
print(list(bin))

plt.hist(hum,bins=bin)
plt.title("Humidity variation")
plt.xticks(bin)
plt.xlabel("humidity")
plt.ylabel("frequency")
plt.show()

# (iii)
H=f1['humidity'].tolist()
P=f1['pressure'].tolist()
R=f1['rain'].tolist()
LA=f1['lightavg'].tolist()
LM=f1['lightmax'].tolist()
M=f1['moisture'].tolist()
mainlist=[F1,H,P,R,LA,LM,M]
def pearson(x_list,y_list):
    mx=mean(x_list)
    my=mean(y_list)
    numerator=0
    for i in range(0,len(x_list)):
        numerator=(x_list[i]-mx)*(y_list[i]-my)+numerator
    r2=0
    r3=0    
    for j in range(0,len(x_list)):
        r2=(x_list[j]-mx)**2+r2
        r3=(y_list[j]-my)**2+r3
    denominator=(r2*r3)**0.5
    ans=numerator/denominator
    return round(ans,2)

arr=np.empty((7,7))
for dim in range(0,7):
    for val in range(0,7):
        arr[dim][val]=(pearson(mainlist[dim],mainlist[val]))
        
def series(a_list):
    ser=pd.Series(a_list) 
    return ser   

index=["temperature" ,"Humidity" ,"pressure" ,"Rain","lightavg" ,"lightmax","moisture"]
frame=pd.DataFrame({"temperature":series(arr[0])  ,"Humidity":series(arr[1])  ,"pressure":series(arr[2])  ,"Rain":series(arr[3])  ,"lightavg":series(arr[4])   ,"lightmax":series(arr[5]) ,"moisture" :series(arr[6])})
frame.index=index
print(frame)



 


        

    





    
















