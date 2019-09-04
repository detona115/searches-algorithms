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

def bfs(start,goal):

    # Lista auxiliar que ira armazenar os filhos do pai corrente 
    LA = [] 
    # Criacao da lista principal que ira armazenar todos os caminhos possiveis 
    LP = [start]  
    fathers = dict()
    visited = [start]

    # Enquanto a lista principal estiver com elementos ou nao encontrar o no final vamos fazer a busca 
    while (len(LP)>0): 
        father = LP[0]
        print "\n\nNos que ainda devemos visitar: ", LP
        del LP[0]
        print "Estamos visitando o no: ", father        
        for son in sons(father):
            if son not in visited:               
                visited.append(son)
                # (Profundidade) Armazenando os filhos validos em na nossa lista auxiliar 
                LA.append(son)
                print "Filho: ", son
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
                    return                           
        # (Profundidade)Fazendo a concatenacao dos filhos com o que tinha na lista para que seja feita uma busca em profundidade 
        LP = LA + LP 
        # Zerando a lista auxiliar para usa- la novamente 
        while len(LA) > 0 : LA.pop() 

if __name__ == '__main__':
    bfs([3,3,1],[0,0,0])