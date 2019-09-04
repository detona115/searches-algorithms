import sys

def str2son(s):
    return [s[0],s[1],s[2]]
def son2str(s):
    return ''.join([str(v) for v in s])

def valid(s):
    r = True
    if s[0] < 0: r = False
    if s[0] > 3: r = False
    if s[1] < 0: r = False
    if s[1] > 3: r = False
    if s[0] < s[1] and s[0] != 0 and s[1] != 0: r = False
    return r
    
def complement(s):
    return [3-s[0],3-s[1],s[2]]

def sons(s):
    r = []
    if (s[2] == 1):
        v = 1
    else:
        v = -1
    #leva 1 missionario
    state = [s[0]-v,s[1],1-s[2]]
    if valid(state) and valid(complement(state)):
        r.append(state)
    #leva 2 missionarios
    state = [s[0]-2*v,s[1],1-s[2]]
    if valid(state) and valid(complement(state)):
        r.append(state)

    #leva 1 canibal
    state = [s[0],s[1]-1*v,1-s[2]]
    if valid(state) and valid(complement(state)):
        r.append(state)

    #leva 2 canibais
    state = [s[0],s[1]-2*v,1-s[2]]
    if valid(state) and valid(complement(state)):
        r.append(state)

    #leva 1 missionario 1 canibal
    state = [s[0]-1*v,s[1]-1*v,1-s[2]]
    if valid(state) and valid(complement(state)):
        r.append(state)
    return r

# o filho que tiver menos missionarios e o mais promissor
def obtenhaFA(son):
    return son[0]



def insereOrdenado(tupla, Laux):

    Laux.append(tupla)
    atual = len(Laux) - 1

    while atual > 0:
        if Laux[atual-1][1] < tupla[1]:
            break
        Laux[atual] = Laux[atual-1]
        atual -= 1
    Laux[atual] = tupla

    return Laux

def bestFirst(start,goal):
    count = 0
    l = [(start, 0)]
    Ltupla = ()
    fathers = dict()
    visited = [start]
    while (len(l)>0):
        count += 1
        father = l[0][0]
        print "\n\nNos que ainda devemos visitar: ", l
        del l[0]
        print "Estamos visitando o no: ", father
        for son in sons(father):
            if son not in visited:
                visited.append(son)
                Ltupla = son, obtenhaFA(son)
                l = insereOrdenado(Ltupla, l)
                print "Filho: ", Ltupla
                fathers[son2str(son)] = father
                if son == goal:
                    res = []
                    node = son
                    while node != start:
                        res.append(node)
                        node = fathers[son2str(node)]
                    res.append(start)
                    res.reverse()
                    print "Solucao encontrada: ", res
                    print "Numero total de nos visitados: ", count
                    return

if __name__ == '__main__':
    bestFirst([3,3,1],[0,0,0])