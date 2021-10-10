"""
Clone of 2048 game.
"""
import random
import poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def tide_list(lst):
    """
    this function sort the provided list and
    """
    tided_list = [num for num in lst if num > 0]
    if len(tided_list) < len(lst):
        result = len(lst) - len(tided_list)
        for idx in range(result):
            tided_list.append(idx * 0)
    return tided_list        
            
def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    
    tiles = tide_list(line)
    for idx in range(len(tiles) - 1):
        if tiles[idx] == tiles[idx + 1]:
            tiles[idx] = tiles[idx] * 2
            tiles[idx + 1] = 0
    tiles = tide_list(tiles)
    return tiles


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._height = grid_height
        self._width = grid_width
        self.reset() # intializing a new field called self._board that contains the initial grid
        
        self._init_tiles_up = [(0, col) for col in range(self._width)]
        self._init_tiles_down = [(self._height -1, col) for col in range(self._width)]
        self._init_tiles_right = [(row, self._width -1) for row in range(self._height)]
        self._init_tiles_left = [(row, 0) for row in range(self._height)]
        self._direction_dict = {UP:self._init_tiles_up, # refer to the initial row or column of a given direction 
                         DOWN:self._init_tiles_down,
                         LEFT:self._init_tiles_left,
                         RIGHT:self._init_tiles_right}

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._board = [[0 for dummy_col in range(self._width)]
                       for dummy_row in range(self._height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        for row in self._board:
            print row
        return ""

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        changed = False # Boolian to check if I should add a new tile to the grid after a move  
        merged_tiles = []
        
        if direction == UP or direction == DOWN:
            num_steps = range(self._height)
            direc = OFFSETS[direction]
            initial_tiles = list(self._direction_dict[direction])
        elif direction == LEFT or direction == RIGHT: 
            num_steps = range(self._width)
            direc = OFFSETS[direction]
            initial_tiles = list(self._direction_dict[direction])
        
        for tup in initial_tiles:
            new_board = []
            for step in num_steps:
                row = tup[0] + (step * direc[0])
                col = tup[1] + (step * direc[1])
                new_board.append(self.get_tile(row, col))
                
            merged_tiles = merge(new_board)
            if merged_tiles != new_board:
                changed = True
            for step in num_steps:
                row = tup[0] + (step * OFFSETS[direction][0])
                col = tup[1] + (step * OFFSETS[direction][1])
                self._board[row][col] = merged_tiles[step]
        if changed:
            self.new_tile()
            
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        zeros_in_board = [[row, col] for col in range(self._width) 
                          for row in range(self._height) if self._board[row][col] == 0]
        chance = [2, 2, 2, 2, 2, 2, 2, 2, 2, 4]
        random_tile = random.choice(zeros_in_board)
        self._board[random_tile[0]][random_tile[1]] = random.choice(chance)
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._board[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._board[row][col]

poc_2048_gui.run_gui(TwentyFortyEight(5, 5))