import sys
import operator

def str2son(s):
    return [s[0],s[1]]

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
    if s[0] > 0 and s[1] < 7:
        estado = [s[0], s[1]]
     
        while estado[0] > 0 and estado[1] < 7:     
            estado[0] = estado[0] - 1           
            estado[1] = estado[1] + 1
        r.append(estado)

    # jarra de 7 abastece jarra de 5
    if s[1] > 0 and s[0] < 5:
        estado = [s[0], s[1]]
        while estado[0] < 5 and estado[1] > 0:
            estado[0] += 1
            estado[1] -= 1
        r.append(estado)

    return r

#insere de tras pra frente
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

# pega o jarro de 7 mais proximo de 4
def obtenhaFA(son):
	if son[1] < 4:
		return 4 - son[1]
	return son[1] - 4

# escolhe o no com menor heuristica
def bestFirst(start):
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
                # poe o cara de menor heuristica na frente pra visitalo
                l = insereOrdenado(Ltupla, l)
                print "Enfileirando o filho: ", Ltupla
                fathers[son2str(son)] = father
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
                  
if __name__ == '__main__':
	bestFirst([0,0])
	#insereOrdenado(([5,2],5),[([5,2],4),([5,2],4),([5,2],4),([5,2],4),([5,2],4)])