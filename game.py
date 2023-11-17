class Game():

    def __init__(self, board, player1, player2, started_at, finished_at):
        """
            board: the playing board for the game,
            player1: first player in game,
            player2: second player in game,
            started_at: when the game started,
            finished_at: when the game ended
        """

        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.started_at = started_at
        self.finished_at = finished_at