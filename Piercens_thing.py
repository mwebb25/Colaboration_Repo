import copy
# Hint: this prints 3 lines
def ct(A):
    L, M, N = A, copy.copy(A), copy.deepcopy(A)
    L[0][0] += 4
    # Hint: L += M is mutating but L = L + M is non-mutating
    M[1] += [1]
    M[1] = M[1] + [2]
    N[1] = L[0]
    N[1][0] = N[1][0] + 5
    print(M)
    return N
L =	[[4], []]
print(ct(L))
print(L)
