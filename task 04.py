n = int(input())
shapes = {}

for i in range(n):
    line = input().split()
    shapes.update({line[0] : line[1:]})

find_shape = input()

for elem in shapes:
    if find_shape in shapes[elem]:
        print(elem)
