class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        trip_tank, cur_tank, start, n = 0, 0, 0, len(gas)
        for i in range(n):
            cur_tank += gas[i] - cost[i]
            trip_tank += gas[i] - cost[i]
            if cur_tank < 0:
                start = i + 1
                cur_tank = 0
        return start if trip_tank >= 0 else -1
        