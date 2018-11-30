import numpy as np


class SplitQuery:

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
                x = np.random.randint(-20,20)
                if not self.a.__contains__(x):
                    i += 1
                    self.a.append(x)

    def find(self, l, r, aim):
        if r >= l:
            mid = (l + r)//2
            if self.a[mid] == aim:
                return mid
            elif self.a[mid] < aim:
                self.find(l, mid-1,aim)
            else:
                self.find(mid + 1, r, aim)

    def run(self):
        self.a.sort()
        print('数组为:')
        for i in self.a:
            print(i,end=' ')
        print()
        aim = int(input('请输入要查找的数:'))
        print('查找的数的位置在', self.find(0, len(self.a) - 1, aim) + 1)



if __name__ == '__main__':

    s = SplitQuery()
    s.inputs(True)
    s.run()

