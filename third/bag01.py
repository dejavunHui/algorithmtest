import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Item:
    def __init__(self, w, v):
        self.w = w
        self.v = v

    def __str__(self):

        return '(重量:%s,价值:%s)' % (self.w, self.v)

    def __repr__(self):

        return self.__str__()


class Bag:

    def __init__(self, C):
        self.C = C
        self.item = []
        self.select = []

    def inputs(self,auto = False):
        n = int(input('请输入物品的个数:'))
        if auto:
            i = 0
            while i < n:
                w = np.random.randint(1, 20)
                v = np.random.randint(0, 20)
                self.item.append(Item(w, v))
                i += 1
        else:
            i = 0
            while i < n:
                i += 1
                w = int(input('请输入第%s个物品的重量:'%i))
                v = int(input('请输入第%s个物品的价值:'%i))
                self.item.append(Item(w, v))
        print('全部物品信息如下:')
        for it in self.item:
            print(it, end=' ')

        print()

    def run(self):
        print('最大价值是:',self.solve(0, self.C))
        self.plot(self.select)

    def solve(self, i, j):#第i个物品,背包容量为j时的价值

        if i == len(self.item):
            return 0
        wi = self.item[i].w
        vi = self.item[i].v
        if j - wi < 0:
            return self.solve(i+1, j)
        if self.solve(i+1, j-wi) + vi > self.solve(i+1, j):
            self.select.append(self.item[i])
            return self.solve(i+1, j-wi) + vi
        else:
            return self.solve(i+1, j)
        # return max(self.solve(i+1, j-wi) + vi, self.solve(i+1, j))

    def plot(self, points):

        fig = plt.figure(figsize=(8, 4))
        ax = fig.add_subplot(111)
        plt.xlabel('W')
        plt.ylabel('V')
        for p in self.item:
            plt.scatter(p.w, p.v, c='green')
            plt.annotate('(%s,%s)'%(p.w, p.v), xy=(p.w, p.v), xytext=(p.w, p.v-.5),textcoords='offset points',
                         ha='center',va='top')

        l, = ax.plot([], [], 'ro', animated=False)

        def init():

            return l,

        def gen():
            for p_ in points:
                yield p_

        x = []
        y = []

        def update(dot):
            x.append(dot.w)
            y.append(dot.v)
            l.set_data(x, y)
            return l,

        ani = FuncAnimation(fig, update, frames=gen, init_func=init, blit=True)
        ani.save('01背包.gif', writer='imagemagick', fps=3)
        plt.show()


if __name__ == '__main__':
    c = int(input('背包的最大容量:'))
    b = Bag(c)
    b.inputs(True)
    b.run()

