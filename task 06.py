n_info = int(input())
m_info = int(input())

cities = []
cities_dict = {}
lengths = {}
for i in range(m_info):
    line = input().split()
    if line[0] not in cities:
        cities.append(line[0])
    if line[1] not in cities:
        cities.append(line[1])

    if lengths.get(line[0]) is None:
        lengths[line[0]] = [[line[1], int(line[2])]]
    else:
        lengths[line[0]].append([line[1], int(line[2])])


find_path = input().split()

for j in range(n_info):
    cities_dict.update({cities[j]: j})


def dict_to_list(d):
    list_done = []
    for elem in d:
        for i in d[elem]:
            list_done.append([elem, i[0], i[1]])
            list_done.append([i[0], elem, i[1]])

    for j in range(len(list_done)):
        list_done[j] = [cities_dict[list_done[j][0]], cities_dict[list_done[j][1]], list_done[j][2]]

    return list_done


def lst_to_matrix(g):
    n = max(max(v1, v2) for v1, v2, c in g) + 1
    m = []
    for i in range(n):
        m.append([float('inf')]*n)
    for v1, v2, c in g:
        m[v1][v2] = c
    return m


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


def count_path(bg, eg, p):
    result_path = [bg]
    k = p[bg][eg]
    if k == float('inf'):
        return
    count_path(bg, k, p)
    result_path.append(k)
    count_path(k, eg, p)

    result_path.append(eg)
    return result_path


list_lenghts = dict_to_list(lengths)
mtr = lst_to_matrix(list_lenghts)
mct, path = floyd(mtr)


result_points = count_path(cities_dict[find_path[0]], cities_dict[find_path[1]], path)

answer = 0
for i in range(len(result_points) - 1):
    for elem in list_lenghts:
        if elem[0] == result_points[i] and elem[1] == result_points[i + 1]:
            answer = answer + elem[2]
print(f'Длина пути: {answer}')

answer_path = []
for elem3 in result_points:
    for item in cities_dict:
        if cities_dict[item] == elem3:
            answer_path.append(item)

print(f'Путь: {"-".join(answer_path)}')
