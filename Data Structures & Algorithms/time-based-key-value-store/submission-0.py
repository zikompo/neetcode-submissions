class TimeMap:

    def __init__(self):
        # key value means using a dict
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # value will probably be a tuple (timestamp, value)
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        # simplest case is there being no key in the dict
        if key not in self.timeMap:
            return ""
        # timestamps are strictly increasing, so don't need to do sorting
        
        # because we are looking for timestamp_prev <= timestamp, we track
        # maximum value less than timestamp

        values = self.timeMap[key]        
        def binary_search(l, r, best):
            if l > r:
                return "" if best == -1 else values[best][1]
            m = l + (r-l)//2
            t = values[m][0]
            if t == timestamp:
                return values[m][1]
            elif t < timestamp:
                return binary_search(m+1, r, m)
            else:
                return binary_search(l, m-1, best)
        return binary_search(0, len(values)-1, -1)
            
            



# {"alice":[(1, "happy"), (3, "sad"), (4, "bad"), (5, "has")]}