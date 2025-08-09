from typing import List

class Solution:
    """
    Observation: There is only 1 valid solution, so the valid starting index 
                 would never lead to -ve tank

    - First, check if the total gas available is less than the total cost, 
      which means completing the circuit is impossible.
    - Iterate over each station, calculating the remaining gas after traveling to the next one.
    - If at any station the gas in the tank goes negative, 
      - update the starting station to the next index and reset the gas tank.
    - Continue iterating until the entire loop is completed;
    - The last valid starting point will be the result.

    Time : O(N)
    Space: O(1)
    """
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # Early exit condition: if total gas is less than total cost, it's impossible to complete the circuit
        if sum(gas) < sum(cost):
            return -1

        n = len(gas)        # Number of gas stations
        tank = 0            # Current gas in the tank
        start_station = 0   # Starting index of the gas station

        # Loop through each station to check if a circuit is possible
        for i in range(n):
            tank += gas[i] - cost[i]    # Update current gas after reaching the next station

            # If the tank goes negative, reset the starting station & tank
            if tank < 0:
                start_station = i + 1
                tank = 0

        return start_station

