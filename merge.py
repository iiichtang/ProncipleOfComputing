"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # replace with your code
    line2 = []
    line2.append(0)
    ptr = 0
    length_line = len(line)

    for length in range(length_line):

        if line[length] == 0:
            pass
        elif line2[ptr] == 0:
            line2[ptr] += line[length]
        elif line2[ptr] == line[length] :
            line2[ptr] += line[length]
            line2.append(0)
            ptr +=1
        else:
            line2.append(line[length])
            ptr += 1

    ptr +=1

    while ptr < length_line :
        line2.append(0)
        ptr +=1

    return line2