class Solution:
    def asteroids_destroyed(self, mass: int, asteroids: list[int]) -> bool:
        # Sort the input
        asteroids.sort()
        for asteroid in asteroids:
            if asteroid > mass:
                return False
            mass += asteroid

        return True