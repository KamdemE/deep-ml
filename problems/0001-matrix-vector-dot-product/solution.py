def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	if len(a[0])!=len(b):
		return -1
	else:
		M=[]
		for i in range(len(a)):
			sums=0
			for j in range(len(a[0])):
		   		sums=sums+a[i][j]*b[j]
			M.append(sums)
		return M
			