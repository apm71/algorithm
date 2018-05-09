class myArray():
    def __init__(self,low,high,maxsum):
        self.low = low
        self.high = high
        self.maxsum = maxsum

    def __str__(self):
        return '(%i,%i,%d)'%(self.low, self.hgih, self.maxsum)

    def detail(self):
        print('low is ',self.low)
        print('high is ',self.high)
        print('max sum is ',self.maxsum)
