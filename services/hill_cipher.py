import sympy as sym


class HillCipher:
	def __init__(self, key_matrix):
		self.size = len(key_matrix)
		self.key_matrix = sym.Matrix(key_matrix)
		self.__mod = 65
  
	def convert_str_to_list(self, str):
		return [ord(i) - self.__mod for i in str]

	def encrypt_per_size(self, clip_plain_text):
		arr = [self.convert_str_to_list(clip_plain_text)]
		symArr = sym.Matrix(arr)
		res = self.key_matrix * symArr.T
		res = res % 26
		res = res.T
  
		return "".join([chr(i + self.__mod) for i in res])

	def encrypt(self, plain_text: str):
		size = self.size
		cipher_text = ""
  
		plain_text = plain_text.replace(" ", "")
		plain_text = plain_text.upper() # TODO: CHECK LATER
  
		# add padding if len of plaintext is not multiple of size
		if len(plain_text) % size != 0:
			plain_text += "X" * (size - (len(plain_text) % size))
  
		for i in range(0, len(plain_text), size):
			clip_plain_text = plain_text[i:i + size]
			cipher_text += self.encrypt_per_size(clip_plain_text)

		return cipher_text

	def decrypt_per_size(self, clip_cipher_text):
		key_inverse = self.key_matrix.inv_mod(26)
   
		arr = [self.convert_str_to_list(clip_cipher_text)]
		symArr = sym.Matrix(arr)
		res = key_inverse * symArr.T
		res = res % 26
		res = res.T
		return "".join([chr(i + self.__mod) for i in res])

	def decrypt(self, cipher_text):
		size = self.size
		plain_text = ""
		for i in range(0, len(cipher_text), size):
			clip_cipher_text = cipher_text[i:i + size]
			plain_text += self.decrypt_per_size(clip_cipher_text)
			print(plain_text)
		return plain_text
