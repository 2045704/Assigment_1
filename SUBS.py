def SUBS(s,t):
    positions = []
    for base in range(len(s)):
        if s[base:base+len(t)] == t:
            positions.append(str(base+1))
    new_pos = ' '.join(positions) 
    return new_pos


with open(r'C:\Users\newma\Downloads\rosalind_subs (1).txt','r') as file:
    A = file.readline().strip()
    B = file.readline().strip()
    subs = SUBS(A,B)
    print(subs)