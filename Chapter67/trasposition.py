# def transposition(p, m, s):
# 	K = {}
# 	for i in range(1, s + 1):
# 		k = []
# 		sp = 0
# 		power = 0
# 		done = False
# 		while not done:
# 			sp = int((i * math.pow(p, power)) % (math.pow(p, m) - 1))
# 			if sp not in k:
# 				k.append(sp)
# 			else:
# 				done = True
# 			power += 1
# 		print(f"K{i} = {k}")
# 		K[i] = k
# 	return K


def cal():
	# print("This is cyclotomic cosets")
	# print(introduction)
	# print("-"*80)
	# print("GD(p^m), Plz enter p and m separably")
	# p = int(input("Field GF p = "))
	# m = int(input("Field GF m = "))
	# k = int(input("Required index s = "))
	# cyclotomic(p, m, k)
	r = 7
	m = "OLEWNDLIHTESSICROCTER"
	cips = []
	cip = []
	for i in range(len(m)):
		if len(cip) == r:
			cips.append(cip)
			cip = []
		cip.append(m[i])
	cips.append(cip)
	print(cips)
	order = [1, 3, 2, 7, 6, 4, 5]
	for l in cips:
		for o in range(r):
			print(f"{l[order[o] - 1]}", end="")
		# print(" ")


if __name__ == "__main__":
	cal()
