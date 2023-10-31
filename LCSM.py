def r_seq(file):
    with open(file,'r') as f:
        lines = f.readlines()
    
    titles = {}
    current_title = None
    for line in lines:
        line = line.strip()
        if line.startswith(">"):
            current_title = line
            titles[current_title] = ""
        else:
            titles[current_title] += line.replace( "X", "A")
            
    return list(titles.values())

def LCSM(sequence):
    seq = r_seq(sequence)
    smallest_seq = min(seq, key=len)
    for i in range(len(smallest_seq), 0, -1):  # Fix the loop range for 'i'
        for j in range(len(smallest_seq) - i + 1):  # Fix the loop range for 'j'
            common_seq = smallest_seq[j:j + i]
            if all(common_seq in s for s in seq):  # Change 's' to 'seq' for consistency
                return common_seq


f = r"C:\Users\newma\Downloads\rosalind_lcsm (1).txt"
A = LCSM(f)
print(A)