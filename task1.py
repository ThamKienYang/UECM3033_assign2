import numpy as np
#You can import some modules or create additional functions

def LUdecomp(A):
    sol = []
    n=len(A)
    for j in range(0, n-1):
        for i in range(j+1, n):
            if A[i,j]!= 0.0:
                lam = A[i,j] / A[j,j]
                A[i, j+1:n] = A[i, j+1:n] - lam * A[j, j+1:n]
                A[i, j] = lam
        return A
    return list(sol)

def lu(A, b):
    sol = []
    A=LUdecomp(A)
    for k in range(1,n):
        b[k] = b[k] - np.dot(A[k,0:k], b[0:k])
        b[n-1]=b[n-1]/A[n-1, n-1]   
    for k in range(n-2, -1, -1):
        b[k] = (b[k] - np.dot(A[k,k+1:n], b[k+1:n]))/A[k,k]
    return b
    return list(sol)

def sor(A, b):
    sol = []
    x = np.zeros_like(b)
    ITERATION_LIMIT = 10
    omega = 1.03
    for itr in range(ITERATION_LIMIT):
        for i in range(len(b)):
            sums = np.dot( A[i,:], x )
            x[i] = x[i] + omega*(b[i]-sums)/A[i,i]
    return list(sol)

def solve(A, b):
    condition = np.count_nonzero(A) > 1/2 *len(A)
    if condition:
        print('Solve by lu(A,b)')
        return lu(A,b)
    else:
        print('Solve by sor(A,b)')
        return sor(A,b)

if __name__ == "__main__":
    ## import checker
    ## checker.test(lu, sor, solve)

    A = np.array([[2,1,6], [8,3,2], [1,5,1]])
    b = np.array([9, 13, 7])
    sol = np.linalg.solve(A,b)
    print(sol)
    
    A = np.array([[6566, -5202, -4040, -5224, 1420, 6229],
         [4104, 7449, -2518, -4588,-8841, 4040],
         [5266,-4008,6803, -4702, 1240, 5060],
         [-9306, 7213,5723, 7961, -1981,-8834],
         [-3782, 3840, 2464, -8389, 9781,-3334],
         [-6903, 5610, 4306, 5548, -1380, 3539.]])
    b = np.array([ 17603,  -63286,   56563,  -26523.5, 103396.5, -27906])
    sol = np.linalg.solve(A,b)
    print(sol)
