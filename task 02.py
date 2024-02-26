n = int(input())
translator = {}

for i in range(n):
    line = input().split()
    translator.update({line[0]: line[1]})

for_translation = input().split()
result = []

for elem in for_translation:
    if translator.get(elem) is not None:
        result.append(translator[elem])
    else:
        result.append(elem)

print(' '.join(result))
