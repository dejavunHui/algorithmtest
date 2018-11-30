import numpy as np


class QuickSort:

    def __init__(self):
        self.a = []

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

    def quick(self, l, r):
        if l < r:
            i = l
            j = r
            temp = self.a[i]
            while i < j:
                while temp < self.a[j] and i < j:
                    j -= 1
                if i < j:
                    self.a[i] = self.a[j]
                    i += 1

                while temp > self.a[i] and i < j:
                    i += 1
                if i < j:
                    self.a[j] = self.a[i]
                    j -= 1
            self.a[i] = temp
            self.quick(l, i - 1)
            self.quick(i + 1, r)

    def run(self):
        print('排序之前的数组:')
        for i in self.a:
            print(i, end=' ')

        self.quick(0, len(self.a) - 1)
        print()
        print('排序以后的数组:')
        for i in self.a:
            print(i, end=' ')


if __name__ == '__main__':
    q = QuickSort()
    q.inputs(True)
    q.run()