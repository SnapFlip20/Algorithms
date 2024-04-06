# separate 0 and 1 in binary string

def sep01(s: str):
    # list of string 1
    return ' '.join(s.split('0')).split()

    # set(unique) of string 1
    return set(' '.join(s.split('0')).split())

    # the number
    return len(set(' '.join(s.split('0')).split()))