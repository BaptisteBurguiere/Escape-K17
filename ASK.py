from math import sin, pi
import soundfile as sf

def Modulation(data, f, bps) :

	dataList = list(data.strip())
	for i in range(len(dataList)) :
		dataList[i] = int(dataList[i])

	Fe = 2.205 * f
	pasTemps = 1 / Fe
	t = 0
	signal = []

	while t < len(dataList)/bps :
		signal += [dataList[int(t*bps)] * sin(2 * pi * f * t)]
		t += pasTemps

	return signal




def Demodulation(filename, bps) :

	data, Fe = sf.read(filename)
	dataList = []
	bit = ((Fe/bps) / 2) + 1

	for i in range(len(data)) :
		if i == bit :
			dataList.append(data[i])
			bit += Fe/bps

	binary = ""
	for j in range(len(dataList)) :
		if dataList[j] < 0.1 and dataList[j] > -0.1 :
			binary += "0"

		else :
			binary += "1"

	return binary