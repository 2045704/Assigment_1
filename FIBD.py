def FIBD(m,n):
    generation = [0] * n
    generation[0] = 1
        
    for rabbit in range(m-1):
        new_gen = 0
        for i in range(n-1,0,-1):
            new_gen += generation[i]
            generation[i] = generation[i-1]
        generation[0] = new_gen
    return sum(generation)

A = FIBD(94,20)
print(A)