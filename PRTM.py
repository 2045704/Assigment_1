Mono_mass_dict = {'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259, 'F': 147.06841, 'G': 57.02146, 'H': 137.05891, 'I': 113.08406, 'K': 128.09496, 'L': 113.08406, 'M': 131.04049, 'N': 114.04293, 'P': 97.05276, 'Q': 128.05858, 'R': 156.10111, 'S': 87.03203, 'T': 101.04768, 'V': 99.06841, 'W': 186.07931, 'Y': 163.06333}
def PRTM(protein):
    mass_tot = 0.0
    for amminoacid in protein:
        if amminoacid in Mono_mass_dict:
            mass_tot += Mono_mass_dict[amminoacid]
    mass_tot = round(mass_tot,3)
    return mass_tot
    
with open(r"C:\Users\newma\Downloads\rosalind_prtm (1).txt",'r') as file:
    protein = file.readline()
    result = PRTM(protein)
    print(result)