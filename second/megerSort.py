import numpy as np
import matplotlib.pyplot as plt


class MegerSort:

    def __init__(self):
        self.a = []

    def clear(self):
        self.a.clear()

    def inputs(self,auto = False):
        n = int(input('请输入排序数的个数:'))
        if not auto:
            i = 0
            while i < n:
                i += 1
                x = int(input('请输入第%s个数:'%i))
                self.a.append(x)
        else:
            i = 0
            while i < n:
                i += 1
                self.a.append(np.random.randint(-10,10))

    def megerSort(self,l,r):

         if r > l:

            mid = (l + r)//2
            self.megerSort(l,mid)
            self.megerSort(mid + 1,r)
            h = l
            i = l
            j = mid + 1
            b = [0] * len(self.a)
            while h <= mid and j <= r:
                if self.a[h] <= self.a[j]:
                    b[i] = self.a[h]
                    h += 1
                else:
                    b[i] = self.a[j]
                    j += 1
                i += 1
            if h > mid:
                for k in range(j, r + 1):
                    b[i] = self.a[k]
                    i += 1
            else:
                for k in range(h, mid + 1):
                    b[i] = self.a[k]
                    i += 1
            for k in range(l, r + 1):
                self.a[k] = b[k]

    def run(self):
        print('排序之前的数组:')
        for i in self.a:
            print(i, end=' ')

        self.megerSort(0, len(self.a) - 1)
        print()
        print('排序以后的数组:')
        for i in self.a:
            print(i, end=' ')


if __name__ == '__main__':

    m = MegerSort()
    m.inputs(True)
    m.run()
