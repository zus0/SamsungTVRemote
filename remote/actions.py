import time

class Actions:
    def __init__(self, remote):
        self.remote = remote
        self.shortcuts = remote.shortcuts()

    def hdmi(self, n):
        if not isinstance(n, int):
            try: n = int(n)
            except: return
        self.shortcuts.source()
        self.shortcuts.source()
        for _ in range(3):
            self.shortcuts.left()
        for _ in range(n):
            self.shortcuts.right()
        self.shortcuts.enter()
    
    def pic_mode(self, mode):
        mode = 1 if mode == "dark" else 2 if self.remote.is_in_app() else 0
        self.shortcuts.menu()
        self.shortcuts.right(0.5)
        self.shortcuts.enter()
        for _ in range(3):
            self.shortcuts.up()
        for _ in range(mode):
            self.shortcuts.down()
        self.shortcuts.enter(1.5)
        self.shortcuts.back(0.5)
        self.shortcuts.back(0.5)
        self.shortcuts.back()