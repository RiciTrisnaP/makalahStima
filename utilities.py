def colorized(sequence):
    bgcolor = {
        'A' : '\033[92m',
        'C' : '\033[94m',
        'G' : '\033[93m',
        'T' : '\033[91m',
        'U' : '\033[91m',
        'reset' : '\033[0;0m',
    }

    temp = ""

    for nucleotide in sequence:
        if nucleotide in bgcolor:
            temp += bgcolor[nucleotide] + nucleotide
        else:
            temp += bgcolor['reset'] + nucleotide

    return temp + '\033[0;0m'

def remove_substring(string, start, end):
    before = string[:start]
    after = string[end:]
    result = before + after
    return result
