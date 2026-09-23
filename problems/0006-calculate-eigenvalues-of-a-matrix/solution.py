import numpy as np
def roots(a: list)->list[float]:
	delt=(a[1])**2 -(4*a[0]*a[2])
	l1=((-a[1])+np.sqrt(delt))/2
	root=[]
	root.append(l1)
	l1=((-a[1])-np.sqrt(delt))/2
	root.append(l1)
	return root

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	a=[]
	a.append(1)
	a.append(-(matrix[0][0]+matrix[1][1]))
	a.append((matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0]))
	return roots(a)