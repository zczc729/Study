from figure import Figure

class RightTriangle(Figure):

    def draw(self):
        for i in range(self.height):
            print(self.ch * (i + 1))
