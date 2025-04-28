import tkinter as tk
class CountdownTimer:

    def __init__(self, root: tk.Misc, timeout_ms: int, on_timeout):
        self.root = root
        self.timeout_ms = timeout_ms
        self.on_timeout = on_timeout
        self._job = None
