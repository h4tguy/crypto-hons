def steps(a,g,o,m,n):
    baby_steps = []
    inv_g = g**(o) % n
    print("inv",inv_g)
    start_table()
    print("r & ${0}({1}^{{-1}})^{{r}} \mod {2}$ \\\\\\hline".format(a,g,n))
    for r in range(m):
        val = (a*(inv_g**r)) % n
        print("{0} & {1} \\\\\\hline".format(r, val))
        baby_steps.append(val)
    end_table()
    print()
    start_table()
    print("i & ${0}^{{ {1} i}} \mod {2}$ \\\\\\hline".format(g,m,n))
    q = 0
    giant_steps = [g**q]
    num_steps = 0

    print("{0} & {1} \\\\\\hline".format(num_steps, giant_steps[-1]))
    while giant_steps[-1] not in baby_steps and num_steps < n:
        q+=m
        val = g**q % n
        giant_steps.append(val)
        num_steps += 1
        print("{0} & {1} \\\\\\hline".format(num_steps, giant_steps[-1]))
    end_table()

def start_table():
    print("\\begin{tabular}{l l}")

def end_table():
    print("\\end{tabular}")

steps(52,16,24,4,101)
