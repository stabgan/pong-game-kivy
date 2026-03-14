# 🏓 Pong Game

A classic Pong game built with Kivy — a cross-platform Python framework for building multi-touch applications. Two players control paddles on opposite sides of the screen, bouncing a ball back and forth to score points.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| 🐍 Python 3 | Core language |
| 📱 Kivy | UI framework & game rendering |
| 🎨 Kivy Language (.kv) | Declarative UI layout |

## 📦 Dependencies

- Python 3.7+
- Kivy 2.0+

Install dependencies:

```bash
pip install kivy
```

## 🚀 How to Run

```bash
cd pong
python PongApp.py
```

### Controls

- **Player 1 (left paddle):** Touch/drag on the left third of the screen
- **Player 2 (right paddle):** Touch/drag on the right third of the screen

## ⚠️ Known Issues

- No win condition — the game runs indefinitely and scores keep incrementing.
- Ball speed increases on every paddle bounce with no upper cap, which can make the ball uncontrollable after extended rallies.
- No keyboard input support — controls are touch/mouse-drag only.
- No sound effects or visual feedback on scoring.
