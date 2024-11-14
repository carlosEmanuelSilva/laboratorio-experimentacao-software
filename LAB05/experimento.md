
# Desenho do experimento

## Hipotése nula e alternativa

### RQ.1: Respostas às consultas GraphQL são mais rápidas que respostas às consultas REST?

* Hipótese nula: não existe diferença entre o tempo de resposta de consultas que utilizam GraphQL ou REST.
* Hipótese nula: o tempo de resposta de uma consulta GraphQL é maior do que o de uma consulta REST.
* Hipótese alternativa: as consultas GraphQL apresentam menor tempo de respota em comparação à consultas REST.

### RQ.2: Respostas às consultas GraphQL tem tamanho menor que respostas às consultas REST?

* Hipótese nula: as respostas de consultas GraphQL possuem tamanho maior que as de consultas REST.
* Hipótese nula: as respostas de ambas as estratégias possuem uma diferença irrelevante em relação ao tamanho.
* Hipótese alternativa: as respostas de consultas as quais utilizam GraphQL são menores quando comparadas com o tamanho das que utilizam REST.

## Variáveis dependentes e independentes

As variáveis dependentes do experimento são: **tempo de resposta** e **tamanho das respostas** das consultas.  
A variável independente do experimento é: **estratégia de consulta** utilizada.  

## Tratamento

Dado que o fator do experimento é a estratégia de consulta, os tratamentos utilizados são: **REST** e **GraphQL**.  

## Objetos experimentais

O objeto experimental do experimento presente é um conjunto de consultas à API da plataforma GitHub as quais deverãm ser performadas tanto em REST quanto em GraphQL. A seguir estão descritas as consultas.

### Consultas

1. Listar quais os repositórios de um usuário específico.
2. Obter issues e pull requests de um repositório específico.
3. Listar repositórios de uma linguagem de programação específica e ordenar pelo núemro de estrelas de forma crescente.
4. Obter informações sobre os colaboradores de um repositório.
5. Listar informções de commits limitados por um período de tempo.

## Tipo de projeto experimental

O método de experimentação escolhido é *related between subjects*. Portanto, todas os objetos experimentais serão executados utilizando os ambos os tratamentos propostos anteriormente.  

## Quantidade de medições

Seram medidos o tempo de resposta em segundos de cada consulta e quantos campos são retornados no corpo de resposta de cada consulta.

## Ameaças à validade 

### Ameaça de construção

* Apesar de depender mais do modo como a consulta será realizada, o experimento pode ser afetado pela configuração da máquina que executar os scrips de consulta.

### Ameaça à validade externa

* O conjunto de objetos definidos pode não ser o suficiente para sustentar uma generalização dos resultados obtidos a partir desse experimento.
