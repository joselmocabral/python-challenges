def dbl_linear(n):
	list_num = [1]
	for x in range(0, n):
	    list_num.append(2 * list_num[x] + 1)
	    list_num.append(3 * list_num[x] + 1)
	list_num = list(set(list_num))
	list_num.sort()
	return list_num[n]