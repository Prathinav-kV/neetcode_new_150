class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        nums = self.timeMap[key]
        s,e = 0,len(nums)-1
        value = ""
        while s<=e:
            m = (s+e)//2
            if nums[m][1] <= timestamp:
                value = nums[m][0]
                s = m + 1
            else:
                e = m - 1
        return value
