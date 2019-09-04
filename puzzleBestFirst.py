import sys
import math
def str2son(s):
    return [[s[0][0],s[0][1],s[0][2]],[s[1][0],s[1][1],s[1][2]],[s[2][0],s[2][1],s[2][2]]]
def son2str(s):
    return ''.join([str(v) for v in s])

def achaPos(LA, valor):

  flag = -1
  x = 0
  while x < 3:#andando com x por linhas 
    y = 0
    while y < 3:#andando com y por colunas
      if LA[x][y] == valor:
        flag = 1
        break  
      y = y + 1

    if flag == 1:
      break

    x = x + 1
  return x,y

def sons(s):
 
  LP = []
  LA = [[s[0][0],s[0][1],s[0][2]],[s[1][0],s[1][1],s[1][2]],[s[2][0],s[2][1],s[2][2]]]
  x,y = achaPos(LA, 0)
  
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
 
  return LP

def printPuzzle(s):
  for v in s:
    print v

def obtenhaFA(son, goal):  
  
  total = 0
  for linha in son:
    for coluna in linha:
      x,y = achaPos(son, coluna)
      if x == 0 and y+1 == coluna:
          continue
      if x == 1 and y+4 == coluna:
          continue
      if x == 2:
        if y+7 == coluna:
          continue
        if coluna == 0 and y == 2:
          continue

      if coluna >= 1 and coluna <= 3:
        i = 0
        j = coluna-1
      if coluna >= 4 and coluna <= 6:
        i = 1
        j = coluna - 4
      if coluna == 7 or coluna == 8:
        i = 2
        j = coluna - 7
      if coluna == 0:
        i = 2
        j = 2
      total += abs(x-i) + abs(y-j)

  return total

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
  l = [(start, 0)]
  Ltupla = ()
  fathers = dict()
  visited = [start]
  while (len(l)>0):
    father = l[0][0]
    print "\n\nNos que ainda devemos visitar: ", l
    del l[0]
    print "Estamos visitando o no: ", father
    for son in sons(father):
      if son not in visited:
        visited.append(son)
        Ltupla = son, obtenhaFA(son, goal)
        l = insereOrdenado(Ltupla, l)
        print "Enfileirando ordenadamente o filho: ", Ltupla
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

if __name__ == '__main__':
  bestFirst([[1,8,4],[3,5,7],[6,2,0]],[[1,2,3],[4,5,6],[7,8,0]])		      
  