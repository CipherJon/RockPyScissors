import unittest
from game.game_logic import determine_winner

class TestGameLogic(unittest.TestCase):
    def test_tie(self):
        self.assertEqual(determine_winner('rock', 'rock'), 'tie')
        self.assertEqual(determine_winner('paper', 'paper'), 'tie')
        self.assertEqual(determine_winner('scissors', 'scissors'), 'tie')
    
    def test_win(self):
        self.assertEqual(determine_winner('rock', 'scissors'), 'win')
        self.assertEqual(determine_winner('paper', 'rock'), 'win')
        self.assertEqual(determine_winner('scissors', 'paper'), 'win')
    
    def test_lose(self):
        self.assertEqual(determine_winner('rock', 'paper'), 'lose')
        self.assertEqual(determine_winner('paper', 'scissors'), 'lose')
        self.assertEqual(determine_winner('scissors', 'rock'), 'lose')

if __name__ == '__main__':
    unittest.main()