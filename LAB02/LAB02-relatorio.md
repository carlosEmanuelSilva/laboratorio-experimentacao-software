# LABORATÓRIO 02 - Um estudo das características de qualidade de sistemas Java

## Introdução
Em projetos Open Source, o código-fonte é público e é permitido que todas as pessoas possam acessa-lo, modifica-lo e distribui-lo. Desse modo, projetos com essas características podem apresentar uma séries de vantagens, como: confiabilidade do software, redução dos custos, trânsparencia, segurança. Contudo, projetos os quais podem ser modificados por qualquer um também apresentam riscos de deterioração da qualidade interna do código.

Portanto, com o experimento desenvolvido durate esse segundo laboratório, pretende-se analisar os aspectos de qualidade de repositórios de projetos escritos em Java pela ótica das méticas para classe propostas por Chidamber e Kemerer, o conjunto de métricas *CK*.

## Hipóteses

RQ 01: Repositórios mais populares tendem a ter uma maior qualidade de código, pois um alto número de estrelas pode indicar um alto numero de desenvolvedores envolvidos no projeto, levando a um código mais revisado e refinado.

RQ 02: Repositórios mais maduros podem apresentar características de qualidade superiores em comparação aos repositórios mais novos, pois tiveram mais tempo para refinar e melhorar seu código.

RQ 03: Repositórios com alta atividad podem ter uma melhor qualidade de código, pois isso pode indicar que os desenvolvedores estão constantemente trabalhando para melhorar e atualizar o sistema.

RQ 04: O tamanho do repositório pode não ter uma relação direta com a qualidade do código. Enquanto repositórios maiores podem ter mais complexidade e potencialmente mais problemas, eles também podem ter mais recursos e uma equipe de desenvolvimento maior, o que poderia levar a um código de maior qualidade.

## Metodologia

Para cada questão de pesquisa, comparamos as características do processo de desenvolvimento dos repositórios com os valores obtidos para as métricas de qualidade. Os resultados foram sumarizados através de medidas de tendência central (média, mediana) e dispersão (desvio padrão) para cada repositório.

## Resultados 

RQ 01: A análise dos dados mostra que os repositórios mais populares tendem a ter um CBO médio de 3.52, uma DIT média de 1.10 e um LCOM médio de 1.06. Isso sugere que os repositórios mais populares têm um baixo acoplamento entre objetos, uma estrutura de herança simples e alta coesão entre métodos, indicando uma boa qualidade de código.

RQ 02: Os repositórios mais maduros apresentam um CBO médio de 5.30, uma DIT média de 1.46 e um LCOM médio de 139.81. Embora esses valores sejam maiores do que os dos repositórios mais populares, eles ainda indicam um nível razoável de qualidade, sugerindo que a maturidade do repositório pode contribuir para a qualidade do código.

RQ 03: Os repositórios mais ativos têm um CBO médio de 6.32, uma DIT média de 1.12 e um LCOM médio de 4304.33. Esses valores são significativamente maiores do que os dos repositórios mais populares e maduros, sugerindo que a atividade frequente no repositório pode levar a um código mais complexo e potencialmente de menor qualidade.

RQ 04: Os repositórios maiores apresentam um CBO médio de 18.90, uma DIT média de 49.99 e um LCOM médio de 118.54. Estes são os valores mais altos entre todas as categorias, indicando que o tamanho do repositório está fortemente correlacionado com a complexidade e potencialmente a menor qualidade do código.

## Comparação entre hipóteses e reultados.

RQ 01: A análise dos dados suporta a hipótese de que repositórios mais populares tendem a ter uma maior qualidade de código. Os valores baixos para CBO, DIT e LCOM indicam um código bem estruturado e de fácil manutenção, o que pode ser atribuído à contribuição de um grande número de desenvolvedores.

RQ 02: Contrariamente à hipótese inicial, os repositórios mais maduros apresentaram valores maiores para as métricas de qualidade em comparação aos repositórios mais populares. Isso sugere que, embora o tempo possa permitir a melhoria do código, também pode levar a um aumento na complexidade, resultando em um acoplamento maior entre objetos e uma menor coesão entre métodos.

RQ 03: A hipótese de que repositórios com alta atividade teriam uma melhor qualidade de código não foi confirmada pelos dados. Na verdade, os repositórios mais ativos apresentaram os maiores valores para as métricas de qualidade, indicando um código mais complexo e potencialmente de menor qualidade. Isso sugere que a constante atualização e modificação do código podem torná-lo mais difícil de manter e entender.

RQ 04: A análise dos dados confirmou a hipótese de que o tamanho do repositório não tem uma relação direta com a qualidade do código. Os repositórios maiores apresentaram os maiores valores para as métricas de qualidade, indicando um código mais complexo. Embora repositórios maiores possam ter mais recursos e uma equipe de desenvolvimento maior, isso parece levar a um código mais complexo e potencialmente de menor qualidade. Portanto, é importante gerenciar adequadamente o crescimento do projeto para garantir a manutenção da qualidade do código.

## Referências
O que é open source? Disponível em: <https://www.redhat.com/pt-br/topics/open-source/what-is-open-source#open-source-princ%C3%ADpios-e-valores>. Acesso em: 12 set. 2024. 
