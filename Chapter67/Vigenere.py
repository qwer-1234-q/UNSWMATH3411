import math
from itertools import permutations
import enchant
from enchant.checker import SpellChecker

end = "q: exit the Vigenere session"
q0r = "If you want to enter the messages by txt (enter 0), you need to " \
      "replace the 'file' address in the readFile() function and add the " \
      "information into vigenereScript.txt [not recommend & didn't fix the " \
      "error]"
q0 = "0: enter the information by script"
q1 = "1: Calculate the index of coincidence Ic of the message"
q2 = "2: Calculate the keyword length r (ignoring spaces and punctuation)"
qv = "Polyalphabetic substitution ciphers\n    key || plaintext || ciphertext"
q3 = "3: Collect the ciphertext"
q4 = "4: Collect the plaintext"
q5 = "5: Use plaintext/ciphertext feedback to get the message and the key"
q6 = "6: Decipher the message and try the keys"
q7 = "7: Decipher the message and let the computer to find the key and message"
questionList = [q0r, q0, q1, q2, qv, q3, q4, q5, q6, q7, end]
detext = ["ciphertext", "plaintext"]
o1 = f"[0]: using {detext[0]} feedback to find {detext[1]}"
o2 = f"[1]: using {detext[1]} feedback to find {detext[0]}"
o3 = f"[2]: un-know or can be both"
options = [o1, o2, o3]


def readFile():
	"""
	file is require to replace.
	"""
	file = "UNSWMATH3411/Chapter67/VigenereScript.txt"
	with open(file, "r", encoding="gbk") as f:
		message_done = False
		plain_done = False
		letter_position = []
		plain = []
		message = []
		
		for line in f.readlines():
			line = line.strip('\n')
			print(line)
			if line == " " or line == "\n" or len(line) <= 0:
				continue
			if line.__contains__("## end of message, start for ciphertext"):
				message_done = True
			elif not message_done:
				message += [i for i in line]
			elif line.__contains__("## end of ciphertext"):
				plain_done = True
			elif message_done and not plain_done:
				plain += [i for i in line.split(" ")]
			elif message_done and plain_done:
				tmp = [int(i) for i in line.split(" ")]
				letter_position.append(tmp)
	# f.close()
	print(message)
	print(plain)
	print(letter_position)
	return message, plain, letter_position


def printQuestions(skip):
	print("*" * 80)
	a = 0
	for i in questionList:
		if skip and a <= 1:
			continue
		else:
			print(i)
		a += 1


def printOptions():
	for i in options:
		print(i)


def cal():
	printQuestions(False)
	t = input("plz input the question number: ")
	if t == "q" or t == "" or t is None:
		print("exit the Vigenere session")
	else:
		try:
			t = int(t)
			if t == 0:
				message, plain, letter_position = readFile()
				message, length = manage_message(message)
				letter_position, N = manage_message(letter_position)
				plain, M = manage_message(plain)
				printQuestions(True)
				t = input("plz input the question number: ")
				t = int(t)
			else:
				message, length = collect_Message()
			if 1 <= t <= 2:
				N, M, letter_position, plain = letter_group()
				index_Coincidence(message, length, N, M, letter_position, t)
			elif 3 <= t <= 4:
				key = [i for i in input("Key: ")]
				use_plain_cipher = int(input(f"Encipher the message using "
				                             f"{detext[t - 3]}? yes[1] "
				                             f"|| no[0]"))
				plain_cipher = encrpy_decrypt_message(message, key,
				                                      use_plain_cipher)
				print(f"{detext[t - 3]}: {plain_cipher}")
				# re_encrpy_decrypt(message, key, plain_cipher)
			elif t == 5:
				key = [i.upper() for i in input("Key: ")]
				printOptions()
				pla_cip = int(input())
				solve_message(message, key, length, pla_cip)
			elif t == 6:
				try_key_decipher(message, length)
			elif t == 7:
				r_length = int(input("a keyword of length r = "))
				try_find_key(message, length, r_length)
		except ValueError:
			print("ValueError: exit the Vigenere")
		except ModuleNotFoundError:
			print("ModuleNotFoundError: If you didn't down nltk, "
			      "you can't do q7")


def solve_message(message, key, length, pla_cip):
	if pla_cip <= 1:
		up_key, plain_cipher = unknown_pla_cip(message, key, 0, len(message),
		                                       "", pla_cip, 0)
		print_message(up_key, message, plain_cipher, pla_cip)
	else:
		key0 = key.copy()
		key1 = key.copy()
		up_key, plain_cipher = unknown_pla_cip(message, key0, 0, len(message),
		                                       "", 0, 0)
		print(f"using {detext[0]} feedback to find {detext[1]}")
		print_message(up_key, message, plain_cipher, 0)
		print("-" * 80)
		up_key, plain_cipher = unknown_pla_cip(message, key1, 0, len(message),
		                                       "", 1, 0)
		print(f"using {detext[1]} feedback to find {detext[0]}")
		print_message(up_key, message, plain_cipher, 1)


def print_message(key, message, plain_cipher, pla_cip):
	if pla_cip == 0:
		printText("key", key)
		printText(detext[0], message)
		printText(detext[1], plain_cipher)
	
	elif pla_cip == 1:
		printText("key", key)
		printText(detext[0], plain_cipher)
		printText(detext[1], message)


def printText(start, text):
	print(f"{start}:")
	for i in text:
		print(f"{i}", end="")
	print(f"                || length: {len(text)}\n")


def collect_Message():
	message = [i for i in input("Enter the message: ")]
	message, length = manage_message(message)
	return message, length


def letter_group():
	N = int(input("Number of letter group: "))
	M = int(input("Number of letter: "))
	plain = plaintext(M)
	letter_position = []
	for n in range(N):
		group = []
		for m in range(M):
			pos = enter_Position(n, m)
			if pos is None or pos < 0 or pos == "q":
				return None
			group.append(pos)
		letter_position.append(group)
	print(letter_position)
	return N, M, letter_position, plain


def plaintext(M):
	plain = []
	if M == 26:
		if int(input("Does it A-Z 26 letters? Yes[1] || No[2]: ")) == 1:
			plain = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
	if len(plain) != M:
		for m in range(M):
			p = input(f"{m + 1} code: ")
			plain.append(p)
	print(f"plaintext is {plain}")
	print(f"total plaintext is {len(plain)}")
	return plain


def index_Coincidence(message, length, N, M, letter_position, type):
	fc = 0
	print("Ic(m) = (", end="")
	num_output = 0
	for m in range(M):
		mc = 0
		for n in range(N):
			mc += letter_position[n][m]
		if m + 1 == M:
			print(f"{mc}^{N}", end="")
		else:
			if num_output == 10:
				print("")
				num_output = 0
			print(f"{mc}^{N}", end=" + ")
		num_output += 1
		fc += math.pow(mc, 2)
	print(f") - {length}")
	print("     ", end="")
	print("-" * 80)
	print(f"      {length}^2, {length}")
	fc -= length
	nc = math.pow(length, 2) - length
	IC = round(fc / nc, 5)
	print(f"= {IC}")
	if type == 2:
		keyword_Length(length, IC)
	else:
		type = int(input("exit[0] || Keyword length[1]"))
		if type == 0:
			print("exit the Vigenere cipher")
		elif type == 1:
			keyword_Length(length, IC)
	try_key_decipher(message, length)
	return IC


def keyword_Length(length, IC):
	r = (0.0273 * length) / ((length - 1) * IC - 0.0385 * length + 0.0658)
	print(f"r = {round(r, 5)}")


def manage_message(message):
	length = len(message) - message.count(",") - message.count(".") - \
	         message.count("/") - message.count("!") - message.count(" ")
	return message, length


def enter_Position(n, m):
	pos = -1
	try:
		pos = (input(f"Group[{n + 1}] Letter[{m + 1}]: "))
		pos = int(pos)
	except ValueError and Exception and IndexError:
		print("please enter again and make sure is integer")
		if pos == "q" or pos is None or pos < 0:
			print("exit Vigenere")
			return None
		else:
			pos = enter_Position(n, m)
	return pos

"PI FRB FHQ YHHG AKPV, AKLQ FRBU HQZZLU PV JRYULFA, BHB!"
def try_find_key(message, length, r_length):
	keys = list(permutations(
				[chr(i) for i in range(ord("A"), ord("Z") + 1)], r_length))
	# print(f"all keys:\n{keys}")
	ciphers = {}
	num_key = 0
	min_key = -1
	min_error = len(message)
	for k in keys:
		k = [i for i in k]
		key = get_Key_Equal_message(k.copy(), length)
		cip = unknown_pla_cip(message, key, 0, len(message), "", 1, 0)[1]
		chkr = SpellChecker("en_US")
		chkr.set_text(cip)
		num_error = 0
		for err in chkr:
			num_error += 1
		mes = {
			"key": k,
			"m": cip,
			"err": num_error
			}
		if num_error <= min_error:
			min_error = num_error
			min_key = num_key
		ciphers[num_key] = mes
		num_key += 1
	for kk in range(num_key):
		cc = ciphers[kk]
		key = cc["key"]
		cip = cc["m"]
		err = cc["err"]
		print(f"{kk}:\n  key: {key}\n  decipher: {cip}\n  #error: {err}")
	if min_key >= 0:
		print("most suitable answer:")
		mes = ciphers[min_key]
		key = mes["key"]
		cipher = mes["m"]
		err = mes["err"]
		print(f"   key: {key}\n   decipher: {cipher}\n   #error: {err}")
	if len(ciphers) <= 0:
		print("we can't find the key and the decipher the message")


def get_Key_Equal_message(key, length):
	i = 0
	while len(key) != length:
		key.append(key[i])
		i += 1
	return key


def try_key_decipher(message, length):
	while int(input("Decipher the message [1] || end [2]: ")) == 1:
		k = [i.upper() for i in input("Key: ")]
		cipher = decipher_message_by_key(k, message, length)
		print(f"message: \n   {cipher}")


def decipher_message_by_key(key, message, length):
	key = get_Key_Equal_message(key, length)
	print(f"key: \n{key}")
	return unknown_pla_cip(message, key, 0, len(message), "", 1, 0)[1]


# def re_encrpy_decrypt(message, key, plain_cipher):
# 	plain_cipher = [i for i in plain_cipher]
# 	try:
# 		if int(input("change key[0] || keep [1]")) == 0:
# 			key = [i for i in input("Key: ")]
# 		use_plain = int(
# 			input("Encipher the message using plaintext/ciphertext? "
# 			      "yes[1] || no[0]"))
# 		t = int(input(f"{detext[0]}[0] || {detext[1]}[1]"))
# 		askQue = int(input(f"change [{detext[t]}] to decode/encode [0] "
# 		                   f"|| use previous {detext} to decode/encode [1] "
# 		                   f"|| use previous [message] [2]"))
# 		decode_message = message
# 		if askQue == 0:
# 			decode_message = [i for i in input("Enter text: ")]
# 		elif askQue == 1:
# 			decode_message = plain_cipher
# 		plain_cipher = encrpy_decrypt_message(decode_message, key, use_plain)
# 		print(f"{detext[t]}: {plain_cipher}")
# 		if int(input("continue [0] || exit [1]")) == 0:
# 			re_encrpy_decrypt(decode_message, key, plain_cipher)
# 	except Exception:
# 		print("exit the vigenere function")


def key_rewrite(key, message):
	i = 0
	while len(key) != len(message):
		if message[i] != " ":
			key.append(message[i])
		i += 1
	return key


def encrpy_decrypt_message(message, key, use_plaintext):
	if use_plaintext:
		key = key_rewrite(key, message)
	cipher = ''
	non_alpha_count = 0
	for i in range(len(message)):
		letter = message[i]
		if letter.isalpha():
			letter.upper()
			offset = ord(key[(i - non_alpha_count) % len(key)]) - ord('A')
			cipher += chr((ord(letter) - ord('A') + offset) % 26 + ord('A'))
		else:
			cipher += letter
			non_alpha_count += 1
	return cipher


def unknown_pla_cip(message, key, i, num, pla_cip_m, pla_cip, non_alpha_count):
	if i < num:
		letter = message[i]
		if letter.isalpha():
			letter.upper()
			chart = ""
			if pla_cip == 0:
				offset = ord(key[(i - non_alpha_count) % len(key)]) - ord('A')
				chart = chr((ord(letter) - ord('A') + offset) % 26 + ord('A'))
			elif pla_cip == 1:
				chart = chr((ord(letter) - ord(key[i - non_alpha_count])) % 26 + ord("A"))
			pla_cip_m += chart
			if len(key) < num:
				key.append(chart)
		else:
			pla_cip_m += letter
			non_alpha_count += 1
		return unknown_pla_cip(message, key, i + 1, num, pla_cip_m, pla_cip,
		                       non_alpha_count)
	else:
		return key, pla_cip_m


if __name__ == "__main__":
	cal()
