"""
Draw a size ascending range of Christmas trees using asterisks, ranging from size 3 to size 9, each tree separated by a blank line.

A size 3 tree should look like this, with a single centered asterisk for the trunk:

   *
  ***
 *****
   *
With the largest size 9 tree looking like this:

         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
         *
"""

for size in range(3, 10):
    for i in range(1, size + 1):
        print(" " * (size - i + 1) + "*" * (2 * i - 1))
    print(" " * size + "*")
    print()