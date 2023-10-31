'''#Can I like get the genes as a single string and mix them up to get probability?
K_gen = "AA"
M_gen = "Aa"
N_gen = "aa"'''

#FIXED PARENTHESIS BUT RESULT SHOULD BE 0.78333
def IPRB(k,m,n):
    tot = k + m + n
    #probability of AA x AA / for all the ones where GENOTIPE IS THE SAME DO -1 
    P1 = (k/tot)*((k-1)/(tot-1))
    #prob of AA x Aa / Aa x AA
    P2 = (k/tot)*(m/(tot-1))
    #prob of AA x aa 
    P3 = (k/tot)*(n/(tot-1))
    #prob of Aa x Aa /// but not all offspring is dom so times 3/4 
    P4 = (m/tot)*((m-1)/(tot-1))*(3/4)
    #prob of Aa x aa /// half the offspring is dominant
    P5 = (m/tot)*(n/(tot-1))*0.5
    #Aa x AA
    P6 = (m/tot)*(k/(tot-1))
    #aa x AA
    P7 = (n/tot)*(k/(tot-1))
    #aa x aA
    P8 = (n/tot)*(m/(tot-1))*0.5
    #aa x aa is not needed bc offspring will be all recessive
    Prob_dominance = P1 + P2 + P3 + P4 + P5 + P6 + P7 + P8
    return Prob_dominance

ex = IPRB(29,26,17)
print(ex)