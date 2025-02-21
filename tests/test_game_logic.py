import unittest
from game.game_logic import get_winner

class TestGameLogic(unittest.TestCase):
    def test_get_winner(self):
        self.assertEqual(get_winner("rock", "scissors"), "player")
        self.assertEqual(get_winner("scissors", "rock"), "computer")
        self.assertEqual(get_winner("paper", "rock"), "player")
        self.assertEqual(get_winner("rock", "paper"), "computer")
        self.assertEqual(get_winner("scissors", "paper"), "player")
        self.assertEqual(get_winner("paper", "scissors"), "computer")
        self.assertEqual(get_winner("rock", "rock"), "draw")
        self.assertEqual(get_winner("paper", "paper"), "draw")
        self.assertEqual(get_winner("scissors", "scissors"), "draw")

if __name__ == "__main__":
    unittest.main()