
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
'''
最近对问题的蛮力法解决
'''


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def distance(p1, p2):
        return np.power(p1.x-p2.x, 2) + np.power(p1.y-p2.y, 2)

    def __str__(self):
        return '(%s,%s)' % (self.x, self.y)


class NearlyPoint:

    def __init__(self):

        self.points = []

    def clear(self):
        self.points.clear()

    def inputs(self, auto=False):
        if auto:
            n = int(input('请输入点的个数:'))
            i = 0
            while i < n:
                i += 1
                x = np.random.randint(-10,10)
                y = np.random.randint(-10,10)
                self.points.append(Point(x,y))

        else:
            n = int(input('请输入点的个数:'))
            i = 0
            while i < n:
                i += 1
                print('请输入第%s个点(x,y):' % i)
                x = int(input('x='))
                y = int(input('y='))
                p = Point(x, y)
                self.points.append(p)
        print('所有点为:')
        for p in self.points:
            print(p, end=' ')

    def run(self):

        p1 = [self.points[0]]
        p2 = [self.points[1]]
        dis = Point.distance(p1[0], p2[0])
        for i in range(len(self.points)):
            for j in range(len(self.points)):
                if i > j:
                    if Point.distance(self.points[i], self.points[j]) < dis:
                        p1.append(self.points[i])
                        p2.append(self.points[j])
                        dis = Point.distance(self.points[i], self.points[j])
        self.plot(p1, p2)
        return p1[-1], p2[-1]

    def plot(self,p1,p2):

        fig = plt.figure(figsize=(8, 4))
        ax = fig.add_subplot(111)
        for p in self.points:
            plt.scatter(p.x, p.y, c='green')
            plt.annotate('(%s,%s)'%(p.x, p.y), xy=(p.x, p.y), xytext=(p.x, p.y-.5),textcoords='offset points',
                            ha='center',va='top')

        l, = ax.plot([], [], 'r-', animated=False)

        def init():

            return l,

        def gen():

            for i, j in zip(p1, p2):
                pp = [i, j]
                yield pp

        x = []
        y = []

        def update(dot):
            x.extend([dot[0].x, dot[1].x])
            y.extend([dot[0].y, dot[1].y])
            if len(x) > 2:
                xx = x[-2:]
                yy = y[-2:]
                l.set_data(xx, yy)
            else:
                l.set_data(x, y)
            return l,

        ani = FuncAnimation(fig, update, frames=gen, init_func=init, blit=True)
        ani.save('最近对.gif', writer='imagemagick', fps=1)
        plt.show()


if __name__ == '__main__':
    p = NearlyPoint()
    p.inputs(True)
    p.run()