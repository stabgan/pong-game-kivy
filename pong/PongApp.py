import random

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty,
    ReferenceListProperty,
    ObjectProperty,
)
from kivy.vector import Vector
from kivy.clock import Clock


class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            speedup = 1.1
            offset = 0.02 * Vector(0, ball.center_y - self.center_y)
            ball.velocity = speedup * (offset - Vector(*ball.velocity))


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def serve_ball(self, vel=None):
        """Reset ball to centre and launch with a random-ish velocity."""
        self.ball.center = self.center
        if vel is None:
            direction = random.choice([-1, 1])
            vel = (direction * 4, random.uniform(-3, 3))
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move()

        # bounce ball off top / bottom
        if self.ball.y < 0 or self.ball.top > self.height:
            self.ball.velocity_y *= -1

        # scored past the left edge → point for player 2
        if self.ball.right < self.x:
            self.player2.score += 1
            self.serve_ball()

        # scored past the right edge → point for player 1
        if self.ball.x > self.width:
            self.player1.score += 1
            self.serve_ball()

        # bounce off paddles (checked after boundary so a reset
        # doesn't immediately collide with a paddle)
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y


class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == "__main__":
    PongApp().run()
