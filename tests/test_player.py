import unittest
from game.player import Player

class TestPlayer(unittest.TestCase):
    def test_player_creation(self):
        player = Player("TestPlayer")
        self.assertEqual(player.name, "TestPlayer")

if __name__ == "__main__":
    unittest.main()