from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        def is_collision(ast_1, ast_2):
            # case 1: <- <- or -> ->
            if (ast_1 < 0 and ast_2 < 0) or (ast_1 > 0 and ast_2 > 0):
                return False

            # case 2: <- ->
            if ast_1 < 0 and ast_2 > 0:
                return False

            # case 3: -> <-
            return True

        def resolve_collision(remaining_asteroids, ast_2):

            while remaining_asteroids:
                ast_1 = remaining_asteroids.pop()

                # resolve collision
                if not is_collision(ast_1, ast_2):
                    remaining_asteroids.append(ast_1)
                    remaining_asteroids.append(ast_2)
                    return
                if ast_1 + ast_2 == 0: return
                big_asteroid = ast_1 if abs(ast_1) > abs(ast_2) else ast_2
                ast_2 = big_asteroid
            remaining_asteroids.append(ast_2)

        final_asteroids = []
        for curr_asteroid in asteroids:
            resolve_collision(final_asteroids, curr_asteroid)
        return final_asteroids
