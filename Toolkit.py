from definitions import RNA_Codons
def countNucFrequency(sequence):
    FrequencyDictionary = {"A" : 0, "C": 0, "G": 0, "T": 0}
    for nucleotide in sequence:
        FrequencyDictionary[nucleotide] += 1
    return FrequencyDictionary

def transcription(sequence):
    return sequence.replace("T","U")

def reverse_complement(sequence):
    mapping = str.maketrans('ATCG', 'TAGC')
    return sequence.translate(mapping)[::-1]

def translate_sequence(sequence, init_pos=0):
    return [RNA_Codons[sequence[pos:pos+3]] for pos in range(init_pos, len(sequence) -2 , 3)]