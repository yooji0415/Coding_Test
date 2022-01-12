point_list = []
x_list = []
y_list = []
for i in range(3):
    point = list(map(int, input().split()))
    point_list.append(point)
    x_list.append(point[0])
    y_list.append(point[1])

for x in x_list:
    for y in y_list:
        if [x, y] not in point_list:
            print("{} {}".format(x, y))
            break
            