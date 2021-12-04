

def cal():
	print("LZ78 algorithm")
	try:
		t = int(input("Get decode [0] || Get encode[1]:"))
	except ValueError:
		print("typing error: please retype")
		cal()
	if t == 0:
		decode()
	elif t == 1:
		encode()


def decode():
	print("empty is end")
	print("# is number and & is symbol\n Don't need to enter , or (, or )")
	N = int(input("number of input:"))
	# m = input("(#, &): ")
	message = {}
	# num = 1
	for n in range(N):
		m = input("(#, &): ")
		if m is not None or m != "":
			i = m.split(" ")
			x = int(i[0])
			y = i[1]
			mm = []
			if len(message) >= x > 0:
				kk = message[x]
				mm = kk.copy()
			mm.append(y)
			message[n + 1] = mm
			print(f"({x}, {y}) = {mm}")
			
	
	s = ''
	for num in range(len(message)):
		me = message[num + 1]
		for i in me:
			s += i
	
	print(f"encoded: \n{s}")
	

def encode():
	s = [i for i in input("encode message:")]
	message = {}
	num = 0
	p = []
	for i in s:
		p.append(i)
		n = getMessageKey(num, p, message)
		k = []
		if n > -2:
			if n >= 0:
				k = [n, i, p]
			elif n == -1:
				k = [num, i, p]
			message[num] = k
			num += 1
			p = []
	print("-"*40)
	print("output", "|","new dictionary entry")
	for i in range(num):
		print(f"({message[i][0]}, {message[i][1]}) = {message[i][2]}")
	print(f'\ntotal is {num}')
	print("-" * 40)

def getMessageKey(num, i, message):
	if num == 0:
		return 0
	pos = 0
	col = -1
	for mf in range(len(message)):
		m = message[mf][2]
		find = True
		for k in range(len(m)):
			if m[k] != i[k]:
				find = False
				break
			elif len(m) == len(i) and k + 1 >= len(m):
				return -2
		if find and len(m) + 1 == len(i):
			col = message[mf][0] + 1
		pos += 1
	return col


if __name__ == "__main__":
	cal()