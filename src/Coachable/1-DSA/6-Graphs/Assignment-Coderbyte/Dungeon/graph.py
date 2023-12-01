from __future__ import annotations
import collections
from typing import Dict


# =============== BEGIN DO NOT MODIFY ========================
class Treasure:
    pass


class Monster:
    def __init__(self, name: str, damage: int):
        self.name = name
        self.damage = damage
        self.next = []

    def append_monster(self, monster):
        self.next.append(monster)

    def append_treasure(self, treasure: Treasure):
        self.next.append(treasure)

    # def __str__(self):
    #     return f"[Monster:{self.name},{self.damage}]"

    def __repr__(self):
        return f"<Monster:{self.name},{self.damage}>"


class Player:
    def __init__(self, health: int):
        self.health = health

    def battle(self, monster: Monster):
        self.health -= monster.damage


# =============== END DO NOT MODIFY ========================

class Dungeon:
    def __init__(self, monster: Monster):
        self.monster = monster

    def find_all_successful_paths(self):
        successful_paths: list[list[Monster]] = []
        visited: set[Monster] = set()
        q: collections.deque[list[Monster]] = collections.deque()

        q.append([self.monster])

        # BFS to find all the paths from root(self.monster) to Treasure
        while q:
            curr_path = q.popleft()
            curr_monster = curr_path[-1]
            if isinstance(curr_monster, Treasure):
                # paths.append(curr_path[:-1])  # Append a copy of the path without removing the treasure
                curr_path.pop()
                successful_paths.append(curr_path)
                continue
            visited.add(curr_monster)
            for neighbor_monster in curr_monster.next:
                if neighbor_monster not in visited:
                    new_path = curr_path + [neighbor_monster]
                    q.append(new_path)

        return successful_paths

    '''
    Helper function: find the optimal path(lowest damage)
    '''

    def find_optimal_path(self) -> list[Monster]:

        successful_paths = self.find_all_successful_paths()

        optimal_health_required = float('inf')
        optimal_path: list[Monster] = []

        # Iterate over all possible paths to find the optimal path
        # print(f"now paths={successful_paths}")
        for path in successful_paths:
            total_damage = sum([mon.damage for mon in path])
            if total_damage < optimal_health_required:
                optimal_health_required = total_damage
                optimal_path = path
            # print(f"tota_damage={total_damage}, opt_hp={optimal_health_required}")
        return optimal_path

    # Is it possible for player to make it to the end if they start with infinite health?
    def can_at_least_one_path_make_it(self) -> bool:
        optimal_path = self.find_optimal_path()
        return len(optimal_path) > 0

    # Is it possible for player to make it to end without losing all their health?
    def can_make_it(self, player: Player) -> bool:
        optimal_path = self.find_optimal_path()
        optimal_health = sum([mon.damage for mon in optimal_path])

        return player.health >= optimal_health

    '''
    Helper: will all paths make it to Treasure
    Algorithm: DFS, root: self.Monster
    Node state: -1 = doesnt lead to Treasure, 0 = not-visited, 1 = leads to treasure
    Terminal Node: monster with no children (i.e,. self.next is empty)
    '''

    def all_paths_lead_to_treasure(self) -> bool:

        visited: Dict[Monster, int] = collections.defaultdict(int)

        def dfs(node: Monster):
            # print(f"path={path}")
            # print(f"node={node}")
            if visited[node] == 1:
                return True
            elif visited[node] == -1:
                return False
            if isinstance(node, Treasure):
                return True
            if not node.next:
                return False
            visited[node] = -1
            for child in node.next:
                if not dfs(child):
                    return False
            visited[node] = 1
            return True

        return dfs(self.monster)

    # Will any path make it to the end? Can they choose randomly and always make it?
    def can_all_paths_make_it(self, player: Player) -> bool:
        if not self.all_paths_lead_to_treasure():
            return False
        if len(self.get_all_paths()) != len(self.find_all_successful_paths()):
            return False

        for path in self.find_all_successful_paths():
            path_weight = sum([mon.damage for mon in path])
            if player.health < path_weight:
                return False
        return True

    def get_all_paths(self) -> list[list[Monster]]:
        result = []
        q = collections.deque()
        q.append([self.monster])
        visited = set()
        while q:
            curr_path = q.popleft()
            node = curr_path[-1]
            if isinstance(node, Treasure):
                curr_path.pop()
                result.append(curr_path)
                continue
            elif not node.next:
                result.append(curr_path)
                continue
            visited.add(node)
            # result.append(curr_path)
            for neighbor in node.next:
                if neighbor not in visited:
                    new_path = curr_path + [neighbor]
                    q.append(new_path)
        return result

    # TODO - using dfs
    def probability_player_will_make_it(self, player: Player) -> float:

        # base cases
        def dfs(node: 'Monster | Treasure', current_hp):
            if isinstance(node, Treasure):
                return 1.0
            elif not node.next:
                return 0.0
            current_hp -= node.damage
            if current_hp < 0:
                return 0.0

            n = len(node.next)
            child_probs = [dfs(child, current_hp) for child in node.next]
            prob = sum(child_probs) / n
            return prob

        result = dfs(self.monster, player.health)
        return result

    # If picking paths randomly, what is the probability player will make it to the end?
    def x_probability_player_will_make_it(self, player: Player) -> float:
        if not self.can_at_least_one_path_make_it() or not self.can_make_it(player):
            return 0

        q = collections.deque([self.monster])
        visited = set()
        graph: Dict[Monster, list[Monster]] = collections.defaultdict(list)
        while q:
            curr_monster = q.popleft()
            if isinstance(curr_monster, Treasure):
                continue
            if curr_monster in visited:
                continue
            for neighbour_monster in curr_monster.next:
                if neighbour_monster not in visited and not isinstance(neighbour_monster, Treasure):
                    graph[curr_monster].append(neighbour_monster)
                    q.append(neighbour_monster)

        node_probabilities = collections.defaultdict(lambda: 1.0)

        for node in graph.keys():
            p = 1 / len(graph[node])
            node_probabilities[node.name] = p

        path_probabilities = []
        all_paths = self.find_all_successful_paths()
        for path in all_paths:
            path_prob = 1
            for node in path:
                path_prob *= node_probabilities[node.name]

            path_weight = sum([mon.damage for mon in path])
            path_probabilities.append((path_prob, path_weight))

        total_probability = 0
        for path in path_probabilities:
            path_prob, path_weight = path
            if path_weight <= player.health:
                total_probability += path_prob
        return total_probability
