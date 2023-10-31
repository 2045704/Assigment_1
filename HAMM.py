def HAMM(DNA1,DNA2):
    hamm = 0
    for base in range(len(DNA1)):
        if DNA1[base] != DNA2[base]:
            hamm +=1
    return hamm
            
'''A = "GAGCCTACTAACGGGAT"
B = "CATCGTAATGACGGCCT"

result = HAMM(A,B)
print(result)
'''

with open(r"C:\Users\newma\Downloads\rosalind_hamm.txt","r") as file:
    lines = file.readlines()
    s = lines[0].strip()
    t = lines[1].strip()
    if len(s) != len(t):
        print("NOPE")
    else:
        hamm_dist = HAMM(s,t)
        print(hamm_dist)