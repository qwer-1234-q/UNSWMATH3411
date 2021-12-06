"""
Only for a, b, * three message.
"""
store = []


def cal():
	a = float(input("a: "))
	b = float(input("b: "))
	stop = float(input("stop: "))
	store.append(a)
	store.append(b)
	store.append(stop)
	encode = (input("encode message(ab*): "))
	decode = (input("decode message (num): "))
	end = 1 - store[2]
	if len(encode) > 0:
		en(encode, end)
	else:
		print(f"end is {end}")
		print(f"decode {decode}")
		print("decode message is:")
		de(float(decode), end)


def en(encode, end):
	e = [i for i in encode]
	print(e)
	s = 0
	v = 0
	time = 0
	for n in e:
		if n == "a":
			v = round(v * store[0], 5)
			print(f"a, s{s}, v{v}")
		elif n == "b":
			s = round(s + store[0] * v, 5)
			v = round(v * store[1], 5)
			print(f"b, s{s}, v{v}")
		elif n == "*":
			s = round(s + end * v, 5)
			v = round(v * store[2], 5)
			print(f"*, s{s}, v{v}")
		time += 1
	print(f'the interval is [{s}, {s+v})')


def de(decode, end):
	if decode >= store[0]:
		decode = (decode - store[0]) / store[1]
		print("s2")
	elif decode >= 0:
		decode = decode / store[0]
		print("s1")
	if decode < end:
		de(decode, end)
	else:
		print("*")


if __name__ == "__main__":
	cal()