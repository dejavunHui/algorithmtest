import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

'''
凸包问题的分治法解决方案
'''


class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    @staticmethod
    def distance(p1, p2):
        return np.power(p1.x-p2.x, 2) + np.power(p1.y-p2.y, 2)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return '(%s,%s)' % (self.x,self.y)

    def __repr__(self):
        return self.__str__()

    def __cmp__(self, other):
        if self.x != other.x:
            return self.x < other.x
        else:
            return self.y < other.y

    def __lt__(self, other):

        return self.x < other.x

    def __hash__(self):
        return hash((self.x, self.y))


class ConvexHull:
    def __init__(self):

        self.points = []
        self.p = []

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

    def run(self):
        n = len(self.points)
        if n == 3:
            self.p = self.points
        else:
            self.points.sort()
            self.p.append(self.points[0])
            self.p.append(self.points[-1])
            self.solve(0,n-1)
            self.solve(n-1,0)
        self.plot(self.p)

    def solve(self, p1, p2):
        max = 0
        index = -1
        if p1 < p2:
            for i in range(p1,p2):
                first = self.points[p1]
                final = self.points[p2]
                pmax = self.points[i]
                area = first.x*final.y + pmax.x*first.y + final.x*pmax.y - pmax.x*final.y - final.x*first.y - first.x*pmax.y
                if area > max:
                    max = area
                    index = i
        else:
            for i in range(p2,p1):
                first = self.points[p1]
                final = self.points[p2]
                pmax = self.points[i]
                area = first.x*final.y + pmax.x*first.y + final.x*pmax.y - pmax.x*final.y - final.x*first.y - first.x*pmax.y
                if area > max:
                    max = area
                    index = i
        if index != -1:
            self.p.append(self.points[index])
            self.solve(p1,index)
            self.solve(index,p2)

    def plot(self, points):

        fig = plt.figure(figsize=(8, 4))
        ax = fig.add_subplot(111)
        for p in self.points:
            plt.scatter(p.x, p.y, c='green')
            plt.annotate('(%s,%s)'%(p.x, p.y), xy=(p.x, p.y), xytext=(p.x, p.y-.5),textcoords='offset points',
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
            x.append(dot.x)
            y.append(dot.y)
            l.set_data(x, y)
            return l,

        ani = FuncAnimation(fig, update, frames=gen, init_func=init, blit=True)
        ani.save('凸包.gif', writer='imagemagick', fps=1)
        plt.show()


if __name__ == '__main__':
    c = ConvexHull()
    c.inputs(auto=True)
    c.run()
