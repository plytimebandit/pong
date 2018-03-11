# pong
Command line pong game. The plan is to play the game on a dot matrix controlled by a Raspberry Pi.

Start the game by executing `./Pong.py`.

The game is designed to be drawn on a 16x16 dot matrix controlled by a Raspberry Pi.
Well, up to now it's just the half finished command line game. You control the racket on the left and you play against yourself.
If the ball hits the left wall the fault gets indicated by flashing all LEDs but you can play forever. There are no lifes nor limits.

This is the incredible game design:
```
+----------------+
|                |
|                |
|                |
|                |
|                |
|          *     |
|*               |
|*               |
|*               |
|                |
|                |
|                |
|                |
|                |
|                |
|                |
+----------------+
```
