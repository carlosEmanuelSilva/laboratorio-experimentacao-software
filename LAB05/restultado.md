# Comparação dos tempos de resposta REST e GraphQL

| Tecnologia | RQ1 | RQ2 | RQ3 | RQ4 | RQ5 |
|------------|-----|-----|-----|-----|-----|
| REST       | 323 | 1,642 | 2,780 | 361 | 651 |
| GraphQL    | 500 | 621   | 2,690 | 305 | 1,320 |

# Comparação do tamanho de respostas REST e GraphQL

| Tecnologia | RQ1  | RQ2  | RQ3  | RQ4  | RQ5   |
|------------|------|------|------|------|-------|
| REST       | 34,9 | 547,6| 156,2| 2.1  | 116,5 |
| GraphQL    | 820B | 15,6 | 2.1  | 124B | 1107,9|

# Observação

* Os tempos estão em milisegundos;
* Os tamanhos estão em Kilobytes excetos os que explicitamente estão em outra medida.

# Análise

RQ1: Tempo de Resposta
REST foi mais rápido em três das cinco consultas, enquanto GraphQL foi mais rápido em duas. Isso significa que não há uma diferença clara no tempo de resposta entre as duas tecnologias.

RQ2: Tamanho das Respostas
GraphQL teve respostas menores em quatro das cinco consultas, mostrando que geralmente é mais eficiente em termos de tamanho de dados.

# Conclusão

GraphQL oferece vantagens em reduzir o tamanho das respostas, mas não é consistentemente mais rápido que REST. A escolha entre os dois deve considerar se você precisa mais de respostas menores ou de tempos de resposta mais rápidos. Além disso, fatores como a configuração do sistema podem ter afetado os resultados, então seria útil testar em diferentes condições no futuro.
