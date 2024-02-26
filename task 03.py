n = int(input())
opposites = {}

for i in range(n):
    line = input().split()
    opposites.update({line[0]: line[1]})

find_word = input()

counter = 0

if opposites.get(find_word) is not None:
    print(opposites[find_word])
    counter += 1
else:
    for keys in opposites:
        if opposites[keys] == find_word:
            print(keys)
            counter += 1

if counter == 0:
    print(find_word)
