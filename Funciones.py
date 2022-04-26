

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


if __name__ == "__main__":
	palabra = input('Ingrese el texto\n')
	palabra1= palabra.lower()
	if len(palabra1) >= 10 and len(palabra1) <= 50 : 
		if caracter_especial(palabra1):
			conteo = letter_count(palabra)
			prob_keys = organizacion_probabilidades(conteo)
			binarios = shannon(prob_keys[0]) 
			print(prob_keys[1])
			print(binarios)
		else:
			print('Caractes invalidos')
	else :
		print('tamaño no soportado')
