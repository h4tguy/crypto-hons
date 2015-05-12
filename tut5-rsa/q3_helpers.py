def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)

def pollardPMinusOne(base, n):
    print("\\item")
    print("\\begin{tabular}{l l l}")
    print("\\hline$j$ & ${0}^{{j!}} \\text{{ mod }} {1}$ & $\\text{{gcd}}({0}^{{j!}} - 1  \\text{{ mod }} {1}, {1})$ \\\\ \\hline".format(base, n))
    tot = 0
    factor = 1
    j = 2
    while factor == 1:
        exp = base**(fact(j)) % n
        factor = gcd(exp - 1, n)
        print("{0} & {1} & {2} \\\\ \\hline".format(j, exp, factor))
        j += 1
    print("\\end{tabular}")
    print("")

    if factor == n:
        print("Therefore the Pollar $p-1$ method fails to factorise {1} with a base of {0}.".format(base,n))
    else:
        print("Therefore {0} is a factor of {1}. This means ${1} = {0} \\times {2}$.".format(factor, n, n/factor))

    print("")

pollardPMinusOne(3, 323)
pollardPMinusOne(2, 323)

def order(n,p):
    for i in range(1,p):
        v = (n**i) % p
        if v==1:
            return i

def smallest_k(n,base,a,b):
    three_ord_a = order(base, a)
    three_ord_b = order(base, b)
    print("\\begin{tabular}{l l l}")
    print("\\hline k & $k! \\text{{ mod }} {0}$ & $k! \\text{{ mod }} {1}$ \\\\ \\hline".format(three_ord_a, three_ord_b))
    done_a = False
    done_b = False
    k = 2
    while not done_a or not done_b:
        v = fact(k)
        val_a, val_b = v % three_ord_a, v % three_ord_b
        if val_a == 0:
            done_a = True
        if val_b == 0:
            done_b = True
        print("{0} & {1} & {2} \\\\ \\hline".format(k, val_a, val_b))
        k+=1
    print("\\end{tabular}")

smallest_k(323, 3, 17, 19)
smallest_k(323, 2, 17, 19)
