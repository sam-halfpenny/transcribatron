import math
import matplotlib.pyplot as plt
def Amplitude(array):
    fArray=[]
    for f in range(math.floor(len(array)/2)): # no need to calculate values above th Nyquist limit
        sum={'re':0,'im':0}
        for n in range(len(array)):
            sum['re']+=(array[n]*math.cos(-(2*math.pi*f*n)/len(array))*2)/len(array)
            sum['im']+=(array[n]*math.sin(-(2*math.pi*f*n)/len(array))*2)/len(array)
        fArray.append(math.sqrt(math.pow(sum['re'],2)+math.pow(sum['im'],2)))
    return fArray
def Phase(array):
    fArray=[]
    for f in range(math.floor(len(array)/2)): # no need to calculate values above th Nyquist limit
        sum={'re':0,'im':0}
        for n in range(len(array)):
            sum['re']+=(array[n]*math.cos(-(2*math.pi*f*n)/len(array))*2)/len(array)
            sum['im']+=(array[n]*math.sin(-(2*math.pi*f*n)/len(array))*2)/len(array)
        fArray.append(math.atan(sum['im']/sum['real']))
    return fArray
def peakAnalysis(ftArray,peakNum):
    hierarchy=[]
    for n in range(peakNum):
        highest={'index':0,'value':0}
        for i in range(len(ftArray)):
            if (ftArray[i]>highest['value'] and ftArray[i]>ftArray[i+1]) and ftArray[i]>ftArray[i-1]:
                highest={'index':i,'value':ftArray[i]}
        hierarchy.append(highest['index'])
    return hierarchy

# array=[]
# for i in range(100):
#     array.append(math.sin(math.sin(6*i*math.pi/100)))
# fourier=fourierTransform(array)
# indexArray=[]
# for i in range(len(fourier)):
#     indexArray.append(i)
# plt.plot(indexArray,fourier,color = 'red',marker = 'o')
# plt.show()


