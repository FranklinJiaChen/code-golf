"""
Draw 7 cubes in increasing size using "╱" (U+2571) for the diagonal edges, "│" (U+2502) for the vertical edges, "─" (U+2500) for the horizontal edges, and "█" (U+2588) for the vertices. The cubes should range from size 1 to size 7 with a blank line between each cube. A size 1 cube should look like:

  █────█
 ╱    ╱│
█────█ │
│    │ █
│    │╱
█────█
And a size 7 cube should look like:

        █────────────────────────────█
       ╱                            ╱│
      ╱                            ╱ │
     ╱                            ╱  │
    ╱                            ╱   │
   ╱                            ╱    │
  ╱                            ╱     │
 ╱                            ╱      │
█────────────────────────────█       │
│                            │       │
│                            │       │
│                            │       │
│                            │       │
│                            │       │
│                            │       │
│                            │       █
│                            │      ╱
│                            │     ╱
│                            │    ╱
│                            │   ╱
│                            │  ╱
│                            │ ╱
│                            │╱
█────────────────────────────█
"""

def draw_cube(size, vertex="█", side="─", vertical="│", diagonal="╱"):
    """
    Draw a cube of the given size using the
    given characters for the vertices, sides, vertical edges,
    and diagonal edges.
    """
    # Draw the topmost vertices
    print(" " * (size + 1) + vertex + side * (size * 4) + vertex)
    # Draw the top edges
    for i in range(size):
        print(" " * (size-i) + diagonal + " " * (size * 4) + diagonal + " " * i + vertical)
    # Draw the topfront vertices
    print(vertex + side * (size * 4) + vertex + (" " * size) + vertical)

    # Draw the middle edges
    for _ in range(size-1):
        print(vertical + " " * (size * 4) + vertical + " " * size + vertical)

    # Draw the bottomback vertex
    print(vertical + " " * (size * 4) + vertical + " " * size + vertex)

    # Draw the bottom edges
    for i in range(size):
        print(vertical + " " * (size * 4) + vertical + " " * (size-i-1) + diagonal)

    # Draw the bottommost vertices
    print(vertex + side * (size * 4) + vertex)

for i in range(1, 8):
    draw_cube(i)
    print()