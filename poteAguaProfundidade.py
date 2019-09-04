def str2son(s):
    return [s[0],s[1],s[2]]
def son2str(s):
    return ''.join([str(v) for v in s])

def sons(s):
    r = []
    
    # enche jarra de 5 litros
    if s[0] != 5:
        estado = [s[0], s[1]]
        estado[0] = 5
        r.append(estado)
    
    # enche jarra de 7 litros
    if s[1] != 7:
        estado = [s[0], s[1]]
        estado[1] = 7
        r.append(estado)
   

    # esvazia jarra de 5 litros
    if s[0] != 0:
        estado = [s[0], s[1]]
        estado[0] = 0
        r.append(estado)

    # esvazia jarra de 7 litros
    if s[1] != 0:
        estado = [s[0], s[1]]
        estado[1] = 0
        r.append(estado)

    # jara de 5 abastece jarra de 7
    if s[0] != 0:
        estado = [s[0], s[1]]
        while estado[0] > 0 and estado[1] < 7:
            estado[0] = estado[0] - 1
            estado[1] = estado[1] + 1
        r.append(estado)

    # jarra de 7 abastece jarra de 5
    if s[1] != 0:
        estado = [s[0], s[1]]
        while estado[0] < 5 and estado[1] > 0:
            estado[0] += 1
            estado[1] -= 1
        r.append(estado)

    return r

# para explicacao ver puzzle profundidade
def profundidade(start):
    count = 0
    l = [start]
    LA = []
    fathers = dict()
    visited = [start]
    while (len(l)>0):
        count += 1
        father = l[0]
        print "\n\nNos que ainda devemos visitar: ", l
        del l[0]
        print "Estamos visitando o no: ", father
        for son in sons(father):
            if son not in visited:
                visited.append(son)
                LA.append(son)
                print "Filho: ", son
                fathers[son2str(son)] = father
                # no goal
                if son[0] == 4 or son[1] == 4:
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
        l = LA + l
        while len(LA) > 0 : LA.pop()                

if __name__ == '__main__':
    profundidade([0,0])  # [5,7]

