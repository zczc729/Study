from figure import Figure

class X(Figure):

    def draw(self):
        output = ''
        for i in range(self.height):
            print('{:<i}{:>self.height}'.format(self.ch, self.ch))
        # for i in range(self.height):
        #     for j in range(i, self.height):
        #         if j == 0:
        #             output += self.ch
        #         if j == self.height - i:
        #             output += self.ch
        #         else:
        #             output += ' '
        #     output += '\n'
        # print(output)
                    