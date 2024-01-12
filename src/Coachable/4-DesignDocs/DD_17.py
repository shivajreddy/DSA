from collections import defaultdict


class UndergroundSystem:
    def __init__(self):
        # { (from_station: end_station) : [ ] }
        self._duration = defaultdict(list)
        self._ppl = defaultdict(lambda: [[], []].copy())
        self._customer_checkin = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # self._ppl[id][0].append((stationName, t))
        # store the check in time as the most recent checked in time for this customer
        self._customer_checkin[id] = t

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self._ppl[id][1].append((stationName, t))

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        pass

    foo
    bar
    fam
    adf










# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)


hm = defaultdict(lambda: [[], []].copy())


















