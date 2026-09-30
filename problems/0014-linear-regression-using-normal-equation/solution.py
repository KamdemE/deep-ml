import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	X=np.array(X)
	Y=np.array(y)
	A=np.linalg.inv(np.transpose(X)@X)
	theta=A@np.transpose(X)@Y
	return theta