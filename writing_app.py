import tkinter as tk
from countdown_timer import CountdownTimer

class DisappearingTextWritingApp:
    def __init__(self, root: tk.Tk, timeout_seconds: float = 5.0):

        self.root = root
        root.title("Disappearing Text Writer")

        self.text = tk.Text(root, wrap='word', font=('Consolas', 12))
        self.text.pack(expand=True, fill='both', padx=10, pady=10)

        ms = int(timeout_seconds * 1000)
        self.timer = CountdownTimer(root, ms, self.clear_text)

        self.text.bind("<KeyRelease>", lambda e: self.timer.reset())

        self.timer.reset()

    def clear_text(self):
        self.text.delete('1.0', tk.END)