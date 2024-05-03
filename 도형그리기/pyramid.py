from figure import Figure

class Pyramid(Figure):
    def draw(self):
        output = ''
        for i in range(self.height):
            for j in range(self.height, i, -1):
                output += ' '
            for j in range(0, 2 * i -1):
                output += self.ch
            output += '\n'
        print(output)