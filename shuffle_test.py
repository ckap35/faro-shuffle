import numpy, scipy, matplotlib
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook




def intershuffle(lst):
    output=lst
    L=len(lst)
    Lhalf=int(L/2)
    a1=lst[0:Lhalf];
    a2=lst[Lhalf::1];
    #output=[val for pair in zip(a1, a2) for val in pair]
    output=a1+a2;
    output[::2]=a1
    output[1::2]=a2
    return output

def checkshufflecycle(lst):
    index=1
    shuffled = [x * 1 for x in lst]
    #print(lst)
    shuffled= intershuffle(lst)
    #print(shuffled)
    while (shuffled!=lst):
        shuffled= intershuffle(shuffled)
        #print(shuffled)
        index+=1
    #print(index)
    return index


Ns=[]
numshuffles=[]

for n in range(2,1000,2):
    Ns.append(n)
    #print(n)
    a=list(range(1,n+1))
    numshufs=checkshufflecycle(a)
    numshuffles.append(numshufs)
    #print("\n")

xData=Ns
yData=numshuffles

# find points for which y=x
both = set(xData).intersection(yData)
indices_x = [xData.index(x) for x in both]
indices_y = [yData.index(x) for x in both]

result = [xData[i] for i in indices_x]




color=[x * 1 for x in xData]
size=[x * 0+20 for x in xData]

fig, ax = plt.subplots()
ax.scatter(xData, yData, c=color, s=size, alpha=0.4)

ax.set_xlabel(r'Number of cards in deck', fontsize=15)
ax.set_ylabel(r'Number of shuffles required', fontsize=15)
ax.set_title('Shuffles required to return to initial state')
plt.plot(xData,xData)
plt.plot(xData,[x/2 for x in xData])
plt.plot(xData,[x/3 for x in xData])
plt.plot(xData,[x/4 for x in xData])
plt.plot(xData,[x/5 for x in xData])
plt.plot(xData,[x/6 for x in xData])
plt.plot(xData,[x/7 for x in xData])
plt.plot(xData,[x/8 for x in xData])

ax.grid(True)
plt.show()


