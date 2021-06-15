import time

class Actions: #TODO more actions
    def __init__(self, remote):
        self.remote = remote
        self.shortcuts = remote.shortcuts()

    def hdmi(self, n):
        self.shortcuts.source()
        self.shortcuts.source()

        for _ in range(3):
            self.shortcuts.left()
        for _ in range(n):
            self.shortcuts.right()
        
        self.shortcuts.enter()