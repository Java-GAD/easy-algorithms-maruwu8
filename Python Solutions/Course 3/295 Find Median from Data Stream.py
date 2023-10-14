'''
The median is the middle value in an ordered integer list. If the size of the list is even,
there is no middle value, and the median is the mean of the two middle values.
For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:
MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

Example 1:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]
'''

from heapq import heappush, heappop

# ---> MAX HEAP + MIN HEAP - get the median in O(1) time by popping the top of both the max heap and min heap
class MedianFinder:
    def __init__( self ):
        # ---> initialize two heaps: a max heap for the left half and a min heap for the right half
        self.min_heap = []  # ---> right half
        self.max_heap = []  # ---> left half

    def addNum( self, num: int ) -> None:
        # ---> push the negative of 'num' to the max heap to simulate a min heap
        heappush(self.max_heap, -num)

        # ---> push the maximum element from the max heap to the min heap
        heappush(self.min_heap, -heappop(self.max_heap))

        # ---> ensure that the size of the min heap is not greater than the size of the max heap
        if len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian( self ) -> float:
        if len(self.max_heap) > len(self.min_heap):
            # ---> if the max heap is larger than the min heap, return the maximum value in the max heap
            return -self.max_heap[0]

        # ---> if equal, return the average of the maximum value in the max heap and the minimum value in the min heap
        return (-self.max_heap[0] + self.min_heap[0]) / 2
