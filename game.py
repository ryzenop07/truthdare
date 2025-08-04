class TruthDareGame:
    def __init__(self):
        self.players = []
        self.current_index = 0
        self.started = False

    def add_player(self, username):
        if username not in self.players:
            self.players.append(username)
            return True
        return False

    def get_current_player(self):
        if not self.players:
            return None
        return self.players[self.current_index]

    def next_player(self):
        if not self.players:
            return None
        self.current_index = (self.current_index + 1) % len(self.players)
        return self.get_current_player()

    def reset(self):
        self.players = []
        self.current_index = 0
        self.started = False
