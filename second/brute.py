import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def distance(p1, p2):
        return np.power(p1.x-p2.x, 2) + np.power(p1.y-p2.y, 2)

    def __str__(self):
        return '(%s,%s)' % (self.x, self.y)

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.y < other.y


class Brute:

    def __init__(self):
        self.points = []
        self.p1 = []
        self.p2 = []
        self.dis = 1e6

    def clear(self):
        self.points.clear()

    def inputs(self, auto=False):

        if auto:
            n = int(input('请输入点的个数:'))
            i = 0
            while i < n:
                x = np.random.randint(-10, 10)
                y = np.random.randint(-10, 10)
                if not self.points.__contains__(Point(x, y)):
                    self.points.append(Point(x, y))
                    i += 1
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

    def solve(self, l, r):

        if l == r - 1:
            if Point.distance(self.points[l],self.points[r]) < self.dis:
                self.dis = Point.distance(self.points[l],self.points[r])
                self.p1.append(self.points[l])
                self.p2.append(self.points[r])
            return Point.distance(self.points[l], self.points[r])
        if l > r - 1:
            return 1e6

        mid = (l + r)//2
        ldis = self.solve(l, mid)
        rdis = self.solve(mid + 1, r)

        dis = 1e6
        for i in range(l, mid + 1):
            p1 = self.points[i]
            for j in range(mid+1, r+1):
                p2 = self.points[j]
                if dis > Point.distance(p1, p2):
                    dis = Point.distance(p1, p2)
                if dis < self.dis:
                    self.dis = dis
                    self.p1.append(p1)
                    self.p2.append(p2)
        return min(ldis, rdis, dis)

    def run(self):

        self.points.sort()
        print(self.solve(1, len(self.points)-1))
        print('找到的点:')
        print(self.p1[-1],self.p2[-1])
        self.plot(self.p1, self.p2)

    def plot(self,p1,p2):

        fig = plt.figure(figsize=(8, 4))
        ax = fig.add_subplot(111)
        for p in self.points:
            plt.scatter(p.x, p.y, c='green')
            plt.annotate('(%s,%s)'%(p.x, p.y), xy=(p.x, p.y), xytext=(p.x, p.y-.5),textcoords='offset points',
                         ha='center', va='top')

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
    b = Brute()
    b.inputs(True)
    b.run()