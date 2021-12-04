def reISBN(isbn, wrong):
	isbn = [i for i in isbn]
	if len(isbn) != 10:
		print("isbn is wrong, please retype: ")
		cal()
	isb = []
	for i in isbn:
		if i == 'X' or i == 'X':
			isb.append(10)
		else:
			isb.append(int(i))
	return sumISBN(isb, wrong)


def sumISBN(isbn, wrong):
	s = 0
	for i in range(10):
		if i+1 != wrong:
			s += (i+1) * isbn[i]
	return s % 11


def getNum(s, pos):
	i = s
	d = 0
	for d in range(10):
		i = d * pos + s
		if i % 11 == 0:
			break
	return d


def cal():
	isbn = (input("input isbn: "))
	type = int(input("check valid [0] || check wrong position [1]"))
	if type == 1:
		wrong = int(input("wrong position: "))
		s = reISBN(isbn, wrong)
		print(f'the number is {getNum(s, wrong)}')
	else:
		s = reISBN(isbn, 11)
		if s == 0:
			print(f"{isbn} is valid")
		else:
			print(f"{isbn} is not valid, remainder is {s}")
	
	


if __name__ == "__main__":
	cal()
