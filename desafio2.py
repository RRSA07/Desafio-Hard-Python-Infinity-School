from collections import defaultdict
import os

class Grafo:
    def __init__(self, matriz):
        self.matriz = matriz
        self.dictAlunos = defaultdict(list)
        
    def verificarOrientacao(self):
    # Verificar se na lista possui vertices com orientação Ex: ['jose','maria'] - ['maria','jose']
        for i in self.matriz:
            for j in self.matriz:
                if (i == list(reversed(j))):
                    self.matriz.remove(j)
        
    def gerarListaAdjacencias(self):
    # Gerar uma lista de Adjacencias onde a chave do dicionario é o vertice e os valores as suas conexões
        for i in self.matriz:
            self.dictAlunos[i[0]].append(i[1])
    
    def gerarCadeia(self):
    # Gerar uma cadeia de grafo não orientado para formar os grupos, estudante não pode participar de mais de um grupo, se estiver esses grupos se relacionam por esse vertice
        for key_x, value_x in self.dictAlunos.items():
            for key_y, value_y in self.dictAlunos.items():
                if (key_y in value_x) and (set(value_y) & set(value_x) == set()) and (key_x not in value_y): # verifica se o vertice da lista posterior está nas conexões
                    for k in value_y: # adciona as conexoes do vertice posterior formando a cadeia
                        value_x.append(k)
                    self.dictAlunos[key_y]='0'
                elif (key_y in value_x) and (set(value_y) & set(value_x) == set()) and (len(value_y)==1) and (key_x in value_y): # verificar se os vertices e conexoes já foram adicionados
                    self.dictAlunos[key_y]='0'                                                                                   
                elif (key_y in value_x) and (set(value_y) & set(value_x) != set()) and (set(key_x) & set(value_y) == set()): # verificar se os vertices e conexoes já foram adcionados
                    self.dictAlunos[key_y]='0'
        
        listaExcluir = []
        
        for key, value in self.dictAlunos.items():
            if (value == '0'):
                listaExcluir.append(key)

        for i in listaExcluir:
            del self.dictAlunos[i] 
    
    def gerarListaGrupos(self):
    # Gerar uma lista com base no dicionario para definir o tamanho dos grupos e verificar a condição    
        listaGrupos = []
        for key, value in self.dictAlunos.items():
            aux = []
            aux.append(key)
            for i in value:
                aux.append(i)
            listaGrupos.append(aux) 
        
        contValido = 0
        contInvalido = 0
        
        for i in listaGrupos:
            if len(i)<=3:
                contValido += 1
                print('\nGrupo {} valido com {} estudantes'.format(i,len(i)))
            elif len(i)>3:
                contInvalido += 1
                print('\nGrupo {} invalido com {} estudantes'.format(i, len(i)))
            
        print('\nQuantidade de grupos totais e invalidos respectivamente: [{},{}]\n'.format(len(listaGrupos), contInvalido))

def main():
    listaAlunos2 = [
    ['jose','maria'],
    ['jose','andre'],
    ['jose','barbara'],
    ['maria','andre'],
    ['andre','barbara'],
    ['andressa','luiza'],
    ['luiza','gabriel'],
    ['leandro','victor'],
    ['victor','john'],
    ['john','leandro'],
    ]

    listaAlunos1 = [
        ['jose','maria'],
        ['luiza','andre'],
    ]
    
    condicao = 'N'
    while (condicao.upper() == 'N'):
        os.system('clear') or None
        print('Desafio Python 2\n')
        opcao = int(input('Digite uma opção:\n1-Usar o primeiro exemplo do desafio:\n2-Usar o segundo exemplo do desafio\n3-Digitar os dados:\n\n'))
        validacao = False
        while (validacao == False):
            if (opcao == 1):
                validacao = True
                grafo=Grafo(listaAlunos1)
                grafo.verificarOrientacao()
                grafo.gerarListaAdjacencias()
                grafo.gerarCadeia()
                grafo.gerarListaGrupos()
            
            elif (opcao == 2):
                validacao = True
                grafo=Grafo(listaAlunos2)
                grafo.verificarOrientacao()
                grafo.gerarListaAdjacencias()
                grafo.gerarCadeia()
                grafo.gerarListaGrupos()

            elif (opcao == 3):
                validacao = True
                listaAlunos3 = []
                quant = int(input('Digite o tamanho da lista:\n'))
                for i in range(quant):
                    print('Digite os dois estudantes que estarão no mesmo grupo:\n')
                    print('Para encerrar os nomes digite N no nome do primeiro aluno\n')
                    nome1 = input('Digite o nome do primeiro aluno:  ')
                    nome2 = input('Digite o nome do segundo aluno:  ')
                    listaAlunos3.append([nome1, nome2])
                        
                grafo=Grafo(listaAlunos3)
                grafo.verificarOrientacao()
                grafo.gerarListaAdjacencias()
                grafo.gerarCadeia()
                grafo.gerarListaGrupos()

            elif (opcao != 1) or (opcao != 2) or (opcao != 3):
                opcao = int(input('Opcão invalida! Digite uma opcao valida!\n\n'))
        condicao = str(input('Deseja sair da aplicação? (S ou N)\n\n')) 
            
if __name__ == "__main__":
    main()
        