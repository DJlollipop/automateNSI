WHITE, BLACK = '\u25a1', '\u25a0'
N = 30

def population(s: str) -> list[int]:
    if len(s) == 0 or not '1' in s:
        return None
    
    l: list[int] = []

    for e in s:
        try:
            l.append(int(e))
        except:
            return None

    fillL, fillR = (N-len(s))/2, (N-len(s))/2 

    match len(s)%2:
        case 0: # pair
            fillR -= len(s)/2
            fillL -= len(s)/2

        case _: # impair
            fillR -= len(s)/2
            fillL -= len(s)/2






def rules(r: int) -> list[int]:
    try:
        binr: str = str(bin(r))
        binr = binr.replace("0b","")
    except:
        return None

    l: list[int] = [int(i) for i in binr]
    print(l)

    while len(l) != 8:
        l.insert(0, 0)

    print(l)
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


        