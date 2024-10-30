import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
f2=pd.read_csv('landslide_data_miss.csv')
F2=f2['stationid'].dropna()
F2=F2.tolist()
#(2)
a=np.empty((7,7))
def interpolate(x_list):   
    for i in range(0,len(x_list)):
        count=0
        if str(x_list[i])=="nan":
            while(str(x_list[i+count])=="nan"):
                count+=1     
            x_list[i]=(i-(i-1))*((x_list[i+count]-x_list[i-1])/((i+count)-(i-1)))+x_list[i-1]
    # print("list is",li)       
    return x_list      
           
tem=f2["temperature"].tolist()
hum=f2["humidity"].tolist()
pressure=f2["pressure"].tolist()
Rain=f2["rain"].tolist()
lightavg=f2["lightavg"].tolist()
lightmax=f2["lightmax"].tolist()
mois=f2["moisture"].tolist()
headlist=[tem,hum,pressure,Rain,lightavg,lightmax,mois]

for i in range(0,7):
    interpolate(headlist[i]) 
print(headlist[0])

#(a)
# mean 
def meannum(x_list):
    s1=0
    for j in x_list:
        s1=s1+j
    m1=round(s1/len(x_list),2) 
    return m1
# median
def mediannum(y_list):
    y_list.sort()
    if len(y_list)%2!=0:
        median1=y_list[(len(y_list)+1)//2]
    else:
        median1=(y_list[(len[y_list]//2)]  +y_list[(len(y_list)//2)+1])//2
    return median1 
# standard deviation  
def stddev(z_list):
    summation=0
    for j in z_list:
        summation=summation+j
    meann=round(summation/len(z_list)) 
    val1=0
    for t in z_list:
        val1=(t-meann)**2+val1
    std1=round(((val1/len(z_list))**0.5 ),2) 
    return std1
arr=np.empty((3,7))
for col in range(0,7):
    arr[0][col]=meannum(headlist[col])
for col in range(0,7):
    arr[1][col]=mediannum(headlist[col])    
for col in range(0,7):
    arr[2][col]=stddev(headlist[col])    
def series(a_list):
    ser=pd.Series(a_list) 
    return ser   
index=["temperature" ,"Humidity" ,"pressure" ,"Rain","lightavg" ,"lightmax","moisture"]
frame=pd.DataFrame({"mean":series(arr[0])  ,"median":series(arr[1])  ,"standarddeviation":series(arr[2])  })
frame.index=index
print(frame)

#(b)
nantemp=f2["temperature"].tolist()
nanhum=f2["humidity"].tolist()
nanpressure=f2["pressure"].tolist()
nanRain=f2["rain"].tolist()
nanlightavg=f2["lightavg"].tolist()
nanlightmax=f2["lightmax"].tolist()
nanmois=f2["moisture"].tolist()
misslist=[nantemp,nanpressure,nanhum,nanRain,nanlightavg,nanlightmax,nanmois]

f1=pd.read_csv('landslide_data_original.csv')
oritemp=f1["temperature"].tolist()
oripressure=f1["pressure"].tolist()
orihum=f1["humidity"].tolist()
oriRain=f1["rain"].tolist()
orilightavg=f1["lightavg"].tolist()
orilightmax=f1["lightmax"].tolist()
orimois=f1["moisture"].tolist()
orilist=[oritemp,oripressure,orihum,oriRain,orilightavg,orilightmax,orimois]

# print("this is index",index(misslist[1]))
def RMSE(ful_list,nan_list):
    numerator=0
    indices = []
    for i in range(len(nan_list)):
        if str(nan_list[i])=="nan":
           indices.append(i)    
    newlist=interpolate(nan_list)

    for i in indices:
        numerator=(ful_list[i]-newlist[i])**2+numerator
    denominator=len(ful_list)
    RMSE=(numerator/denominator)**0.5
    return RMSE

yaxis=[]
for i in range(7):
    yaxis.append(RMSE(orilist[i],misslist[i])) 
print(yaxis)    
xaxis=["temperature","humidity","pressure","Rain","lightavg","lightmax","mois"]
print("yaxis",yaxis)
plt.scatter(xaxis,yaxis)
plt.show()      


     














        

