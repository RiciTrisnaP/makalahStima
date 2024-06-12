from Toolkit import *
from utilities import *
from stringMatching import *

DNASequence = "ATGGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGGTCTGTTCCAAGGGCCTTTGCGTCAGGTGGGCTCAGGATTCCAGGGTGGCTGGACCCCAGGCCCCAGCTCTGCAGCAGTGA"

intron1 = "CCCAGGC"
intron2 = "CAGAAGA"

transcriptionResult = transcription(DNASequence)
indexIntron1 = KMP_search(DNASequence, intron1)
Splicing_Result = remove_substring(transcriptionResult,indexIntron1, indexIntron1+len(intron1))
indexIntron2 = KMP_search(Splicing_Result, intron2)
Splicing_Result = remove_substring(Splicing_Result,indexIntron2, indexIntron2+len(intron2))


print(f'\nSequence : {colorized(DNASequence)}\n')
print(f'[1] Sequence Length : {len(DNASequence)}\n')
print(colorized(f'[2] Nucleotide Frequency: {countNucFrequency(DNASequence)}\n'))
print(f'[3] DNA: \n 5\' {colorized(DNASequence)} 3\' Coding Strand')
print(f'    {''.join(['|' for i in range(len(DNASequence))])}')
print(f' 3\' {colorized(reverse_complement(DNASequence)[::-1])} 5\' Template Strand')
print(f'\n[4] Transcription Result:\n 5\' {colorized(transcriptionResult)} 3\'\n')
print(f'Intron 1 : {colorized(intron1)}')
print(f'Intron 2 : {colorized(intron2)}')
print(f'\n[5] RNA Splicing Result \n 5\' {colorized(Splicing_Result)} 3\'\n')
print( ' '.join(translate_sequence(Splicing_Result)))
