# pong
LED matrix pong game for the Raspberry Pi.

Start the game by executing `./Pong.py`.

The game is designed to be drawn on a 16x16 dot matrix controlled by a Raspberry Pi.
You control the racket on the left by using tactile push switch and you play against yourself.
If the ball hits the left wall it's a fault and it gets indicated by flashing all LEDs but you can play forever. There are no lifes nor limits.

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

\
You can play the game also in bash without an LED matrix connected. Just run `./Pong_GUI.py` instead.

The implementation of the SPI interface is based on the implementation of Glenn K. Lockwood:
https://github.com/glennklockwood/raspberrypi/blob/master/spi/spi.py
