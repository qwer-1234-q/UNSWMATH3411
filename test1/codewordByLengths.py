from test3 import encode


def cal():
	N = int(input("Number of codewords: "))
	radix = int(input("radix: "))
	codeword = []
	for n in range(N):
		c = int(input(f"{n + 1}: "))
		codeword.append(c)
	if radix == 2:
		m = encode.matrix(N, codeword)
	else:
		m = encode.matrix_Shannon(N, codeword, radix)



if __name__ == "__main__":
	cal()