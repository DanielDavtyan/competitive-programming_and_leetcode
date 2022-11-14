steps = input()

x = y = 0
coordinates_visited = set()
is_bug = False
for step in steps:
    if step == 'L':
        coordinates_visited.add((x, y))
        coordinates_visited.add((x + 1, y))
        coordinates_visited.add((x, y + 1))
        coordinates_visited.add((x, y - 1))
        x -= 1
    if step == 'R':
        coordinates_visited.add((x, y))
        coordinates_visited.add((x - 1, y))
        coordinates_visited.add((x, y + 1))
        coordinates_visited.add((x, y - 1))
        x += 1
    if step == 'U':
        coordinates_visited.add((x, y))
        coordinates_visited.add((x - 1, y))
        coordinates_visited.add((x + 1, y))
        coordinates_visited.add((x, y - 1))
        y += 1
    if step == 'D':
        coordinates_visited.add((x, y))
        coordinates_visited.add((x - 1, y))
        coordinates_visited.add((x + 1, y))
        coordinates_visited.add((x, y + 1))
        y -= 1

    if (x, y) in coordinates_visited:
        is_bug = True

if is_bug:
    print('BUG')
else:
    print('OK')
