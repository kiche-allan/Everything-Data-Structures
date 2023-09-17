class SmallestInfiniteSet:

    def __init__(self):
        self.present = [True for _ in range(1001)]
        

    def popSmallest(self) -> int:
        for x in range(1, 1001):
            if self.present[x]:
                self.present[x] = False
                return x
        

    def addBack(self, num: int) -> None:
        self.present[num] = True