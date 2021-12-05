import math

end = "q: exit the Vigenere session"
q0r = "If you want to enter the messages by txt (enter 0), you need to " \
     "replace the 'file' address in the readFile() function and add the " \
     "information into vigenereScript.txt"
q0 = "0: enter the information by script"
q1 = "1: Calculate the index of coincidence Ic of the message"
q2 = "2: Calculate the keyword length r (ignoring spaces and punctuation)"

questionList = [q0r, q0, q1, q2, end]


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
				N = len(letter_position)
				M = len(plain)
				printQuestions(True)
				t = input("plz input the question number: ")
				t = int(t)
			else:
				message, length = collect_Message()
				N, M, letter_position, plain = letter_group()
			if t == 1:
				index_Coincidence(message, length, N, M, letter_position, 0)
			elif t == 2:
				index_Coincidence(message, length, N, M, letter_position, 2)
		except ValueError:
			print("ValueError: exit the Vigenere")


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
		keyword_Length(message, length, IC)
	else:
		type = int(input("exit[0] || Keyword length[1]"))
		if type == 0:
			print("exit the Vigenere cipher")
		elif type == 1:
			keyword_Length(message, length, IC)
	return IC


def keyword_Length(message, length, IC):
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


if __name__ == "__main__":
	cal()