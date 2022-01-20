"""Custom badge example for Adafruit CLUE."""
from adafruit_pybadger import pybadger

pybadger.badge_background(
    background_color=pybadger.YELLOW,
    rectangle_color=pybadger.BLACK,
    rectangle_drop=0.2,
    rectangle_height=0.6,
)

pybadger.badge_line(
    text="@MidNightCookies", color=pybadger.DEEP_PURPLE, scale=2, padding_above=2
)
pybadger.badge_line(text="John", color=pybadger.RED, scale=5, padding_above=3)
pybadger.badge_line(
    text="Johnathon M. Cook", color=pybadger.GREEN, scale=2, padding_above=2
)
pybadger.badge_line(
    text="Software Engineer", color=pybadger.RED, scale=2, padding_above=4
)

pybadger.show_custom_badge()

while True:

    # BACK LED
    pybadger.pixels.fill(pybadger.JADE)

    # BUTTONS
    if pybadger.button.a:
        pybadger.show_qr_code("https://circuitpython.org")

    if pybadger.button.b:
        pybadger.show_custom_badge()