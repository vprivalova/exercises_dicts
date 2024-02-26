line = input().split()
frequency = {}

for elem in line:
    if frequency.get(elem) is None:
        frequency.update({elem: 1})
    else:
        frequency[elem] += 1

frequency_list = list(frequency.items())
frequency_list.sort(key=lambda item: item[1], reverse=True)

for elem2 in frequency_list:
    print(elem2[0])
