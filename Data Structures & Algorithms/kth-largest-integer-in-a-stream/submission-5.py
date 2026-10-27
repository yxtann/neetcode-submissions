import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k

        for num in nums:

            # add until we hit a heap of len k while going through the nums list
            if len(self.heap) < k:
                heapq.heappush(self.heap, num)
                continue
        
            # if the num is smaller or equal, don't care about it
            if num <= self.heap[0]:
                continue

            # if the num is bigger, add it in then pop the smallest
            if num > self.heap[0]:
                heapq.heappush(self.heap, num)
                heapq.heappop(self.heap)
                continue

    def add(self, val: int) -> int:

        # Not enough elements in heap to return kth smallest
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
            return self.heap[0]

        if val > self.heap[0]:
            heapq.heappush(self.heap, val)
            heapq.heappop(self.heap)
            
        return self.heap[0]

        
        
