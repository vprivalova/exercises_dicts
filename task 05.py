n = int(input())

tree = {}

for i in range(n):
    line = input().split()
    if tree.get(line[0]) is None:
        tree.update({line[0]: [line[1]]})
    else:
        tree[line[0]].append(line[1])

person = input()


def descendants(fam_tree, x):
    if fam_tree.get(x) is None:
        return 0
    else:
        counter = 0

        for elem in fam_tree[x]:
            counter = counter + descendants(fam_tree, elem) + 1

    return counter


print(descendants(tree, person))
