"""
Gijswijt’s sequence is a slow-growing sequence where each term counts the maximum number of repeated blocks of numbers in the sequence immediately preceding that term.

The sequence begins 1, 1, 2, 1, 1, 2, 2, 2, 3, 1 ... and its construction can be seen in the following figure.

[1]
[1],[1]
 1 , 1 ,[2]
 1 , 1 , 2 ,[1]
 1 , 1 , 2 ,[1],[1]
[1 , 1 , 2],[1 , 1 , 2]
 1 , 1 , 2 , 1 , 1 ,[2],[2]
 1 , 1 , 2 , 1 , 1 ,[2],[2],[2]
 1 , 1 , 2 , 1 , 1 , 2 , 2 , 2 ,[3]
 1 , 1 , 2 , 1 , 1 , 2 , 2 , 2 , 3 , 1
On each line, the blocks that are used to get the next number in the sequence are marked in []. Print the first 1,000 terms of Gijswijt’s sequence, each on a separate line.
"""
sequence = '1'
length = len(sequence)

while length < 1000:
    try_to_find_number = 2
    for sublength in range(1, length):
        substring = sequence[-sublength:]
        while sublength*try_to_find_number<length+1 and sequence.endswith(substring*try_to_find_number):
            try_to_find_number += 1
    sequence += str(try_to_find_number-1)
    length = len(sequence)
for c in sequence:
    print(c)