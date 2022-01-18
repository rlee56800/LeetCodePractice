class MedianFinder:
    
    def __init__(self):
        self.nums_list = []

    def addNum(self, num: int) -> None:
        if not self.nums_list: # no numbers in list
            self.nums_list.append(num)
        elif len(self.nums_list) == 1: # if only one number in list
            self.nums_list.append(num)
            self.nums_list.sort()
        else: # if 2 numbers in list
            self.nums_list.append(num)
            self.nums_list.sort()
            self.nums_list = [self.nums_list[1]]

    def findMedian(self) -> float:
        if len(self.nums_list) == 1:
            return self.nums_list[0]
        else:
            return sum(self.nums_list)/2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
