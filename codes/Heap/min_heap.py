class MinHeap:
    def __init__(self) -> None:
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1
    
    def _right_child(self, index):
        return 2 * index + 2
    
    def _parent(self, index):
        return (index -1) //2
    
    def _heapfy_up(self, index):
        if index == 0:
            return

        parent_index = self._parent(index)

        if self.heap[index] < self.heap[parent_index]:
            self.heap[index] ,self.heap[parent_index] = self.heap[parent_index], self.heap[index] 
            self._heapfy_up(parent_index)

    def _heapfy_down(self, index):
        size = len(self.heap)

        left = self._left_child(index)
        right = self._right_child(index)

        index_of_smallest = index

        if left < size and self.heap[left] < self.heap[index_of_smallest]:
            index_of_smallest = left

        if right < size and self.heap[right] < self.heap[index_of_smallest]:
            index_of_smallest = right

        if index_of_smallest != index:
            self.heap[index], self.heap[index_of_smallest] = self.heap[index_of_smallest], self.heap[index]
            self._heapfy_down(index_of_smallest)
    
    def insert(self, value):
        self.heap.append(value)
        self._heapfy_up(len(self.heap)-1)

    def getMin(self):
        if len(self.heap) == 0:
            raise IndexError("heap is empty")
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapfy_down(0)

        return root
    
    def display(self):
        print(self.heap)
        
minHeap = MinHeap()
minHeap.insert(0)
minHeap.insert(1)
minHeap.insert(2)
minHeap.insert(3)
minHeap.insert(4)
minHeap.insert(5)       #   [0, 1, 2, 3, 4, 5]
minHeap.insert(0)       #   [0, 1, 0, 3, 4, 5, 2]
print(minHeap.getMin()) # 0 [0, 1, 2, 3, 4, 5]
                         


minHeap.display()
