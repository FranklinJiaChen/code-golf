"""
My idea is to put store the CSS colours in a fixed decision tree
data structure such that each level asks the same question.

It can be represented as a nested list which get's rid of the
keys in the dictionary. Saving golfing space.

Finding and storing will look like:
[[[...],],[...],[...]][question_1][question_2][question_...]

# this didn't work that well as the tree takes up a lot of space.

I did make a unique int key hashing function
"""
from collections import defaultdict

dict = {'IndianRed': '#cd5c5c', 'LightCoral': '#f08080', 'Salmon': '#fa8072', 'DarkSalmon': '#e9967a', 'LightSalmon': '#ffa07a', 'Red': '#ff0000', 'Crimson': '#dc143c', 'FireBrick': '#b22222', 'DarkRed': '#8b0000', 'Pink': '#ffc0cb', 'LightPink': '#ffb6c1', 'HotPink': '#ff69b4', 'DeepPink': '#ff1493', 'MediumVioletRed': '#c71585', 'PaleVioletRed': '#db7093', 'Coral': '#ff7f50', 'Tomato': '#ff6347', 'OrangeRed': '#ff4500', 'DarkOrange': '#ff8c00', 'Orange': '#ffa500', 'Gold': '#ffd700', 'Yellow': '#ffff00', 'LightYellow': '#ffffe0', 'LemonChiffon': '#fffacd', 'LightGoldenRodYellow': '#fafad2', 'PapayaWhip': '#ffefd5', 'Moccasin': '#ffe4b5', 'PeachPuff': '#ffdab9', 'PaleGoldenRod': '#eee8aa', 'Khaki': '#f0e68c', 'DarkKhaki': '#bdb76b', 'Lavender': '#e6e6fa', 'Thistle': '#d8bfd8', 'Plum': '#dda0dd', 'Violet': '#ee82ee', 'Orchid': '#da70d6', 'Fuchsia': '#ff00ff', 'Magenta': '#ff00ff', 'MediumOrchid': '#ba55d3', 'MediumPurple': '#9370db', 'BlueViolet': '#8a2be2', 'DarkViolet': '#9400d3', 'DarkOrchid': '#9932cc', 'DarkMagenta': '#8b008b', 'Purple': '#800080', 'Indigo': '#4b0082', 'DarkSlateBlue': '#483d8b', 'SlateBlue': '#6a5acd', 'MediumSlateBlue': '#7b68ee', 'RebeccaPurple': '#663399', 'GreenYellow': '#adff2f', 'Chartreuse': '#7fff00', 'LawnGreen': '#7cfc00', 'Lime': '#00ff00', 'LimeGreen': '#32cd32', 'PaleGreen': '#98fb98', 'LightGreen': '#90ee90', 'SpringGreen': '#00ff7f', 'MediumSpringGreen': '#00fa9a', 'MediumSeaGreen': '#3cb371', 'SeaGreen': '#2e8b57', 'ForestGreen': '#228b22', 'Green': '#008000', 'DarkGreen': '#006400', 'YellowGreen': '#9acd32', 'OliveDrab': '#6b8e23', 'Olive': '#808000', 'DarkOliveGreen': '#556b2f', 'MediumAquamarine': '#66cdaa', 'DarkSeaGreen': '#8fbc8f', 'LightSeaGreen': '#20b2aa', 'DarkCyan': '#008b8b', 'Teal': '#008080', 'Aqua': '#00ffff', 'Cyan': '#00ffff', 'LightCyan': '#e0ffff', 'PaleTurquoise': '#afeeee', 'Aquamarine': '#7fffd4', 'Turquoise': '#40e0d0', 'MediumTurquoise': '#48d1cc', 'DarkTurquoise': '#00ced1', 'CadetBlue': '#5f9ea0', 'SteelBlue': '#4682b4', 'LightSteelBlue': '#b0c4de', 'PowderBlue': '#b0e0e6', 'LightBlue': '#add8e6', 'SkyBlue': '#87ceeb', 'LightSkyBlue': '#87cefa', 'DeepSkyBlue': '#00bfff', 'DodgerBlue': '#1e90ff', 'CornflowerBlue': '#6495ed', 'RoyalBlue': '#4169e1', 'Blue': '#0000ff', 'MediumBlue': '#0000cd', 'DarkBlue': '#00008b', 'Navy': '#000080', 'MidnightBlue': '#191970', 'Cornsilk': '#fff8dc', 'BlanchedAlmond': '#ffebcd', 'Bisque': '#ffe4c4', 'NavajoWhite': '#ffdead', 'Wheat': '#f5deb3', 'Burlywood': '#deb887', 'Tan': '#d2b48c', 'RosyBrown': '#bc8f8f', 'SandyBrown': '#f4a460', 'GoldenRod': '#daa520', 'DarkGoldenRod': '#b8860b', 'Peru': '#cd853f', 'Chocolate': '#d2691e', 'SaddleBrown': '#8b4513', 'Sienna': '#a0522d', 'Brown': '#a52a2a', 'Maroon': '#800000', 'White': '#ffffff', 'Snow': '#fffafa', 'Honeydew': '#f0fff0', 'MintCream': '#f5fffa', 'Azure': '#f0ffff', 'AliceBlue': '#f0f8ff', 'GhostWhite': '#f8f8ff', 'WhiteSmoke': '#f5f5f5', 'SeaShell': '#fff5ee', 'Beige': '#f5f5dc', 'OldLace': '#fdf5e6', 'FloralWhite': '#fffaf0', 'Ivory': '#fffff0', 'AntiqueWhite': '#faebd7', 'Linen': '#faf0e6', 'LavenderBlush': '#fff0f5', 'MistyRose': '#ffe4e1', 'Gainsboro': '#dcdcdc', 'LightGrey': '#d3d3d3', 'Silver': '#c0c0c0', 'DarkGrey': '#a9a9a9', 'Grey': '#808080', 'DimGrey': '#696969', 'LightSlateGrey': '#778899', 'SlateGrey': '#708090', 'DarkSlateGrey': '#2f4f4f', 'Black': '#000000'}

colours = list(dict.keys())
# # judge decision questions and see how well the tree is balanced

# len_dicts = [defaultdict(int) for _ in range(17)]

# for i in range(2, 17):
#     for colour in colours:
#         len_dicts[i][len(colour) % i]+=1

# i = 0
# for d in len_dicts:
#     print(i)
#     sorted_keys = sorted(d.keys())  # Sort keys of the dictionary
#     for key in sorted_keys:
#         print(f'{key}: {d[key]}')
#     i += 1
#     print()

# first_char_mod_dicts = [defaultdict(int) for _ in range(27)]

# for i in range(2, 27):
#     for colour in colours:
#         first_char = colour[0]
#         hashed_value = ord(first_char) % i  # Calculate hash value using ASCII value
#         first_char_mod_dicts[i][hashed_value] += 1

# for d in first_char_mod_dicts:
#     sorted_keys = sorted(d.keys())  # Sort keys of the dictionary
#     for key in sorted_keys:
#         print(f'{key}: {d[key]}')
#     print()

# last_char_mod_dicts = [defaultdict(int) for _ in range(27)]

# for i in range(2, 27):
#     for colour in colours:
#         first_char = colour[-1]
#         hashed_value = ord(first_char) % i  # Calculate hash value using ASCII value
#         last_char_mod_dicts[i][hashed_value] += 1

# for d in last_char_mod_dicts:
#     sorted_keys = sorted(d.keys())  # Sort keys of the dictionary
#     for key in sorted_keys:
#         print(f'{key}: {d[key]}')
#     print()


combined_dict = defaultdict(int)

# Populate the combined dictionary based on combined criteria
# for i in range(2, 17):
#     for j in range(2, 27):
#         for k in range(2, 27):
i=10
j=16
k=11

((15*11+10)*10+9)*4+3

for colour in colours:
    length_mod = len(colour) % i
    first_char_mod = ord(colour[0]) % j
    last_char_mod = ord(colour[-1]) % k
    another_key = sum(1 for char in colour if char in "eS") % 4

    # key = (length_mod, first_char_mod, last_char_mod, another_key)
    key = (first_char_mod, last_char_mod, length_mod, another_key)
    combined_dict[key] += 1
    print(colour) if key == (9, 3, 5, 2) else None

# # collision detection
# collision = 0
# for key, value in combined_dict.items():
#     if value > 1:
#         collision += 1
#         print(f'{key}: {value}')
# print(collision)

# print dict sorted by key
def key_to_int(key):
    return ((key[0]*11+key[1])*10+key[2])*4+key[3]-39

def int_to_key(int):
    int+=39
    key3 = int % 4
    int-=key3
    int//=4
    key2 = int % 10
    int-=key2
    int//=10
    key1 = int % 11
    int-=key1
    int//=11
    key0 = int
    return (key0,key1,key2,key3)


hashed_dict = defaultdict(str)

for colour in colours:
    length_mod = len(colour) % i
    first_char_mod = ord(colour[0]) % j
    last_char_mod = ord(colour[-1]) % k
    another_key = sum(1 for char in colour if char in "eS") % 4

    # key = (length_mod, first_char_mod, last_char_mod, another_key)
    key = (first_char_mod, last_char_mod, length_mod, another_key)

    hashed_dict[key_to_int(key)] = colour

hashed_keys = sorted(hashed_dict.keys())  # Sort keys of the dictionary

l = [0] * 6999

for key in hashed_keys:
    l[key] = dict[hashed_dict[key]]

# print(l)


new_d = {
}

for key in hashed_keys:
    new_d[key] = dict[hashed_dict[key]]

print(new_d)
print(sum([len(str(key)) for key in new_d.keys()]))