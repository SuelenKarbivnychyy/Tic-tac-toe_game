"""
    Define a move by player
"""


class Move():

    def __init__(self, position_x, position_y, author):
        """
            author: who made the move,
            position: where the move is placed on the board
        """

        self.position_x = position_x
        self.position_y = position_y
        self.author = author