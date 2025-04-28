import tkinter as tk

class DisappearingTextWritingApp:
    def __init__(self, root: tk.Tk, timeout_seconds: float = 5.0) -> None:
        self.root = root
        self.root.title("Disappearing Text Writer")
        self.text = tk.Text(master=self.root, wrap='word', font=('Consolas', 12))
        self.text.pack(expand=True, fill='both', padx=10, pady=10)
        self.timeout_ms = int(timeout_seconds * 1000)
        self.char_counter = 0
        self.text.bind(sequence="<KeyRelease>", func=self._on_key_release)

    def _on_key_release(self, event: tk.Event) -> None:
        char = event.char
        if not char or len(char) != 1 or (char.isspace() and char != ' '):
            return
        char_index = self.text.index("insert-1c")
        tag_name = f"char{self.char_counter}"
        self.char_counter += 1
        self.text.tag_add(tag_name, char_index, f"{char_index}+1c")
        self.root.after(self.timeout_ms, lambda tag=tag_name: self._remove_char(tag))

    def _remove_char(self, tag: str) -> None:
        ranges = self.text.tag_ranges(tag)
        if ranges:
            start, end = ranges
            self.text.delete(start, end)
        self.text.tag_delete(tag)
