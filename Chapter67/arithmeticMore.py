
en_de = ["encode message (ab*/s1s2*) (only use s1s2*) ",
         "decode message (num) "]


def cal():
	print("Here is arithmetic coding.")
	try:
		N = int(input("Number of input (including stop): "))
		store = []
		for n in range(N):
			if n + 1 == N:
				a = float(input(f"P(*/stop): "))
			else:
				a = float(input(f"P(S{n+1}): "))
			store.append(a)
		t = int(input(f"{en_de[0]}[0] || {en_de[1]}[1]:"))
		encode_decode = input(f"{en_de[t]}: ")
		if t == 0:
			encode_message(encode_decode, store, N)
		else:
			print("decode message is:")
			decode_message(float(encode_decode), store, N)
	except ValueError and Exception:
		if input("Enter [q] exit, otherwise enter all again") != 'q':
			cal()


def encode_message(encode, store, N):
	end = 1 - store[N - 1]
	en = [i for i in encode]
	s = 0
	v = 1
	for i in range(len(en)):
		if en[i] not in ["s", "S"]:
			if en[i] == "*":
				s = round(s + end * v, 5)
				v = round(v * store[N - 1], 5)
				print(f"*, start: {s}, width {v}")
			else:
				if int(en[i]) - 2 < 0:
					ind = 0
					inv = store[int(en[i]) - 1]
				else:
					ind = store[int(en[i]) - 2]
					inv = store[int(en[i]) - 1]
				if int(en[i]) - 1 == 0:
					v = round(v * inv, 5)
					print(f"s{en[i]}, start: {s}, width {v}")
				else:
					s = round(s + ind * v, 5)
					v = round(v * inv, 5)
					print(f"s{en[i]}, start: {s}, width {v}")
	print(f'the interval is [{s}, {s+v})')


def decode_interval(store):
	interval = []
	i = 0.0
	for s in store:
		interval.append(i)
		i += s
	interval.append(i)
	print(interval)
	return interval


def decode_message(decode, store, N):
	interval = decode_interval(store)
	decode = float(decode)
	message = []
	print(f"end is ({interval[-2]}, {interval[-1]}) decode {decode}")
	while interval[-2] >= decode:
		for st in range(len(interval) - 1, -1, -1):
			if interval[-2] <= decode <= interval[-1]:
				break
			if 0 <= st < N and decode >= interval[st]:
				decode = float((decode - interval[st]) / store[st])
				print(f"s{st + 1}, decode {round(decode, 3)}")
				message.append(st + 1)
	print("stop")
	print("summary for decode")
	for m in message:
		print(f"s{m}", end="")
	print("*")


if __name__ == "__main__":
	cal()