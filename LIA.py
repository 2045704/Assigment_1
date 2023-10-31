import math
def com_fun(n,r):
    f = math.factorial
    return f(n)/f(r)/f(n-r)

def LIA(k,n):
    prob_het = 4/16
    prob = []
    total = 2**k
    for i in range(n,(total+1)):
        prob.append(com_fun(total,i)*(prob_het**i)*((1-prob_het)**(total-i)))
    return sum(prob)
    
A = LIA(5,9)
print(A)