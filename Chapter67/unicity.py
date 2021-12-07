import math


def cal():
	num_keys = int(input("number of keys: "))
	keys = []
	for n in range(num_keys):
		keys.append(int(input("q = ")))
	R = (input("R = "))
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
	K = 1.0
	for key in keys:
		K *= math.factorial(key)
	print(f"|K| = {format(K, '.1E')}")
	HK = math.log2(K)
	if R is None or R == "" or R.isspace() or R.isalpha() or R == " " \
			or len(R) == 0:
		R = 1.5
		d = 3.2
	else:
		d = (math.log2(keys[0]) - float(R))
	n_null = HK/d
	UD = math.ceil(HK/d)
	print(f"unicity distance is:")
	print(f"ceilling [{round(HK, 5)} / ("
	      f"{round(math.log2(keys[0]), 5)} - {round(float(R), 5)})]")
	print(f" = {round(HK, 5)} / {d}")
	print(f" = {round(n_null, 5)} ~= {UD}")
	if int(input("find the reflect [1] || otherwise [2]: ")) == 1:
		print(f"log2 {keys} = {round(math.log2(keys[0]), 2)} reflect that,")
		print(f"{round(d, 2)} ({round((d/math.log2(keys[0]))*100, 3)}%) out of "
		      f"every {round(math.log2(keys[0]), 2)}")
		print(f'therefore, need at least {UD} letters in a message')
	return HK, UD, d


def expected_deciphers(HK, n, d):
	H2K = HK - d * int(n)
	q = math.pow(2, H2K)
	print(f"if n = {round(n, 5)}, 2^({round(HK, 5)} - {round(d, 5)} x "
	      f"{round(n, 5)}) ~ {format(q, '.1E')} || {q}")


if __name__ == "__main__":
	cal()