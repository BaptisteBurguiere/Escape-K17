def creerDict() :

	n = 256
	return {chr(i):i for i in range(n)}




def inversDict(dictionnaire) :

	return {v:k for k,v in dictionnaire.items()}




def toBinary(data) :
	
	listBinaire = []
	dataBinaire = ""

	while data != 0 :

		if data % 2 == 0 :
			listBinaire.append("0")

		else :
			listBinaire.append("1")
			data -= 1

		data = data / 2

	i = len(listBinaire) - 1
	while i >= 0 :

		dataBinaire += listBinaire[i]
		i -= 1

	return dataBinaire

	


def toBase10(data) :

	dataReverse = ""

	i = len(data) - 1
	while len(dataReverse) != len(data) :

		dataReverse += data[i]
		i -= 1

	nombre = 0
	for i in range(0, len(dataReverse)) :

		if dataReverse[i] == "1" :
			nombre += 2 ** i

	return nombre




def compression(data) :

	dictionnaire = creerDict()
	dictionnaireSize = len(dictionnaire)

	w = ""
	encodedData = []

	for c in data :
		wc = w + c

		if wc in dictionnaire :
			w = wc

		else :
			encodedData.append(dictionnaire[w])
			dictionnaire[wc] = dictionnaireSize
			dictionnaireSize += 1
			w = c

	if w :
		encodedData.append(dictionnaire[w])

	binaryData = ""

	for n in encodedData :

		binary = toBinary(n)

		bitsManquants = ""
		for i in range(9 - len(binary)) :
			bitsManquants += "0"

		binary = bitsManquants + binary
		
		binaryData += binary

	return binaryData	




def decompression(data) :

	binary = ""
	dataList = []

	for i in range(len(data)) :
		binary += data[i]

		if len(binary) == 9 :
			dataList.append(toBase10(binary))
			binary = ""


	dictionnaire = creerDict()
	dictionnaire = inversDict(dictionnaire)
	dictionnaireSize = len(dictionnaire)

	decodedData = ""

	w = chr(dataList.pop(0))
	decodedData += w

	for k in dataList :

		if k in dictionnaire :
			entre = dictionnaire[k]

		elif k == dictionnaireSize :
			entre = w + w[0]

		decodedData += entre
		
		dictionnaire[dictionnaireSize] = w + entre[0]
		dictionnaireSize += 1

		w = entre

	return decodedData