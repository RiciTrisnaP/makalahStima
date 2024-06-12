Nucleotides = ["A", "C", "G", "T"]

DNA_Reverse_Complement = {'A' : 'T', 'T' : 'A', 'C' : 'G', 'G' : 'C'}

RNA_Codons = {
    # 'M' - START, '_' - STOP
    "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
    "UGU": "Cys", "UGC": "Cys",
    "GAU": "Asp", "GAC": "Asp",
    "GAA": "Glu", "GAG": "Glu",
    "UUU": "Phe", "UUC": "Phe",
    "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly",
    "CAU": "His", "CAC": "His",
    "AUA": "Ile", "AUU": "Ile", "AUC": "Ile",
    "AAA": "Lys", "AAG": "Lys",
    "UUA": "Leu", "UUG": "Leu", "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
    "AUG": "Met",
    "AAU": "Asn", "AAC": "Asn",
    "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
    "CAA": "Gln", "CAG": "Gln",
    "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg", "AGA": "Arg", "AGG": "Arg",
    "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser", "AGU": "Ser", "AGC": "Ser",
    "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
    "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
    "UGG": "Trp",
    "UAU": "Tyr", "UAC": "Tyr",
    "UAA": "_", "UAG": "_", "UGA": "_"
}
