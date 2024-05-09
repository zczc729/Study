from figure import Figure

class X(Figure):

    def draw(self):
        for i in range(self.height):
            for j in range(self.height):
                if i == j or i + j == self.height - 1:
                    print(self.ch, end='')
                else:
                    print(' ', end='')
            print()
                    