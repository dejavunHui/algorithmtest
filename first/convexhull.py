import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

'''
凸包问题的蛮力法解决方案
'''


class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

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
        if self.y != other.y:
            return self.y < other.y
        else:
            return self.x > other.x

    def __hash__(self):
        return hash((self.x, self.y))


class ConvexHull:
    def __init__(self):

        self.points = []

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
        p = []
        n = len(self.points)
        for i in range(n):
            for j in range(i + 1, n):
                # a = self.points[j].y - self.points[i].y
                # b = self.points[i].x - self.points[j].x
                # c = self.points[i].x * self.points[j].y - self.points[i].y * self.points[j].x

                sig1 = 0
                sig2 = 0

                for k in range(n):
                    if k == i or k == j:
                        continue
                    # rs = a * self.points[k].x + b * self.points[k].y - c
                    rs = np.matrix([[self.points[i].x, self.points[i].y, 1],
                                    [self.points[j].x, self.points[j].y, 1],
                                    [self.points[k].x, self.points[k].y, 1]])
                    rs = np.linalg.det(rs)
                    if rs == 0:
                        sig1 += 1
                        sig2 += 1
                    if rs > 0:
                        sig1 += 1
                    if rs < 0:
                        sig2 += 1

                if sig1 == n-2 or sig2 == n-2:
                    if not p.__contains__(self.points[i]):
                        p.append(self.points[i])
                    if not p.__contains__(self.points[j]):
                        p.append(self.points[j])
        print()
        print('找到的定点有:')
        for pp in p:
            print(pp,end=' ')
        self.plot(p)

    def plot(self, points):

        points.sort()
        plow = points[0]
        l = list(filter(lambda ll: ll.x <= plow.x, points))
        r = list(filter(lambda ll: ll.x > plow.x, points))
        l.sort(key=lambda ll: ll.y)
        r.sort(key=lambda ll: -ll.y)
        pp = l + r

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
            pp.append(pp[0])
            for p_ in pp:
                yield p_

        x = []
        y = []

        def update(dot):
            x.append(dot.x)
            y.append(dot.y)
            l.set_data(x, y)
            return l,

        ani = FuncAnimation(fig, update, frames=gen, init_func=init, blit=True)
        ani.save('凸包.gif', writer='imagemagick', fps=3)
        plt.show()


if __name__ == '__main__':
    c = ConvexHull()
    c.inputs(auto=True)
    c.run()