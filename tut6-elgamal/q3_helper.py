def f(u, g, a, m, b_1, b_2):
    if u <= b_1:
        return (g*u % m, 1)
    if u <= b_2:
        return (u**2 % m, 2)
    return (a*u % m, 3)

def exponents(b,c,m, set_num):
    if set_num == 1:
        b = (b + 1) % m
    if set_num == 2:
        b = (2*b) % m
        c = (2*c) % m
    if set_num == 3:
        c = (c+1) % m
    return (b,c)

def rho(g,a,m,b,b_1,b_2):
    print("\\begin{tabular}{l l l l}")
    print("i & $u_i \mod {0}$ & $b_i$ & $c_i$ \\\\\\hline".format(m))
    u = [g**b % m]
    c = 0
    i = 1
    print_row(i,u[0],b,c)
    i+=1
    done = False
    while not done:
        val, set_num = f(u[-1], g,a,m,b_1,b_2)
        b,c = exponents(b,c,m-1,set_num)
        print_row(i, val, b, c)
        u.append(val)
        if len(u) % 2==0:
            if u[-1] == u[(len(u)-1)//2]:
                done = True
        i += 1
    print("\\end{tabular}")
    return u


def print_row(i,u,b,c):
    print("{0} & {1} & {2} & {3} \\\\\\hline".format(i,u,b,c))

rho(2,58,83,27,55,33)
