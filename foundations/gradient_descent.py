class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        x = init
        newx = 0
        slope = 0
        for _ in range(iterations):
            slope = 2 * x
            x = x - learning_rate * slope


        return round(x,5)
