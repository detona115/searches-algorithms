import sys
def str2son(s):
    return [[s[0][0],s[0][1],s[0][2]],[s[1][0],s[1][1],s[1][2]],[s[2][0],s[2][1],s[2][2]]]
def son2str(s):
    return ''.join([str(v) for v in s])



def sons(s):
  tamanho = len(s)
  flag = -1
  x = 0
  LA = [[s[0][0],s[0][1],s[0][2]],[s[1][0],s[1][1],s[1][2]],[s[2][0],s[2][1],s[2][2]]]
  
  LP = []

  # Descobrir a posicao em que 0, movendo- o  teremos os filhos
  # x e y eh a posicao do 0
  while x < 3:#andando com x por linhas 
    y = 0
    while y < 3:#andando com y por colunas
      if LA[x][y] == 0:
	flag = 1
	break  
      y = y + 1

    if flag == 1:
      break

    x = x + 1


  if y + 1 <= 2: #se o 0 pode andar a direita
    LA[x][y] = LA[x][y+1]
    LA[x][y+1] = 0
    LP.append(LA) # insere essa nova configuracao no final da lista principal
    LA = [[s[0][0],s[0][1],s[0][2]],[s[1][0],s[1][1],s[1][2]],[s[2][0],s[2][1],s[2][2]]]
    #para nao perdermos a configuracao do pai

  if y - 1 >= 0: #se 0 pode andar a esquerda
  	LA[x][y] = LA[x][y-1]
  	LA[x][y-1] = 0
  	LP.append(LA) #inserindo o novo filho no final da lista principal
  	LA = [[s[0][0],s[0][1],s[0][2]],[s[1][0],s[1][1],s[1][2]],[s[2][0],s[2][1],s[2][2]]]
     

  if x - 1 >= 0: #se podemos subir o zero
    LA[x][y] = LA[x-1][y]
    LA[x-1][y] = 0
    LP.append(LA) #insere a nova configuracao no final da lista principal
    LA = [[s[0][0],s[0][1],s[0][2]],[s[1][0],s[1][1],s[1][2]],[s[2][0],s[2][1],s[2][2]]]

  if x + 1 <= 2: #se o 0 pode descer
    LA[x][y] = LA[x+1][y]
    LA[x+1][y] = 0
    LP.append(LA) #insere a nova configuracao no final da lista principal
    LA = [[s[0][0],s[0][1],s[0][2]],[s[1][0],s[1][1],s[1][2]],[s[2][0],s[2][1],s[2][2]]]
  # retorna os filhos
  return LP


def printPuzzle(s):
  for v in s:
    print v


"""
- Criar uma lista principal e uma auxiliar; 'l' e 'LA'
    - Dado que nossa l contem o elemento 'start', facamos:

      - Buscar os filhos do primeiro elemento da nossa l e coloca- los na LA
      - Retirar o primeiro elemento da l e concatenar essa nova l com a LA da seguinte forma:
      - l = LA . (l - l(0));
      - Repetir os passos acima enquanto nao encontrar 'goal' ou len(LP) > 0
"""
def profundidade(start,goal):
    l = [start]
    LA = []
    fathers = dict()
    visited = [start]
    while (len(l)>0):
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
        l = LA + l
        #apagando LA para usar novamente
        while len(LA) > 0 : LA.pop()        
                          
if __name__ == '__main__':
  profundidade([[0,3,6],[5,4,7],[1,2,8]],[[1,2,3],[4,5,6],[7,8,0]])
      
	
	
		      