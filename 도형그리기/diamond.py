from figure import Figure

class Diamond(Figure):

    def draw(self):
        for i in range(self.height):
            if i <= int(self.height / 2):
                for j in range(int(self.height / 2)-i):
                    print(" ",end="")
                for j in range(2*i-1):
                    print("*",end="")
            else:
                for j in range(i - int(self.height / 2)):
                    print(" ",end="")
                for j in range((self.height - i)*2-1):
                    print("*",end="")
            print()