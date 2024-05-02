# Sweeping Line in 1D

def sweep(line):
    line.sort()
    start, end = line[0]
    length = 0
    no_line = []
    if start != 0:
        no_line.append((0, start))
    
    for i in range(1, len(line)):
        if line[i][0] <= end < line[i][1]:
            end = line[i][1]
        elif end < line[i][0]:
            length += end-start
            no_line.append((end, line[i][0]))
            start, end = line[i]
    length += end-start

    return length
    #return no_line