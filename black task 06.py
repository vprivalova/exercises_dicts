
def lst_to_matrix(g):
    n = max(max(v1, v2) for v1, v2, c in g) + 1
    m = []
    for i in range(n):
        m.append([float('inf')]*n)
    for v1, v2, c in g:
        m[v1][v2] = c
    return m


def matrix_to_dict(m):
    d = {}
    n = len(m)
    for v in range(n):
        d[v] = []
    for v1 in range(n):
        for v2 in range(n):
            if m[v1][v2] != float('inf'):
                d[v1].append((v2, m[v1][v2]))
    return d


def floyd(m):
    n = len(m)
    p = []
    for i in range(n):
        p.append([float('inf')] * n)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if m[i][k] + m[k][j] < m[i][j]:
                    m[i][j] = m[i][k] + m[k][j]
                    p[i][j] = k
    return m, p


def print_path(i, j, p):
    k = p[i][j]
    if k == float('inf'):
        return
    print_path(i, k, p)
    print(f'{k}-', end='')
    print_path(k, j, p)


gr = []

with open('g.txt') as f:
    for x in f:
        gr.append(tuple(int(y) for y in x.split()))
print(gr)
mtr = lst_to_matrix(gr)
print('!!')
print(mtr)
print(matrix_to_dict(mtr))
mct, path = floyd(mtr)
print(mct)
print(path)
print('0-', end='')
print_path(0, 4, path)
print('4')
