class Player:
    def __init__(self, name):
        self.name = name

    def get_choice(self):
        return input(f"{self.name}, enter your choice (rock, paper, scissors): ").lower()