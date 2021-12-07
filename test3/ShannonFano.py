import math
import encode
import humman
from itertools import combinations_with_replacement, combinations
import fractions
import question


infor1 = "Shannon-Fano code"
infor2 = "plz retype if you type something wrong."
infor3 = "this function will not assume any errors"
sli = "*" * 50
q1 = "1: encode/decode message/average length of the code \n     " \
     "[eg., L[SF](S)"
q2 = "2: the length of encode codeword "
q3 = "3: average codeword length per  \n     " \
     "{lim[Lsf(S)]/(n)= Hr(S) = -a*log_r(a) ... ~= ?}"
q4 = "4: the probability of the S \n     => don't contain length"
q5 = "5: the length for extension S with lots of prob. \n     " \
     "[order, x-extension(s^n)] \n     " \
     "=> similar with 4 but including length"
end = "q: exit the Shannon-Fano"
questions = [infor1, infor2, infor3, sli, q1, q2, q3, q4, q5, end]


def printQuestions():
	print("*"*80)
	for i in questions:
		print(i)


def cal():
	printQuestions()
	t = input("plz input the question number:")
	if t == "q" or t == "" or t is None:
		print("exit the Shannon-Fano")
	else:
		t = int(t)
		single = [1, 3, 4, 5]
		if t in single:
			N = int(input("number input: "))
			if t == 1:
				t1(N)
			elif t == 3:
				t3(N)
			elif t == 4 or t == 5:
				t4(N, t)
		elif t == 2:
			p = float(input("P(s) = "))
			r = int(input("r-radix: "))
			t2(p, r)
		else:
			print("the number is incorrect, plz retype")
			cal()


def t1(N):
	logg = int(input("type of coding (e.g. binary, ternary): "))
	prob = []
	store = []
	for n in range(N):
		a = float(input(f'p{n + 1} = '))
		prob.append(a)
		pi = 1 / a
		li = round(math.log(pi, logg), 5)
		store.append(math.ceil(li))
		print(f"p{n + 1}: 1/p = {round(pi, 5)} || log_r(pi) = {li} || "
		      f"length = {math.ceil(li)}")
	m = encode.matrix_Shannon(N, store, logg)
	if len(m) == N:
		t = int(input("decode [0] || encode [1] "
		              "|| average length [2] || end [3]: "))
		if t == 1:
			message = [i for i in input("Put encode message: ").split("s")]
			print(message)
			s = ""
			for i in message:
				if i == "" or i is None:
					continue
				else:
					num = int(i)
					s += str(m[num - 1])
			print(s)
		elif t == 0:
			message = [i for i in input("Put decode message: ")]
			print(message)
			decode = []
			code = []
			for i in message:
				code.append(int(i))
				print(code)
				index = findM(code, m)
				print(f"index {index}")
				if index > -1:
					s = "s" + str(index)
					decode.append(s)
					code = []
			if len(code) > 0:
				print(code)
				print("cannot decode")
			else:
				print("decode message is:")
				print("".join(decode))
		elif t == 2:
			k = 0.0
			for i in range(N):
				k += len(m[i]) * prob[i]
			print(f'average length: {round(k, 5)}')


def findM(code, matrix):
	num = -1
	pos = 1
	print(code)
	for m in matrix:
		if len(m) == len(code):
			print(m)
			get = True
			for n in range(len(code)):
				if int(code[n]) != int(m[n]):
					print(f'c is {code[n]} and m is {m[n]}')
					get = False
					break
			if get:
				num = pos
				return num
		pos += 1
	return num


def t2(p, r):
	a = 1 / p
	b = r / p
	L = 0
	while a > math.pow(r, L):
		L += 1
	
	while a <= math.pow(r, L) <= b:
		L += 1
	L -= 1
	print(f"length is {L}")


def t3(N):
	c = int(input("r-radix: "))
	k = 0.0
	for n in range(N):
		num = question.float_fraction(input(f"s[{n + 1}]: "))
		k += humman.hamFra(num, c)
	print(f"{k}")


def t4(N, t):
	r = int(input("r-radix: "))
	F = int(input("find the order: "))
	S = int(input("x-extenstion or S(x): "))
	order = []
	for n in range(N):
		num = question.float_fraction(input(f"s[{n}]: "))
		order.append(num)
		order.sort()
	
	L = list(combinations_with_replacement(range(len(order)), S))
	print(f"not consider replete: {L}")
	store = []
	for i in L:
		num = 1.0
		for j in range(S):
			num *= order[int(i[j])]
		if num not in store:
			store.append(round(num, 7))
		store.sort()
	print(store)
	p = store[F - 1]
	print(f"{p} fraction {fractions.Fraction(p).limit_denominator()}")
	
	Likely = list(combinations(range(len(order)), S))
	print(f"Likely: {Likely}")
	sl = []
	for i in Likely:
		num = 1.0
		for j in range(S):
			num *= order[int(i[j])]
		if num not in store:
			sl.append(round(num, 7))
	p = sl[F - 1]
	print(f"{p} fraction {fractions.Fraction(p).limit_denominator()}")
	
	if t == 5:
		t2(p, r)


if __name__ == "__main__":
	cal()