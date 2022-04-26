import math 

def letter_count(text):
	text = text.lower()
	letters = {}
	for x in range(len(text)):
		letters[text[x]] = letters.get(text[x],0) + 1
	return letters
    
def caracter_especial(palabra):
    for letra in palabra:
        c = ord(letra)
        if (c>=97 and c<=122) or (c>=48 and c<=57) or c==241 or c==32:
            pass
        else:
            return False
    return True

def organizacion_probabilidades(conteo):
	sort_conteo = sorted(conteo.items(),key=lambda x: x[1], reverse = True)
	sort_conteo = dict(sort_conteo)

	probabilidades = list(sort_conteo.values())
	llaves = list(sort_conteo.keys())
	prob_llaves = (probabilidades,llaves)
	return prob_llaves


def shannon(prob):
	last_pos = len(prob)
	first_time = True
	while len(prob)>2:

		pos = division(prob[0:last_pos+1])

		if pos < 0:
			if len(new_bin) == 2:
				prob = prob[2:]
				last_pos = len(prob)
				pos = division(prob[0:last_pos])
			else:
				prob = prob[1:]
				last_pos = len(new_bin)-2
				pos = division(prob[0:last_pos+1])

		new_bin = fill_binary(len(prob[0:last_pos+1]),pos) 
		last_pos = pos

		if first_time:
			binaries = new_bin
			first_time = False
		
		else:
			plus = len(binaries) - len(prob)
			for i in range(len(new_bin)):
				binaries[i+plus] = binaries[i+plus] + new_bin[i]
	
	return binaries


def division(block):
	total = 0
	for x in range(len(block)):
		total = total + block[x]

	mid = total/2
	check = 0
	i = 0

	while check < mid:
		check = check + block[i]
		i = i+1

	i = i-1
	if abs(check-mid) < abs((check-block[i])-mid):
		return i
	else:
		return i-1

def fill_binary(longitud,position):
	new_block = []
	for i in range(longitud):
		if i <= position:
			new_block.append('0')
		else:
			new_block.append('1')
	return new_block

def longitud_promedio(probabilidades,binarios,texto):
	for x in range(len(probabilidades)):
		probabilidades[x] = probabilidades[x] / len(texto)
	lon = 0.0
	z = 0
	while z < len(probabilidades):
		lon = lon + (probabilidades[z]*len(binarios[z]))
		z = z + 1
	return lon

def entropia(probabilidades,texto):
	for x in range(len(probabilidades)):
		probabilidades[x] = probabilidades[x] / len(texto)
	ent = 0.0
	z = 0
	while z < len(probabilidades):
		ent = ent + (-1 * probabilidades[z]*math.log2(probabilidades[z]))
		z = z + 1
	return ent

def eficiencia(entropia,long_prom):
	eficiencia = entropia / long_prom
	eficiencia = int(eficiencia*100)
	return eficiencia

def tasa_compresion(keys,long_prom):
	r = (math.log2(len(keys)))/long_prom
	return r

def back(palabra):
	palabra1= palabra.lower()
	if len(palabra1) >= 10 and len(palabra1) <= 50 : 
		if caracter_especial(palabra1):
			conteo = letter_count(palabra)
			prob_keys = organizacion_probabilidades(conteo)
			binarios = shannon(prob_keys[0]) 
			keys_prob = organizacion_probabilidades(conteo)
			long_prom = longitud_promedio(keys_prob[0],binarios,palabra1)
			keys_prob = organizacion_probabilidades(conteo)
			ent = entropia(keys_prob[0],palabra1)
			keys_prob = organizacion_probabilidades(conteo)
			efi = eficiencia(ent,long_prom)
			keys_prob = organizacion_probabilidades(conteo)
			r = tasa_compresion(keys_prob[1],long_prom)
			var = dict(Long = long_prom, Entropia = ent, Eficiencia = efi, Taza_De_Comprencion = r)
			DicBin = dict(zip(keys_prob[1],binarios))
			DicBin.update(var)
			return DicBin
		else:
			return 2
	else :
		return 1