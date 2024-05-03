from figure import Figure

class Ribbon(Figure):

    def draw(self):
        for i in range(1, int(self.height / 2)):
            print(self.ch * i + " " * (self.height - i * 2) + self.ch * i)
        for i in range(int((self.height - 1) / 2), 0, -1):
            print(self.ch * i + " " * (self.height - i * 2) + self.ch * i)