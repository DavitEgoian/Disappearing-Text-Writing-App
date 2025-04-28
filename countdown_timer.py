import tkinter as tk
class CountdownTimer:
    def __init__(self, root: tk.Misc, timeout_ms: int, on_timeout):
        self.root = root
        self.timeout_ms = timeout_ms
        self.on_timeout = on_timeout
        self._job = None

    def reset(self):
        if self._job:
            self.root.after_cancel(self._job)
        self._job = self.root.after(self.timeout_ms, self._timeout)

    def _timeout(self):
        self._job = None
        self.on_timeout()

    def cancel(self):
        if self._job:
            self.root.after_cancel(self._job)
            self._job = None