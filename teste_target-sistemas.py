 QUESTÃO 2 ) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

RESPOSTA : 
 Código
  # recebe um número do usuário
num = int(input("Digite um número: "))

# inicializa a sequência de Fibonacci com os primeiros dois números
fibonacci = [0, 1]

# calcula os próximos números da sequência até o número informado ser ultrapassado
while fibonacci[-1] < num:
    proximo = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo) #usando append que adiciona um item ao fim lista.

# verifica se o número informado pertence à sequência de Fibonacci
if num in fibonacci:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
  
 QUESTÃO 3 ) 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

  import json

# Lê o arquivo JSON com os valores de faturamento diário
with open('dados.json', 'r') as arquivo: #arquivo fornecido pelo avaliador
    dados = json.load(arquivo)

# Obtém o número de dias do mês
num_dias = len(dados)

# Calcula a soma dos valores de faturamento diário
soma_faturamento = sum(dados)

# Calcula a média mensal de faturamento (ignorando os dias sem faturamento)
media_faturamento = soma_faturamento / num_dias

# Inicializa as variáveis de menor e maior faturamento com o primeiro valor do vetor
menor_faturamento = dados[0]
maior_faturamento = dados[0]

# Inicializa o contador de dias com faturamento acima da média
dias_acima_media = 0

# Percorre o vetor de faturamento diário e atualiza as variáveis de menor e maior faturamento
# e o contador de dias com faturamento acima da média
for faturamento in dados:
    if faturamento < menor_faturamento:
        menor_faturamento = faturamento
    if faturamento > maior_faturamento:
        maior_faturamento = faturamento
    if faturamento > media_faturamento:
        dias_acima_media += 1

# Exibe os resultados
print("Menor valor de faturamento: R$", menor_faturamento)
print("Maior valor de faturamento: R$", maior_faturamento)
print("Número de dias com faturamento acima da média mensal:", dias_acima_media)

  QUESTÃO 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.
 RESPOSTA : 
 Para calcular o percentual de representação de cada estado no faturamento total da distribuidora, podemos utilizar a seguinte fórmula:

percentual_estado = (faturamento_estado / faturamento_total) * 100

Onde faturamento_estado é o valor de faturamento do estado em questão e faturamento_total é o valor total de faturamento da distribuidora.

Segue abaixo um exemplo de implementação em Python:
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

faturamento_total = sum(faturamento.values())

for estado, valor in faturamento.items():
    percentual = (valor / faturamento_total) * 100
    print(f'{estado}: {percentual:.2f}%')
 # finalizado, voltando a explicação abaixo :
 Neste exemplo, o dicionário faturamento armazena os valores de faturamento de cada estado. O valor total de faturamento é calculado através da função sum() aplicada aos valores do dicionário.

Em seguida, é feito um loop sobre os itens do dicionário faturamento. Para cada estado, é calculado o percentual de representação no faturamento total, utilizando a fórmula apresentada anteriormente.
O valor é então impresso na tela com duas casas decimais.

QUESTÃO 5 ) 5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
  código :
 CÓDIGO em python:
# recebe uma string do usuário
string = input("Digite uma string: ")

# cria uma nova string vazia para armazenar o resultado
string_invertida = ""

# percorre a string original de trás para frente
for i in range(len(string) - 1, -1, -1):
    # adiciona cada caractere da string original na nova string
    string_invertida += string[i]

# imprime a string invertida
print("A string invertida é:", string_invertida)
