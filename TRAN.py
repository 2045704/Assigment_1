def read_sequences(file):
    f = open(file)
    lines=f.readlines()
    lines[-1]+="\n"
    lines.append(">")
    f.close()
    seqs = []
    myseq = ""
    for i in lines[1:]:
        if i[0] == ">":
            seqs.append(myseq)
            myseq =""
        else:
            myseq+=i[:-1]
    return seqs


seqs = read_sequences (r"C:\Users\newma\Downloads\rosalind_tran (2).txt")
s1 = seqs[0]
s2 = seqs[1]

pur =["A","G"]
pyr =["C","T"]

nuc = {"A":"pur","G":"pur","C":"pyr","T":"pyr"}

transition = 0
transversion = 0

for i in range(0,len(s1)):
    n1=s1[i]
    n2=s2[i]    
    if n1 != n2:
        if nuc[n1]==nuc[n2]:
            transition += 1
        else: transversion += 1
        
a = transition/transversion
print(a)