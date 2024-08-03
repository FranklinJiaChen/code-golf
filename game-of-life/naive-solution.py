import sys
def game_of_life(input: str) -> None:
    """
    Takes in a 32x32 grid of cells, where each cell is either alive or dead.
    Alive = #
    Dead = .
    prints the next generation of the game of life.
    """
    input = input.replace("\n", "")
    output = ""
    for c in range(1024):
        is_alive = input[c]=="#"
        neighbors = 0
        if c-33 >= 0 and input[c-33]=="#":
            neighbors += 1
        if c-32 >= 0 and input[c-32]=="#":
            neighbors += 1
        if c-31 >= 0 and input[c-31]=="#":
            neighbors += 1
        if c-1 >= 0 and input[c-1]=="#":
            neighbors += 1
        if c+1 < 1024 and input[c+1]=="#":
            neighbors += 1
        if c+31 < 1024 and input[c+31]=="#":
            neighbors += 1
        if c+32 < 1024 and input[c+32]=="#":
            neighbors += 1
        if c+33 < 1024 and input[c+33]=="#":
            neighbors += 1
        if is_alive:
            if neighbors < 2 or neighbors > 3:
                output += "."
            else:
                output += "#"
        else:
            if neighbors == 3:
                output += "#"
            else:
                output += "."
        if (c+1)%32==0:
            output += "\n"
    print(output)
game_of_life(sys.argv[1])