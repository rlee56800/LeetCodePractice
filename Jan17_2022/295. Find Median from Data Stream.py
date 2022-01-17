'''
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

    For example, for arr = [2,3,4], the median is 3.
    For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:

    MedianFinder() initializes the MedianFinder object.
    void addNum(int num) adds the integer num from the data stream to the data structure.
    double findMedian() returns the median of all elements so far. Answers within 10^-5 of the actual answer will be accepted.

'''

class MedianFinder:
    
    def __init__(self):
        self.nums_list = []

    def addNum(self, num: int) -> None:
        #self.nums_list.append(num)
        for i in range(len(self.nums_list)):
            if num < self.nums_list[i]:
                self.nums_list.insert(i, num)
                return
        self.nums_list.append(num)

    def findMedian(self) -> float:
        half_val = len(self.nums_list)//2
        if len(self.nums_list)%2 == 0:
            return (self.nums_list[half_val - 1] + self.nums_list[half_val])/2.0
        else:
            return self.nums_list[half_val]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
