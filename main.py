# Caesar Cipher Encrypt/Decrypt
def caesar(message,shift):
	alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
	msg = ""
	for i in range(len(message)):
		if message[i].upper() in alphabet:
			idx = (alphabet.index(message[i].upper()) + shift) % len(alphabet)
			msg += alphabet[idx]
	return msg

#Vigenere Encrypt
def vigenere_encrypt(text,key):
	alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
	msg = ""
	key = key.upper()
	key = key * 999
	for i in range(len(text)):
		if text[i].upper() in alphabet:
			shift =(alphabet.index(text[i].upper()) + alphabet.index(key[i])) %27
			msg += alphabet[shift]
			
	return msg


# Vigenere Decrypt
def vigenere_decrypt(text, key):
	alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
	msg = ""
	key = key.upper()
	key = key * 999
	for i in range(len(text)):
		if text[i].upper() in alphabet:
			shift =(alphabet.index(text[i].upper()) - alphabet.index(key[i])) %27
			msg += alphabet[shift]
			
	return msg