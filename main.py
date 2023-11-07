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

    fillL, fillR = ((N+2)-(len(s)/2))/2, ((N+2)-(len(s)/2))/2 

    match len(s)%2:
        case 0: # pair
            l = [0 for _ in range(fillL)] + l
            l += [0 for _ in range(fillR)]

        case _: # impair
            l = [0 for _ in range(fillL)] + l
            l += [0 for _ in range(fillR)]

assert population("1") == [0 for _ in range(15)] + [1] + [0 for _ in range(16)]






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
    l : list[int] = [0,]
    for i in range(len(pop-2)):
        A : bool =  