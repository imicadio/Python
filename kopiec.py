import heapq
from math import floor

class MaxHeap:
    def __init__(self, data=[]):
        self.data = data

    def left(self, i):
        return i * 2 + 1

    def right(self, i):
        return i * 2 + 2

    def parent(self, i):
        return (i//2) - 1

    # zwraca True, jeżeli w każdym węźle spełniona jest własność kopca typu max
    def is_max_heap(self):
        for i in range(len(self.data)-1):
            if i*2+1 < len(self.data):
                if self.data[i*2+1] >= self.data[i]:
                    return False
            if i*2+2 < len(self.data):
                if self.data[i*2+2] >= self.data[i]:
                    return False
        return True

    def shift_up(self, i):
        parent = (i//2)-1
        while i > 0 and self.data[parent] < self.data[i]:
            self.data[parent], self.data[i] = self.data[i], self.data[parent]
            i = parent
            parent = (i//2)-1

    def shift_down(self, i):
        while True:
            left = i * 2 + 1
            right = i * 2 + 2
            if left < len(self.data) and self.data[left] > self.data[i]:
                largest = left
            else:
                largest = i
            if right < len(self.data) and self.data[right] > self.data[largest]:
                largest = right
            if largest == i:
                break
            else:
                self.data[largest], self.data[i] = self.data[i], self.data[largest]
                i = largest


    # dodaje element do kopca
    # https://en.wikipedia.org/wiki/Binary_heap#Insert
    def insert(self, x):
        i = len(self.data)
        self.data.append(x)
        self.shift_up(i)


    # pobiera element na indeksie 0
    # https://en.wikipedia.org/wiki/Binary_heap#Extract
    def extract(self):
        v = self.data[0]
        self.data[0] = self.data.pop()
        self.shift_down(0)
        return v

    # tworzy kopiec z tablicy
    # https://en.wikipedia.org/wiki/Binary_heap#Building_a_heap
    def build(self, arr):
        self.data = arr
        for i in range(len(self.data)-1,-1,-1):
            self.shift_down(i)

heap = MaxHeap()

heap.build([10, 20, 1, 25, 22, 9])
heap.insert(30)
heap.insert(2)
heap.insert(5)

print(heap.extract())
print(heap.is_max_heap())
print(heap.extract())