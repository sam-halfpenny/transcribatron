import scipy.io.wavfile as wave
import numpy
import math
def reduceBitRate(array,factor):
    newArray={'arr':[],'br':math.floor(len(array)/factor)}
    for i in range(newArray['br']):
        newArray['arr'].append(array[factor*i])
    return newArray
    
    
def createMonoFile(file):
    fileArray=wave.read(file)
    wavArray=fileArray[1]
    bitRate=fileArray[0]
    print(wavArray)
    newArray=[]
    for i in wavArray:
        newArray.append((i[0]+i[1])/2) # take an average of the stereo output
    wave.write('Monosound.wav',bitRate,newArray)
def stereoToMono(array):
    wavArray=array[1]
    bitRate=array[0]
    if len(wavArray)==1:
        return wavArray
    newArray=[]
    for i in range(len(wavArray)):
        newArray.append((int(wavArray[i][0])+int(wavArray[i][1]))/2) # take an average of the stereo output
    return [bitRate,newArray]
def splitStereo(array):
    wavArray=array[1]
    bitRate=array[0]
    newArray=[[],[]]
    for i in wavArray:
        newArray[0].append(i[0])
        newArray[1].append(i[1])
    return [bitRate,newArray]