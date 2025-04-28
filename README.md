# Disappearing Text Writing App
An online writing app where if you stop typing, your work will disappear.

## 📝 Project Overview
Inspired by “The Most Dangerous Writing App,” this tool challenges writers to maintain a steady flow. After each keystroke, a countdown begins—stop typing for more than the timeout (default 5 seconds), and all text is erased.

## 🚀 Features

- **Disappearing Text**: Every character is scheduled for deletion unless new input resets the timer.
- **Customizable Timeout**: Default inactivity window is 5 seconds; easily adjustable in the constructor.
- **Simple, Focused UI**: Clean full-window text editor powered by Tkinter.
- **Lightweight & Self‑Contained**: No external dependencies beyond the Python standard library.

## 💻 Installation & Usage

1. **Clone or download** this repository.  
2. Ensure you have **Python 3.6+** installed (Tkinter comes bundled on most systems).  
3. Run the app:  
   ```bash
   python main.py
   ```
4. Start typing—keep the words flowing or watch them disappear!

## 📂 Project Structure

```
Disappearing-Text-Writing-App/
├── countdown_timer.py         # Timer utility for scheduling deletions
├── DisappearingTextWritingApp.py  # Core app: binds keystrokes and handles auto‑deletion
└── main.py                    # Entry point: launches the Tkinter window
```

## ⚙️ Customization

- **Timeout Duration**: Change the `timeout_seconds` parameter when instantiating the app in `main.py`.  
- **Font & Styling**: Modify the `font` and widget options in `DisappearingTextWritingApp.__init__`.  
- **Key Events**: Extend or modify the `KeyRelease` binding to filter which keystrokes trigger deletions.

---

