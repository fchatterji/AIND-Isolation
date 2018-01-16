"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = game_agent.MinimaxPlayer()
        self.player2 = game_agent.MinimaxPlayer()
        self.game = isolation.Board(self.player1, self.player2)

    def test_game_agent(self):
        self.game.apply_move((2, 3))
        self.game.apply_move((0, 5))
        print(self.game.to_string())
        assert(self.player1 == self.game.active_player)
        print(self.game.get_legal_moves())

        new_game = self.game.forecast_move((1, 1))
        assert(new_game.to_string() != self.game.to_string())
        print("\nOld state:\n{}".format(self.game.to_string()))
        print("\nNew state:\n{}".format(new_game.to_string()))

        self.game.play()


if __name__ == '__main__':
    unittest.main()



