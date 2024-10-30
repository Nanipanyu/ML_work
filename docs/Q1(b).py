import sys
l=[]
if len(sys.argv)==1:
    print("No Input File")
r_val=[]
for i in range(1,len(sys.argv)):

    file_name1=open(sys.argv[i],'r')
    lines=file_name1.readlines()
    x_val=lines[0][1:].split()
    y_val=lines[1][2:].split()
    x_val=[int(i) for i in x_val]
    y_val=[int(i) for i in y_val]

    xy=[x_val[i]*y_val[i] for i in range(len(x_val))]
    sumxy=sum(xy)
    sumx=sum(x_val)
    sumy=sum(y_val)
    xsq=[x_val[i]*x_val[i] for i in range(len(x_val))]
    ysq=[y_val[i]*y_val[i] for i in range(len(y_val))]
    sumxsq=sum(xsq)
    sumysq=sum(ysq)
    n=len(x_val)

    rnum=(n*sumxy - sumx*sumy)
    rden=((n*sumxsq - sumx*sumx)**0.5)*((n*sumysq - sumy*sumy)**0.5)
    r=rnum/rden
    r_val.append(r)
foutput=open('Output1c.txt','w')
for i in range(len(r_val)):
    foutput.write("Output from input: ")
    foutput.write(str(i+1))
    foutput.write(" ")
    foutput.write(str(r_val[i]))
    foutput.write("\n")

foutput.close()
