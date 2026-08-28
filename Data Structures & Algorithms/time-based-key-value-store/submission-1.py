class TimeMap:

    def __init__(self):
        self.dic = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        val = self.dic.get(key, [])
        l = 0
        r = len(val) - 1
        
        while l <= r:
            m = (l + r) // 2
            
            # 1. Exact match? Boom, we are done. Stop wasting time.
            if val[m][1] == timestamp:
                return val[m][0]
                
            # 2. Smaller than requested? Save it, but keep looking right for a closer one.
            elif val[m][1] < timestamp:
                res = val[m][0]
                l = m + 1
                
            # 3. Too big? Look left.
            else:
                r = m - 1
                
        return res
