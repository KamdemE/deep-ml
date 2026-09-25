import numpy as np

def hamming_distance_kanerva(state: list, prototypes: list, threshold: int) -> tuple:
	"""
	Compute Hamming distances and find active prototypes for Kanerva coding.

	Args:
		state: Binary state vector (list of 0s and 1s).
		prototypes: List of binary prototype vectors.
		threshold: Maximum Hamming distance for a prototype to be active.

	Returns:
		Tuple of (distances, active_indices).
	"""
	L=[0 for _ in range(len(prototypes))]
	M=[]
	for i in range(len(state)):
		for j in range(len(prototypes)):
			if state[i]!=prototypes[j][i]:
				L[j]+=1
			
	for i in range(len(L)):
		if L[i]<=threshold:
			M.append(i)
	
	return tuple([L,M])
	pass