from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()
sense.low_light = True
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    sense.show_message(
        current_time, text_colour=red, back_colour=black, scroll_speed=0.2
    )
