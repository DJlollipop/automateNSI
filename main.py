WHITE, BLACK = '\u25a1', '\u25a0'
N = 30

final: list[list[int]] = [] # final 2d vector

def population(s: str) -> list[int]:
    if len(s) == 0 or not '1' in s:
        return None
    
    if len(s)>30:
        return [0] + s[:30] + [0]
    
    l: list[int] = []

    for e in s:
        try:
            l.append(int(e))
        except Exception as e:
            print(e)
            return None

    fill: int = int(
        (
            N+2 - len(s)
        )/2 
    )

    if len(s)%2 == 0: # pair
            l = [0 for _ in range(fill)] + l
            l += [0 for _ in range(fill)]

    else: # impair
            l = [0 for _ in range(fill-1)] + l
            l += [0 for _ in range(fill)]

    return [0] + l[:30] + [0]

assert population("1") == [0 for _ in range(15)] + [1] + [0 for _ in range(16)]
assert population("101") == [0 for _ in range(14)] + [1, 0, 1] + [0 for _ in range(15)]
assert len(population("1")) == 32
assert len(population("1001001")) == 32
assert population("0") == None

def rules(r: int) -> list[int]:
    try:
        binr: str = str(bin(r))
        binr = binr.replace("0b","")
    except:
        return None

    l: list[int] = [int(i) for i in binr]

    while len(l) != 8:
        l.insert(0, 0)

    return l 


def evolve(pop,rules):
    l = []
    for i in range(1,len(pop)-1):
        A : bool = pop[i-1] == 1
        B : bool = pop[i] == 1
        C : bool = pop[i+1] == 1
        if not A and not B and not C:
            l.append(rules[7]) 
        if not A and not B and C:
            l.append(rules[6]) 
        if not A and B and not C:
            l.append(rules[5]) 
        if not A and B and C:
            l.append(rules[4]) 
        if A and not B and not C:
            l.append(rules[3]) 
        if A and not B and C:
            l.append(rules[2]) 
        if A and B and not C:
            l.append(rules[1]) 
        if A and B and C:
            l.append(rules[0])
    l.insert(0,0)
    l.append(0)
    return l


def printevolve(genesis: list[int], rule: int, nbgen: int) -> None:
    old = genesis

    def printv2():
        s=""
        for i, x in enumerate(old):
            if i == 0 or i == len(old)-1:
                continue
            if x == 0:
                s+=BLACK
            else:
                s+=WHITE
        print(s)

    printv2()
    
    for _ in range(nbgen):
        chain = evolve(old, rules(rule))

        old = chain
        printv2()

printevolve(population("1"), 255, 10)