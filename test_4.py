#coding=utf-8
#  4. 用数组实现一个列表类，包括列表的常用操作，实现五个

class mylist:
    def __init__(self,arr=[]):
        self.arr=arr
        # self.arr

    def myappend(self,addarr):
        self.arr=self.arr+[addarr]
        return self.arr

    def myextend(self,addarr):
        self.arr=self.arr+addarr
        return self.arr

    def mysort(self):
        def qsort(arr):
            if len(arr)<=1:
                return arr
            return qsort([n for n in arr[1:] if n <arr[0]]) +arr[0:1] + \
        qsort([m for m in arr[1:] if m >arr[0]])

        self.arr=qsort(self.arr)
        return self.arr

    def mycount(self,num):
        count=0
        for n in self.arr:
            if n==num:
                count+=1
        return count

    def myremove(self,num):
        for i in range(len(self.arr)):
            if self.arr[i]==num:
                self.arr=self.arr[:i]+self.arr[i+1:]
                return self.arr
        else:
            print("%s not in arr." %num)
            return self.arr

    def mypop(self):
        try:
            temp=self.arr[-1]
            self.arr=self.arr[:-1]
            return temp
        except:
            print('IndexError: pop from empty list')

    def myreserve(self):
        self.arr=self.arr[::-1]
        return self.arr

    def __repr__(self):
        return (str(self.arr))

a=mylist()
a.myextend([1,2,4,2,8,20,3])
print(a)
print(a.myreserve())
print(a.mysort())
print(a.mycount(2))
print(a.myremove(2))
print(a.mypop())