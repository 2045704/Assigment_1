def GC_COUNT(DNA):
    gc_count = 0
    total_bases = len(DNA)
    for base in DNA:
        if base == 'G' or base == 'C':
            gc_count +=1
    return (gc_count/total_bases)*100

with open(r"C:\Users\newma\Downloads\rosalind_gc.txt","r") as file:
    Rosalind_ID = ""
    DNA_String = ""
    Max_ID = ""
    Max_GC = 0
    for line in file:
        if line.startswith(">"):
            if Rosalind_ID != "":
                gc = GC_COUNT(DNA_String)
                if gc > Max_GC:
                    Max_GC = gc
                    Max_ID = Rosalind_ID
            Rosalind_ID = line[1:].strip()
            DNA_String = ""
        else:
            DNA_String += line.strip()
            
            
gc = GC_COUNT(DNA_String)
if gc > Max_GC:
    Max_GC = gc
    Max_ID = Rosalind_ID
    
print(Max_ID)
print(Max_GC)          


'''
Example = "TATAGCGCGCGC"
Plzwork = GC(Example)
print(Plzwork)'''