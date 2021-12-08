"""
Cyclotomic cosets are useful in the construction of q-ary cyclic codes of
length n. To define the q-ary cyclotomic cosets modulo n, we consider a
binary relation on the integers in {0, 1, 2, …, n − 1}.
Given two integers a and b in {0, 1, 2, …, n − 1}, we say that a is related to
b if b = a q^i for some integer i, with all calculations performed modulo
n. It is clear that this relation is reflexive and transitive. When
q and n are relatively prime, this relation is also symmetric, and hence is an
equivalence relation. Given positive integers q and n that are relatively
prime, the q-ary cyclotomic cosets are the equivalence classes defined by
this binary relation.

A cyclotomic coset in general has the form
									{s, sq, sq^2, sq^3, …}
for some non-negative integer s.
"""
import math

introduction = "Cyclotomic cosets are useful in the construction of q-ary " \
               "cyclic codes of length n. To define the q-ary cyclotomic " \
               "cosets modulo n, we consider a binary relation on the " \
               "integers in {0, 1, 2, …, n − 1}. Given two integers a and b " \
               "in {0, 1, 2, …, n − 1}, we say that a is related to b if b = " \
               "a q^i for some integer i, with all calculations performed " \
               "modulo n. It is clear that this relation is reflexive and " \
               "transitive. When q and n are relatively prime, this relation " \
               "is also symmetric, and hence is an equivalence relation. " \
               "Given positive integers q and n that are relatively prime, " \
               "t q-ary cyclotomic cosets are the equivalence classes " \
               "defined by this binary relation.\n\nA cyclotomic coset in " \
               "general has the form\n\t\t{s, sq, sq^2, sq^3, …} " \
               "for some non-negative integer s."


def cyclotomic(p, m, s):
	K = {}
	for i in range(1, s + 1):
		k = []
		sp = 0
		power = 0
		done = False
		while not done:
			sp = int((i * math.pow(p, power)) % (math.pow(p, m) - 1))
			if sp not in k:
				k.append(sp)
			else:
				done = True
			power += 1
		print(f"K{i} = {k}")
		K[i] = k
	return K


def cal():
	print("This is cyclotomic cosets")
	print(introduction)
	print("-"*80)
	print("GD(p^m), Plz enter p and m separably")
	p = int(input("Field GF p = "))
	m = int(input("Field GF m = "))
	k = int(input("Required index s = "))
	cyclotomic(p, m, k)


if __name__ == "__main__":
	cal()
