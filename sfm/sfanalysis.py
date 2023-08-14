import math
import fourierTransform as ft
from freqToPitch import frequencyToPitch
import scipy.io.wavfile as wave
import numpy as np
import mono
import math
import matplotlib.pyplot as plt
fileData=mono.stereoToMono(wave.read(input('filename:')))
audioData=fileData[1]
bitRate=fileData[0]
brScale=int(input('input bit rate reduction factor:'))
fileData=mono.reduceBitRate(audioData,brScale)
audioData=fileData['arr']
bitRate=math.floor(bitRate/brScale)
ftSamplePeriod=int(input('input Fourier Transform sample period(seconds):'))
frequencySample=int(input('input the number of frequency samples per period:'))
keyArray=[]
for i in range(math.floor(len(audioData)/bitRate)):
    ftArray=np.fft.fft(audioData[bitRate*ftSamplePeriod*(i):bitRate*ftSamplePeriod*(i+1)])
    topFrequencies=ft.peakAnalysis(ftArray,frequencySample)
    keyArray.append([])
    for f in topFrequencies:
        keyArray[i].append(frequencyToPitch(f*ftSamplePeriod))
i+=1
ftArray=np.abs(np.fft.fft(audioData[bitRate*ftSamplePeriod*(i):]))
topFrequencies=ft.peakAnalysis(ftArray,frequencySample)
keyArray.append([])
for f in topFrequencies:
    keyArray[i].append(frequencyToPitch(f*((len(audioData)%bitRate)/bitRate)))
print(keyArray)



