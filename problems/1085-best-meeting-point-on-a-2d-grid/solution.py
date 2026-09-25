from statistics import multimode, median

def mode_ou_mediane(liste):
    modes = multimode(liste)
    if len(modes) == 1:
        return modes[0]
    else:
        return median(modes)

def best_meeting_point(grid):
    # grid is a list of lists containing 0s and 1s
    # return the minimum total Manhattan distance as an int
    X=[]
    Y=[]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1:
                X.append(i)
                Y.append(j)
    if len(X)==0 and len(Y)==0:
        return 0
    m_x=mode_ou_mediane(X)
    m_y=mode_ou_mediane(Y)
    x=[abs(X[i]-m_x) for i in range(len(X))]
    y=[abs(Y[i]-m_y) for i in range(len(Y))]
    return sum(x)+sum(y)
    pass