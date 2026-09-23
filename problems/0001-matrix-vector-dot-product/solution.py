import numpy as np

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	if len(a[0])!=len(b):
		return -1
	else:
		a=np.array(a)
		b=np.array(b)
		return list(a@b)
			