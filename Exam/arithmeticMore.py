
def cal():
	N = int(input("Number of input (including stop): "))
	store = []
	for n in range(N):
		if n + 1 == N:
			a = float(input(f"P(*/stop): "))
		else:
			a = float(input(f"P(S{n+1}): "))
		store.append(a)
	encode = (input("encode message (ab*): "))
	decode = (input("decode message (num): "))
	end = 1 - store[2]
	if len(encode) > 0:
		en(encode, end, store, N)
	else:
		print(f"end is {end}")
		print(f"decode {decode}")
		print("decode message is:")
		de(float(decode), end, store, N)


def en(encode, end, store, N):
	e = [i for i in encode]
	print(e)
	s = 0
	v = 0
	time = 0
	for n in e:
		if n != "s":
			ind = store.index(int(n))
			if ind + 1 != N:
				if ind != 0:
					v = round(v * int(store[ind]), 5)
					print(f"S{ind + 1}, s{s}, v{v}")
				else:
					s = round(s + int(store[ind]) * v, 5)
					v = round(v * int(store[ind - 1]), 5)
					print(f"S{ind + 1}, s{s}, v{v}")
			else:
				s = round(s + end * v, 5)
				v = round(v * int(store[2]), 5)
				print(f"*, s{s}, v{v}")
			time += 1
	print(f'the interval is [{s}, {s+v})')


def position(decode, N):
	pos = []
	for n in range(N):
		p = 0
		for m in range(N):
			if n != m and decode[n] < decode[m]:
				p += 1
		pos[p] = n
	return pos


def de(decode, end, store, N):
	pos = position(store, N)
	find = N
	while find > 0:
		if decode >= store[pos[N]]:
			decode = (decode - store[0]) / store[1]
			print(f"s{find}")
			find -= 1
		elif decode >= 0:
			decode = decode / store[0]
			print(f"s{find}")
			find -= 1
		if decode < end:
			de(decode, end, store, N)
		else:
			print("*")


if __name__ == "__main__":
	cal()