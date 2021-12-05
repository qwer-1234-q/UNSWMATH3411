import math


def cal():
	keys = int(input("q = "))
	R = float(input("R = "))
	HK, UD, d = unicity(keys, R)
	expect_d_test(HK, 0, d)


def expect_d_test(HK, n, d):
	try:
		n = int(input("n-letter ciphertext: "))
		expected_deciphers(HK, n, d)
		expect_d_test(HK, n, d)
	except ValueError:
		print("exit the unicity")



def unicity(keys, R):
	HK = math.log2(math.factorial(keys))
	d = (math.log2(keys) - R)
	UD = math.ceil(HK/d)
	print(f"unicity distance is ceilling({round(HK, 5)} / ("
	      f"{round(math.log2(keys), 5)} -"
	      f" {round(R, 5)}) ) = {UD}")
	print(f"log2 {keys} = {round(math.log2(26), 2)} reflect that,")
	print(f"{round(d, 2)} ({round((d/math.log2(26))*100, 3)}%) out of "
	      f"every "
	      f"{round(math.log2(26), 2)}")
	print(f'therefore, need at least {UD} letters in a message')
	return HK, UD, d


def expected_deciphers(HK, n, d):
	H2K = HK - d * int(n)
	q = math.pow(2, H2K)
	print(f"if n = {round(n, 5)}, 2^({round(HK, 5)} - {round(d, 5)} x "
	      f"{round(n, 5)}) ~ {format(q, '.1E')} || {q}")


if __name__ == "__main__":
	cal()