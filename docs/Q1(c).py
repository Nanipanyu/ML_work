import matplotlib.pyplot as plt
import sys
print(sys.argv)
l=[]
if len(sys.argv)==1:
    print("No Input File")

for i in range(1,len(sys.argv)):
    file_name1=open(sys.argv[i],'r')
    lines=file_name1.readlines()
    x_val=lines[0][1:].split()
    y_val=lines[1][2:].split()
    x_val=[int(i) for i in x_val]
    y_val=[int(i) for i in y_val]
    d={}
    for i in range(len(x_val)):
        d[x_val[i]]=y_val[i]
    d=dict(sorted(d.items()))
    l.append(d)
    print(d)
print(l)
leg=[x for x in range(1,len(l)+1)]
for i in range(len(l)):
    y=list(l[i].values())
    x=list(l[i].keys())
    plt.scatter(x,y)
    plt.xlabel("X")
    plt.ylabel("Y")
plt.legend(leg)
plt.show()
