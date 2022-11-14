n, m = input().split()
rotate, shift = input().split()
array = []
for i in range(int(n)):
    array.append(list(input()))


class BeachRectangle:
    def __init__(self, n, m, array):
        self.n = n
        self.m = m
        self.array = array
        self.blank_spaces = self.find_blank_spaces()

    def find_blank_spaces(self):
        blank_spaces = {}
        for y in range(len(self.array)):
            for x in range(len(array[i])):
                if array[y][x] == '.':
                    blank_spaces[(y, x)] = {'matrix': dict(self.blank_spaces), 'discomfort': 0}
        return blank_spaces

    def move_sunbed(self, direction):
        for coordinates in self.blank_spaces:
            matrix = self.blank_spaces[coordinates]['matrix']
            x, y = coordinates
            if direction == 'up':

            up = matrix[(x, y + 1)]
            down = matrix[(x, y - 1)]
            right = matrix[(x + 1, y)]
            left = matrix[(x - 1, y)]

