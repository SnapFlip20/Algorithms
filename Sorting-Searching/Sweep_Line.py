# Sweeping Line in 1D

def sweep(line):
    line.sort()
    start, end = line[0]
    length = 0
    for i in range(1, len(line)):
        if line[i][0] <= end < line[i][1]:
            end = line[i][1]
        elif end < line[i][0]:
            length += end-start
            start, end = line[i]
    length += end-start

    return length