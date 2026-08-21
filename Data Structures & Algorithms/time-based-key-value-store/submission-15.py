class TimeMap:

    def __init__(self):
        list_dict = defaultdict(list)
        self.store = list_dict


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.store[key]


        left = 0
        right = len(arr)-1
        ans = -1

        while(left <= right):
            mid = (left+right)//2   
            if arr[mid][1] <= timestamp:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        if ans == -1:
            return ""
        return arr[ans][0]
