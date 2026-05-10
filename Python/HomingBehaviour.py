# COMP204 Winter 2026 -- Exercise 10
# Question 1 - Homing Behaviour in Rodents

# Anything outside of any function will not be graded, 
# but you may write helper functions to complete your task.
# Remove the keywords 'pass' and write your code in the functions.
# DO NOT change the functions definition or the docstring (except when asked in the question).

# === DO NOT IMPORT ANYTHING ELSE ===
import matplotlib.pyplot as plt
import numpy as np


class Food:
    """A food item. It simply has a tuple position."""

    def __init__(self, x: int, y: int) -> None:
        self.position = (x, y)


class Rodent:
    """The rodent. Loves to eat food.
    
    Attributes:
    position (list[int])       -- [row, column] position on the grid.
    distance (int)             -- The distance the rodent has travelled.
    eaten (int)                -- The number of foods the rodent has eaten.
    
    Methods:
    eat                        -- Eat a food item and update the 
                                  relevant attributes.                              
    """

    def __init__(self, x: int, y: int) -> None:
        self.position = (x, y)
        self.distance = 0
        self.eaten = 0


    def eat(self, food: Food, dist: int) -> None:
        """Eat a food item. Update the distance travelled, 
        change the position of the rodent to the food's position, and
        increment the number of food items eaten."""

        self.distance += dist
        self.position += food.position
        self.eaten += food 



class Grid:
    """The simulation grid.
    
    Attributes:
    food (list[Food])       -- A list of food objects.
    rodent (Rodent)         -- The rodent.
    size (int)              -- The size of the grid. 
                               Important for plotting.
    
    Methods:
    update                  -- Updates the state of the grid.
    """
    
    def __init__(self, rodent: Rodent, food=[], grid_size=6) -> None:
        self.food = food
        self.rodent = rodent
        self.size = grid_size


    def update(self) -> None:
        """Update the state of the grid. 
        Allow the rodent to eat the nearest food item.
        Remove from the list of foods the food item that was just consumed.
        """
        if not self.food: # aka. if nothing is in self.food [] then --> return; 
            return 
        
        food_nearby = None
        min_dist = int(100000) 

        for food in self.food:
            dist = abs(self.rodent.position[0] - food.position[0]) + abs(self.rodent.position[1] - food.position[1])

            if dist < min_dist: # 3 < 5 
                min_dist = dist # min_dist --> dist  = 5 --> 3
                food_nearby = food # x, y 

        if food_nearby:

            self.rodent.eat(food_nearby, min_dist)
            self.food.remove(food_nearby)
            


# A helper function provided to you for visualization.
def plot_steps(grid: Grid):
    """This function plots each update of the grid.
    Useful for debugging."""

    # Create a record of each step for plotting purposes
    history = []
    while len(grid.food) > 0:
        step = {
            'foods': [f.position for f in grid.food],
            'rodent_pos': grid.rodent.position,
            'rodent_dist': grid.rodent.distance,
            'rodent_eaten': grid.rodent.eaten
        }
        history.append(step)

        prev_len = len(grid.food)
        grid.update()
        post_len = len(grid.food)

        # This is logic to avoid infinite loop 
        # before actually completing the function bodies.
        if prev_len == post_len:
            break

    # Make sure the last step is included
    history.append({'foods': [f.position for f in grid.food],
                    'rodent_pos': grid.rodent.position,
                    'rodent_dist': grid.rodent.distance,
                    'rodent_eaten': grid.rodent.eaten
                    })

    # One subplot per step.
    # Visualize the food as a green cell and the rodent as a blue cell.
    fig, ax = plt.subplots(1, len(history))
    for i in range(len(history)):
        s = history[i]
        explicit_grid = np.zeros((grid.size, grid.size, 3))
        for f in s['foods']:
            explicit_grid[f] = 0, 1, 0
        explicit_grid[tuple(s['rodent_pos'])] = 0, 0, 1

        ax[i].imshow(explicit_grid)
        ax[i].axis('off')
        food_eaten, travelled = s['rodent_eaten'], s['rodent_dist']
        ax[i].set_title(f'Step {i}:\nFood eaten={food_eaten}\nTravelled={travelled}')

    plt.tight_layout()
    plt.show()


# Use this scope to test your function
# Anything written here will not be graded
# Feel free to modify as you wish
if __name__ == '__main__':
    f0, f1, f2 = Food(1, 2), Food(4, 4), Food(5, 2)
    rodent = Rodent(2, 4)
    grid = Grid(rodent, [f0, f1, f2])

    plot_steps(grid)
