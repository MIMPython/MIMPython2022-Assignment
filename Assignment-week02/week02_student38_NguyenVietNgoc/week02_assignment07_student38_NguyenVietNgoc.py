def encrypt_rot13(text):
	result = "" 
	for i in range(len(text)):
		char = text[i]

		if (char.isupper() and ord(char) < 78):
			result += chr(ord(char) + 13)

		else:
			result += chr(ord(char) - 13)
	return result

# Encrypt text
text1 = "ATTACKATONCE"
print ("Encrypt ROT-13:  " + encrypt_rot13(text1))   # Encrypt rot13:  NGGNPXNGBAPR

# Decrypt text
text2 = encrypt_rot13(text1)    # text2 = "NGGNPXNGBAPR"
print ("Decrypt ROT-13:  " + encrypt_rot13(text2))   # Decrypt rot13:  ATTACKATONCE
 