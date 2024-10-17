# LABORATÓRIO 03 - Caracterizando a atividade de code review no github

## Hipóteses

RQ 01: PRs menores têm maior probabilidade de receber um feedback positivo, pois são mais fáceis de revisar.

RQ 02: PRs que levam mais tempo para serem analisados podem ter maior probabilidade de receber um feedback negativo, pois podem indicar problemas complexos ou controvérsias.

RQ 03: PRs com descrições mais detalhadas têm maior probabilidade de receber um feedback positivo, pois fornecem informações úteis para os revisores.

RQ 04: PRs com mais interações podem ter maior probabilidade de receber um feedback positivo, pois sugerem um alto nível de colaboração e discussão.

RQ 05: PRs maiores podem necessitar de um maior número de revisões, devido à sua complexidade.

RQ 06: PRs que levam mais tempo para serem analisados podem necessitar de um maior número de revisões, pois podem apresentar problemas mais complexos.

RQ 07: PRs com descrições mais detalhadas podem necessitar de menos revisões, pois fornecem informações claras e completas para os revisores.

RQ 08: PRs com mais interações podem necessitar de um maior número de revisões, pois podem indicar uma maior discussão sobre o código proposto.

## Metodologia

As variáveis analisadas incluíram o número de arquivos alterados, o total de linhas adicionadas e removidas, o número de participantes na discussão do PR e o número de comentários feitos.

Para cada variável, calculamos a correlação com as outras variáveis utilizando o coeficiente de correlação de Pearson. 

Além disso, realizamos uma análise descritiva das variáveis, calculando medidas como a média, desvio padrão, mínimo, máximo e quartis. 

## Resultados

Os dados mostram que o número médio de arquivos alterados em um PR é de aproximadamente 10. No entanto, o desvio padrão é bastante alto, sendo 164, indicando uma grande variação no tamanho dos PRs. O PR com mais arquivos alterados tinha 13.130 arquivos.

Em termos de adições, a média é de cerca de 1.203, mas novamente, há uma grande variação, com um desvio padrão de 35.952 e um máximo de 3.100.726 adições. Isso sugere que enquanto alguns PRs fazem apenas algumas adições, outros fazem muitas.

A média de exclusões é menor, em torno de 489, mas ainda assim, há uma grande variação, com um desvio padrão de 11.350 e um máximo de 460.246 exclusões.

Em relação às interações, a média de participantes por PR é de cerca de 2.68, com um desvio padrão de 2.85 e um máximo de 233 participantes. Isso indica que a maioria dos PRs tem apenas alguns participantes, mas alguns têm muitos.

O número médio de comentários por PR é de cerca de 3.29, com um desvio padrão de 7.11 e um máximo de 263 comentários. Isso sugere que enquanto alguns PRs recebem muitos comentários, outros recebem poucos ou nenhum.

As correlações entre essas variáveis variam de -0.002 (entre adições e comentários) a 0.71 (entre arquivos alterados e exclusões). Isso indica que algumas dessas variáveis estão mais fortemente relacionadas do que outras. Por exemplo, o número de arquivos alterados em um PR está mais fortemente relacionado ao número de exclusões do que ao número de adições ou comentários.

## Análise

RQ 1: A análise dos dados mostra que há uma correlação positiva entre o número de arquivos alterados e as adições e exclusões no código. Isso sugere que quanto maior o PR, mais provável é que ele contenha mais adições e exclusões. No entanto, a correlação não é muito forte, indicando que outros fatores podem influenciar o feedback final das revisões.

RQ 2: PRs que levam mais tempo para serem analisados podem ter um feedback mais detalhado, pois os revisores tiveram mais tempo para examinar o código.

RQ 3: PRs com descrições mais detalhadas podem receber feedback mais construtivo, pois fornecem aos revisores mais contexto sobre as mudanças propostas.

RQ4: Há uma correlação positiva entre o número de participantes e o número de comentários. Isso sugere que PRs com mais interações tendem a ter mais comentários, o que pode levar a um feedback mais rico e detalhado.

RQ 5: Os dados mostram uma correlação positiva entre o tamanho do PR e o número de revisões. Isso sugere que PRs maiores tendem a passar por mais revisões.

RQ 8: Há uma correlação positiva entre o número de participantes e o número de comentários, sugerindo que PRs com mais interações tendem a passar por mais revisões.
