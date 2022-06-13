'''       AUTORES

Felipe Rocha
Gabrielle Sperandeo
Gabriel Tellaroli

Curso: Ciência da Computação - 7º Semestre/2022
'''

'''       DOCUMENTAÇÃO       
    
    1) Em caráter de implementação, a pilha lê se da direita (topo) para a esquerda
        Ex.: na pilha [$, q, x], o topo da pilha é "x"

    2) Conforme alinhado com o professor José Neto via e-mail, o descritivo da atividade consta a linha "N70G98G73Z85R02K10F03".
        Entretanto, o correto seria: N70G98G73Z85T02K10F03

    3) Ao inicializar o programa, certifica-se que o arquivo de entrada encontra-se na mesma pasta deste programa (analisador_sintatico.py),
        visto que será necessário digitar o nome do programa para sua correta execução.
'''

#Importando a biblioteca Regex para verificação do conteúdo da matriz
import re

''' ************* MANIPULANDO PILHA ************* '''

class Pilha:

    # Inicializa a pilha
     def __init__(self):
         self.items = []

    # Obtém o valor do topo da pilha
     def top(self):
            return self.items[len(self.items)-1] 

    # Inclui um item no topo da pilha       
     def push(self, item):
         self.items.append(item)

    # Remove o item do topo da pilha
     def pop(self):
         return self.items.pop(len(self.items)-1)

    # Imprime todos os itens da pilha
     def imprime_pilha(self):
         print(str(self.items))


''' ************* FIM MANIPULAÇÃO PILHA ************* '''

''' ************* MANIPULANDO ARQUIVO ************* '''

# Realiza a leitura do arquivo
def le_arq(nome):
    try: 
        file = open(nome, 'r')
        #Lendo o arquivo e trocando os espaços por null, concatenando assim todas as linhas, e retornando na variável entrada
        entrada = file.read().replace(" ", "").replace("\n", "")
        return entrada
    except:
        print("\nNão foi possível abrir o arquivo {0}!\n\nPor favor, certifique-se que foi digitado corretamente\na.txt".format(nome))
        exit()
    

''' ************* FIM MANIPULAÇÃO ARQUIVO ************* '''

''' ************* MANIPULAÇÕES DE VARIÁVEIS ************* '''

#Recebe uma string, e a devolve invertida
def inverter(entrada):
    return entrada[::-1]

#Definindo uma matriz com todas as produções da tabela parser

matriz = [# Col 0     Col 1         Col 2      Col 3        Col 4       Col 5          Col 6        Col 7       Col 8       Col 9       Col 10        Col 11        Col 12      Col 13      Col 14       Col 15     Col 16        Col 17    Col 18      Col 19      Col 20      Col 21      Col 22      Col 23      Col 24      Col 25       Col 26         Col 27
          ['Parse',        'G',        'X',        'Y',         'Z',         'A',         'B',         'C',         'I',         'J',         'K',         'T',         'S',         'F',         'M',        'O',        'N',        '0',        '1',        '2',        '3',        '4',        '5',        '6',        '7',        '8',        '9',             '$'], #linha 0
          [    'p',    'ERR01',    'ERR02',    'ERR03',     'ERR04',     'ERR05',     'ERR06',     'ERR07',     'ERR08',     'ERR09',     'ERR10',    'ERR011',    'ERR012',    'ERR013',    'ERR014',  'p -> qx',   'ERR015',   'ERR016',   'ERR017',   'ERR018',   'ERR019',   'ERR020',   'ERR021',   'ERR022',   'ERR023',   'ERR024',   'ERR025',        'p -> ε'], #linha 1
          [    'x',   'ERR026',   'ERR027',   'ERR028',    'ERR029',    'ERR030',    'ERR031',    'ERR032',    'ERR033',    'ERR034',    'ERR035',    'ERR036',    'ERR037',    'ERR038',    'ERR039',   'ERR040',  'x -> ra',   'ERR041',   'ERR042',   'ERR043',   'ERR044',   'ERR045',   'ERR046',   'ERR047',   'ERR048',   'ERR049',   'ERR050',        'x -> ε'], #linha 2
          [    'a',   'ERR051',   'ERR052',   'ERR053',    'ERR054',    'ERR055',    'ERR056',    'ERR057',    'ERR058',    'ERR059',    'ERR060',    'ERR061',    'ERR062',    'ERR063',    'ERR064',   'ERR065',   'a -> x',   'ERR066',   'ERR067',   'ERR068',   'ERR069',   'ERR070',   'ERR071',   'ERR072',   'ERR073',   'ERR074',   'ERR075',        'a -> ε'], #linha 3
          [    'q',   'ERR076',   'ERR077',   'ERR078',    'ERR079',    'ERR080',    'ERR081',    'ERR082',    'ERR083',    'ERR084',    'ERR085',    'ERR086',    'ERR087',    'ERR088',    'ERR089',  'q -> Oz',   'ERR090',   'ERR091',   'ERR092',   'ERR093',   'ERR094',   'ERR095',   'ERR096',   'ERR097',   'ERR098',   'ERR099',   'ERR100',        'q -> ε'], #linha 4
          [    'r',   'ERR101',   'ERR102',   'ERR103',    'ERR104',    'ERR105',    'ERR106',    'ERR107',    'ERR108',    'ERR109',    'ERR110',    'ERR111',    'ERR112',    'ERR113',    'ERR114',   'ERR115',  'r -> dy',   'ERR116',   'ERR117',   'ERR118',   'ERR119',   'ERR120',   'ERR121',   'ERR122',   'ERR123',   'ERR124',   'ERR125',        'r -> ε'], #linha 5
          [    'y',  'y -> eb',  'y -> eb',  'y -> eb',   'y -> eb',   'y -> eb',   'y -> eb',   'y -> eb',   'y -> eb',   'y -> eb',   'y -> eb',   'y -> eb',   'y -> eb',   'y -> eb',   'y -> eb',   'ERR126',   'ERR127',   'ERR128',   'ERR129',   'ERR130',   'ERR131',   'ERR132',   'ERR133',   'ERR134',   'ERR135',   'ERR136',   'ERR137',        'y -> ε'], #linha 6
          [    'b',   'b -> y',   'b -> y',   'b -> y',    'b -> y',    'b -> y',    'b -> y',    'b -> y',    'b -> y',    'b -> y',    'b -> y',    'b -> y',    'b -> y',    'b -> y',    'b -> y',   'ERR138',   'b -> ε',   'ERR139',   'ERR140',   'ERR141',   'ERR142',   'ERR143',   'ERR144',   'ERR145',   'ERR146',   'ERR147',   'ERR148',        'b -> ε'], #linha 7
          [    'd',   'ERR149',   'ERR150',   'ERR151',    'ERR152',    'ERR153',    'ERR154',    'ERR155',    'ERR156',    'ERR157',    'ERR158',    'ERR159',    'ERR160',    'ERR161',    'ERR162',   'ERR163',  'd -> Nz',   'ERR164',   'ERR165',   'ERR166',   'ERR167',   'ERR168',   'ERR169',   'ERR170',   'ERR171',   'ERR172',   'ERR173',        'ERR174'], #linha 8
          [    'e', 'e -> hll', 'e -> hll', 'e -> hll',  'e -> hll',  'e -> hll',  'e -> hll',  'e -> hll',  'e -> hll',  'e -> hll',  'e -> hll',  'e -> hll',  'e -> hll',  'e -> hll',  'e -> hll',   'ERR175',   'ERR176',   'ERR177',   'ERR178',   'ERR179',   'ERR180',   'ERR181',   'ERR182',   'ERR183',   'ERR184',   'ERR185',   'ERR186',        'e -> ε'], #linha 9
          [    'z',   'ERR187',   'ERR188',   'ERR189',    'ERR190',    'ERR191',    'ERR192',    'ERR193',    'ERR194',    'ERR195',    'ERR196',    'ERR197',    'ERR198',    'ERR199',    'ERR200',   'ERR201',   'ERR202',  'z -> lc',  'z -> lc',  'z -> lc',  'z -> lc',  'z -> lc',  'z -> lc',  'z -> lc',  'z -> lc',  'z -> lc',  'z -> lc',        'z -> ε'], #linha 10
          [    'c',   'c -> ε',   'c -> ε',   'c -> ε',    'c -> ε',    'c -> ε',    'c -> ε',    'c -> ε',    'c -> ε',    'c -> ε',    'c -> ε',    'c -> ε',    'c -> ε',    'c -> ε',    'c -> ε',   'ERR203',   'c -> ε',   'c -> z',   'c -> z',   'c -> z',   'c -> z',   'c -> z',   'c -> z',   'c -> z',   'c -> z',   'c -> z',   'c -> z',        'c -> ε'], #linha 11
          [    'h',   'h -> G',   'h -> X',   'h -> Y',    'h -> Z',    'h -> A',    'h -> B',    'h -> C',    'h -> I',    'h -> J',    'h -> K',    'h -> T',    'h -> S',    'h -> F',    'h -> M',   'ERR204',   'ERR205',   'ERR206',   'ERR207',   'ERR208',   'ERR209',   'ERR210',   'ERR211',   'ERR212',   'ERR213',   'ERR214',   'ERR215',        'ERR216'], #linha 12
          [    'l',   'ERR217',   'ERR218',   'ERR219',    'ERR220',    'ERR221',    'ERR222',    'ERR223',    'ERR224',    'ERR225',    'ERR226',    'ERR227',    'ERR228',    'ERR229',    'ERR230',   'ERR231',   'ERR232',   'l -> 0',   'l -> 1',   'l -> 2',   'l -> 3',   'l -> 4',   'l -> 5',   'l -> 6',   'l -> 7',   'l -> 8',   'l -> 9',        'l -> ε'], #linha 13
]


''' ************* MAIN ************* '''

print("\n************** Analisador Sintático **************")
nome = str(input("\nDigite o nome do arquivo .txt: "))

entrada = le_arq(nome)

# Instancia duas pilhas vazias
pilha = Pilha() #Pilha que contém a troca de terminais/não terminais (1º coluna da tabela: *Pilha* | Sentença | Regra)
pilha_sentenca = Pilha() #Pilha que contém a sentença a ser testada (2º coluna da tabela: Pilha | *Sentença* | Regra)

# Invertendo a string, para que a ordem dos valores na pilha estejam corretas
entrada_invertida = inverter(entrada)

# Inserindo o $ na Sentença
pilha_sentenca.push("$")

# Insere elementos na pilha_sentenca
for i in range(0, len(entrada_invertida)):
    pilha_sentenca.push(entrada_invertida[i])

# Insere elementos na pilha (apenas o símbolo inicial e o $)
# Notar que estão sendo incluídos de forma invertida para obedecer a ordem dos valores na pilha
pilha.push("$")
pilha.push("p")

print('\n************** TABELA **************')
print()

# Obtém o topo da Pilha
topo_pilha = pilha.top()

# Obtém o topo da Sentença
topo_sentenca = pilha_sentenca.top()

#Variável para apresentação da iteração
l = 1

while not((pilha.top() == pilha_sentenca.top() == '$')):

    print("************** ITERAÇÃO Nº {0} **************".format(l))

    #Começa no 1 pois a posição 0 é a palavra "Parse"
    for i in range(1, 14): #Iteração para as listas
        if (matriz[i][0] == topo_pilha): #Itera pelos não terminais da gramática, que estão em matriz[i][0]
            posicao_linha = i
            break

    #Iteração para os **índices** de cada lista, verificando qual sua posição, e gravando-a em j
    for j in range(1, 28): 
        if (matriz[0][j] == topo_sentenca):
            posicao_coluna = j
            break
            
    #Verifica se a posição matriz[i][posicao] possui algum valor diferente de vazio
    if ( not( (re.search("\AERR", matriz[posicao_linha][posicao_coluna])) ) and
         not( (topo_pilha == topo_sentenca) ) and
         not( (topo_pilha == "ε") )
       ):

        print("\nRegra:", matriz[posicao_linha][posicao_coluna])
        entra_pilha = inverter(matriz[posicao_linha][posicao_coluna][5:])
        print()

        #Retira o caractere que estava no topo, para receber a nova produção
        pilha.pop()

        # Obtem os caracteres da produção e os insere na pilha.
        # Exemplo: p -> qx, irá obter o caractere x e inserir na pilha, e depois o caractere q e inserir na pilha
        for k in range(0, len(entra_pilha)):
            caractere = entra_pilha[k]
            pilha.push(caractere)
        
        print("Pilha:")
        pilha.imprime_pilha()

        print("\nSentença:")
        pilha_sentenca.imprime_pilha()  

        # Atualiza os valores do topo da Pilha e da Sentença
        topo_pilha = pilha.top()
        topo_sentenca = pilha_sentenca.top()

        print()

    elif (topo_pilha == topo_sentenca):

        print("\nRegra: retira o", topo_pilha)
        print()

        # Remove o topo da Pilha e da Sentença
        pilha.pop()
        pilha_sentenca.pop()

        print("Pilha:")
        pilha.imprime_pilha()

        print("\nSentença:")
        pilha_sentenca.imprime_pilha()
        print()

        # Atualiza os valores do topo da Pilha e da Sentença
        topo_pilha = pilha.top()
        topo_sentenca = pilha_sentenca.top()
        
    elif(topo_pilha == "ε"):

        print("\nRegra: retira o", topo_pilha)
        print()

        # Remove o topo da Pilha
        pilha.pop()

        print("Pilha:")
        pilha.imprime_pilha()

        print("\nSentença:")
        pilha_sentenca.imprime_pilha()
        print()

        # Atualiza os valores do topo da Pilha e da Sentença
        topo_pilha = pilha.top()
        topo_sentenca = pilha_sentenca.top()

    else: #Realiza a verificação e apresentação do erro, caso identificado
        
        # Variável para verificação do erro. Caso o programa chegue neste ELSE, entende-se que ocorreu um erro
        erro = 1

        # Obtém o caractere que ocasionou o erro a ser verificado
        caractere = pilha_sentenca.top()

        for j in range(1, 28):

            # Se o caractere está na lista de não terminais da gramática, ele é um erro identificado
            if (caractere == matriz[0][j]):
                erro = 0
                break

        if (erro == 0):
            print("\nIdentificado '{0}'!".format(matriz[posicao_linha][posicao_coluna]))
            print("\nÍndice do erro: matriz[{0}][{1}].\n".format(posicao_linha, posicao_coluna))
            
        elif (erro == 1):
            print("\nO caractere '{0}' não faz parte da gramática!\n".format(pilha_sentenca.top()))

        else:
            print("\nErro não identificado!")
        
        print("************** RESULTADO ********************")
        print("\nSentença REJEITADA!\n")
        exit()
        
    l += 1

print("************** RESULTADO ********************")
print("\nSentença ACEITA!\n")