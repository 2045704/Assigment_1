def rab(n,k):
    if n==1 or n==2:
        return 1
    else:
        rab_pairs = [1,1]
        for i in range(2,n):
            reproduction = rab_pairs[-1] + k*rab_pairs[-2]
            rab_pairs.append(reproduction)
            
        return rab_pairs[-1]



example = rab(36,2)
print(example)