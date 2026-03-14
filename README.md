# 🏓 Pong — Kivy

A classic two-player Pong game built with the Kivy framework, following (and extending) the official Kivy tutorial.

## What It Does

Two paddles, one ball, first to outscore your opponent wins. Each player drags their paddle on their side of the screen; the ball speeds up on every paddle hit and gains a slight angle based on where it strikes the paddle.

## How It Works

| Component | Role |
|-----------|------|
| `PongBall` | Moves each frame by its velocity vector |
| `PongPaddle` | Detects collision, reflects the ball with a 1.1× speed-up and vertical offset |
| `PongGame` | Orchestrates the game loop at 60 FPS via `Clock.schedule_interval` |
| `pong.kv` | Declares the widget tree, sizes, and score labels |

The ball is served from the centre with a random vertical component and random left/right direction so every rally starts differently.

## 🛠 Tech Stack

| | Technology | Purpose |
|---|-----------|---------|
| 🐍 | Python 3 | Game logic |
| 🖼️ | Kivy ≥ 1.10 | Cross-platform GUI / game framework |

## Getting Started

```bash
pip install kivy
cd pong
python PongApp.py
```

Drag the left third of the screen to move the left paddle; drag the right third to move the right paddle.

## ⚠️ Known Issues

- No win condition — the score counts up forever.
- Ball speed increases indefinitely after many paddle hits.
- No sound effects or visual polish beyond the tutorial defaults.
