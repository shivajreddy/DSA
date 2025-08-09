"""
### Key Idea:
- **Early Exit Condition**: First, the program checks whether the total amount 
  of gas available (`sum(gas)`) is less than the total cost required 
  (`sum(cost)`). If it is, it's impossible to complete the circuit, so it 
  returns `-1`.

- **Greedy Approach**: The idea is to traverse each station while keeping track 
  of the current amount of gas in `curr_tank`. If at any station, the car runs 
  out of gas (`curr_tank < 0`), it means this station or any station before it 
  cannot be the starting point. Therefore, the program updates the starting 
  station (`start_station`) to the next station (`i + 1`) and resets the `curr_tank`.

- **Final Result**: If the entire trip is completed successfully, the starting 
  station is returned. Otherwise, the function returns `-1` when it's not 
  possible to complete the circuit.

### Time Complexity:
- `O(n)`: We are iterating through the `gas` and `cost` lists once.

### Space Complexity:
- `O(1)`: We only use constant extra space.

### Optimizations:
- **Single Pass Check**: By checking `sum(gas) < sum(cost)` initially, the 
  algorithm avoids unnecessary computation for cases where a solution doesn't 
  exist.

- **Greedy Reset Mechanism**: The algorithm doesn't backtrack. It simply resets 
  the start point when it finds an invalid station, which allows the program to 
  stay efficient.

"""

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Determines if it's possible to complete a circular circuit of gas stations,
        starting from a certain index, such that the car never runs out of gas.

        Args:
        gas (List[int]): List of integers representing the gas available at each station.
        cost (List[int]): List of integers representing the cost of gas to travel to the next station.

        Returns:
        int: The index of the station where you should start the circuit. 
             If it's not possible to complete the circuit, returns -1.
        """

        # Early exit condition: if total gas is less than total cost, it's impossible to complete the circuit
        if sum(gas) < sum(cost):
            return -1

        # Initialize variables
        n = len(gas)        # Number of gas stations
        tank = 0            # Current gas in the tank
        start_station = 0           # Starting index of the gas station

        # Iterate through each gas station
        for i in range(n):
            # Calculate the remaining gas after traveling to the next station
            tank += gas[i] - cost[i]

            # If at any point the tank goes negative, reset the starting station
            if tank < 0:
                # Move the starting index to the next station
                start_station = i + 1
                # Reset the tank as we cannot start from the current station
                tank = 0

        # Return the starting station index
        return start_station

