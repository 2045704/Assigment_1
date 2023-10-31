from Bio import SeqIO
from Bio.Seq import Seq

def matrix(sequences):
    n = len(sequences[0])

    profile = {'A':[0]*n,'C':[0]* n,'G':[0]* n,'T':[0]*n}
    for sequence in sequences:
        for k in range(n):
            char = sequence[k]
            profile[char][k] += 1
    return profile


def CONS(profile):
    cons = ""
    n = len(profile['A'])
    for i in range(n):
        MAX_quant = 0
        Max_freq_char = ""
        for char, counts in profile.items():
            if counts[i] > MAX_quant:
                MAX_quant = counts[i]
                Max_freq_char = char
        cons += Max_freq_char
    return cons

ex_data = r"C:\Users\newma\Downloads\rosalind_cons (7).txt"
sequences = [str(seq.seq) for seq in SeqIO.parse(ex_data, "fasta")]

A = matrix(sequences)
B = CONS(A)
print(B)
for a in "ACGT":
    print(f"{a}: {' '.join(map(str, A[a]))}")