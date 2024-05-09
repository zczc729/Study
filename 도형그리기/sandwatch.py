from figure import Figure

class Sandwatch(Figure):

    def draw(self):
        num = 1

        for i in range(self.height, 0 , -2):
            if i == self.height:
                print(self.ch * i)
            else:
                str1 = ' ' * num + self.ch * i + ' ' * num
                num += 1
                print(str1)

        num = num - 1

        for i in range(2, self.height + 1, +2):
            str1 = ' ' * num + self.ch * i + ' ' * num
            num -= 1
            print(str1)



