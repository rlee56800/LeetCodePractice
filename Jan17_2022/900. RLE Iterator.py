'''We can use run-length encoding (i.e., RLE) to encode a sequence of integers. In a run-length encoded array of even length encoding (0-indexed), for all even i, encoding[i] tells us the number of times that the non-negative integer value encoding[i + 1] is repeated in the sequence.

    For example, the sequence arr = [8,8,8,5,5] can be encoded to be encoding = [3,8,2,5]. encoding = [3,8,0,9,2,5] and encoding = [2,8,1,8,2,5] are also valid RLE of arr.

Given a run-length encoded array, design an iterator that iterates through it.

Implement the RLEIterator class:

    RLEIterator(int[] encoded) Initializes the object with the encoded array encoded.
    int next(int n) Exhausts the next n elements and returns the last element exhausted in this way. If there is no element left to exhaust, return -1 instead.
'''

class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.pointer = 0
        self.generated_arr = []
        
        for i in range(0, len(encoding), 2):
            self.generated_arr.extend([encoding[i+1]] * encoding[i])

    def next(self, n: int) -> int:
        if n > len(self.generated_arr):
            self.generated_arr = []
            return -1
        else:
            ret = self.generated_arr[n-1]
            del self.generated_arr[:n]
            return ret

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
