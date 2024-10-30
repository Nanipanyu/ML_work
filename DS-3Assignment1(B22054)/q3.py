import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv('landslide_data_miss.csv')
df=pd.DataFrame(data)
cols=list(df.columns)

def interpolate(df):
    headlist=list(df.columns)
    for j in range(2,len(headlist)):  
        for i in range(0,len(df[headlist[j]])):
            count=0
            if pd.isnull(df[headlist[j]][i]):
                while(pd.isnull(df[headlist[j]][i+count])):
                    count+=1     
                df[headlist[j]][i]=(i-(i-1))*((df[headlist[j]][i+count]-df[headlist[j]][i-1])/((i+count)-(i-1)))+df[headlist[j]][i-1]
    return df
values1=interpolate(df)
print(values1) 

figure, axis=plt.subplots(2,4)
axis[0,0].boxplot(list(values1[cols[2]]))
axis[0,0].set_title("temperature")

axis[0,1].boxplot(list(values1[cols[3]]))
axis[0,1].set_title("humidity")

axis[0,2].boxplot(list(values1[cols[4]]))
axis[0,2].set_title("pressure")

axis[0,3].boxplot(list(values1[cols[5]]))
axis[0,3].set_title("Rain")

axis[1,0].boxplot(list(values1[cols[6]]))
axis[1,0].set_title("lightavg")

axis[1,1].boxplot(list(values1[cols[7]]))
axis[1,1].set_title("lightmax")

axis[1,2].boxplot(list(values1[cols[8]]))
axis[1,2].set_title("moisture")

plt.show()

#(2)
def medianfill(df):
    newdf=interpolate(df)
    headlist=list(df.columns)    
    for i in range(2,len(headlist)):
        Q1=np.percentile(list(newdf[headlist[i]]),25)
        Q3=np.percentile(list(newdf[headlist[i]]),75)
        IQR=Q3-Q1
        col=list(newdf[headlist[i]])
        col.sort()
        if len(col)%2!=0:
            median1=col[(len(col)+1)//2]
        else:
            median1=(col[(len[col]//2)]  +col[(len(col)//2)+1])//2 

        for j in range(len(df[headlist[i]])):
            if (Q1-(1.5*IQR))>(newdf[headlist[i]][j]) or (Q3+(1.5*IQR))<(newdf[headlist[i]][j]):
                newdf[headlist[i]][j]=median1

    return newdf 
values2=medianfill(df)

figure, axis=plt.subplots(2,4)
axis[0,0].boxplot(list(values2[cols[2]]))
axis[0,0].set_title("temperature")

axis[0,1].boxplot(list(values2[cols[3]]))
axis[0,1].set_title("humidity")

axis[0,2].boxplot(list(values2[cols[4]]))
axis[0,2].set_title("pressure")

axis[0,3].boxplot(list(values2[cols[5]]))
axis[0,3].set_title("Rain")

axis[1,0].boxplot(list(values2[cols[6]]))
axis[1,0].set_title("lightavg")

axis[1,1].boxplot(list(values2[cols[7]]))
axis[1,1].set_title("lightmax")

axis[1,2].boxplot(list(values2[cols[8]]))
axis[1,2].set_title("moisture")

plt.show()       




