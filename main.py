import tkinter as tk
from writing_app import DisappearingTextWritingApp

def main():
    root = tk.Tk()
    app = DisappearingTextWritingApp(root, timeout_seconds=5)
    root.mainloop()

if __name__ == "__main__":
    main()