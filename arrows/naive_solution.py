"""
Given a list of Unicode arrows, print the coordinates.
This got me last place in code golf.
"""

import sys

arrow_dict: dict ={
  "↙": [-1, -1],
  "↲": [-1, -1],
  "⇙": [-1, -1],
  "←": [-1, 0],
  "⇐": [-1, 0],
  "⇦": [-1, 0],
  "↖": [-1, 1],
  "↰": [-1, 1],
  "⇖": [-1, 1],
  "↓": [0, -1],
  "⇓": [0, -1],
  "⇩": [0, -1],
  "↔": [0, 0],
  "↕": [0, 0],
  "⇔": [0, 0],
  "⇕": [0, 0],
  "⥀": [0, 0],
  "⥁": [0, 0],
  "↑": [0, 1],
  "⇑": [0, 1],
  "⇧": [0, 1],
  "↘": [1, -1],
  "↳": [1, -1],
  "⇘": [1, -1],
  "→": [1, 0],
  "⇒": [1, 0],
  "⇨": [1, 0],
  "↗": [1, 1],
  "↱": [1, 1],
  "⇗": [1, 1]
}

x, y = 0, 0

def print_coordinates(x: int, y: int, direction: str) -> None:
    """
    Starting at [0, 0],
    print the result of applying
    the given Unicode arrow arguments.
    """
    x += arrow_dict[direction][0]
    y += arrow_dict[direction][1]
    print(x, y)
    return x, y

for arg in sys.argv[1:]:
    x, y = print_coordinates(x, y, arg)