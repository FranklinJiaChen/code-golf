def list_to_bytes(lst):
    return bytes(lst)

# 32 to 126 are printable ASCII characters
# 39 and 92 requires escaping in strings and thus 2 bytes.
# all = [x for x in range(32, 127)]
lst = (-34, -33, -32, -1, 1, 32, 33, 34)
lst = [x+66 for x in lst]
byte_string = list_to_bytes(lst)
print(byte_string)
