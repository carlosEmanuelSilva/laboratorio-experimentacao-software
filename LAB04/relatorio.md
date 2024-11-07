# Análise de padrões em post de ensino de engenharia de software no reddit 
## Introdução
O Reddit é uma rede social na qual os usuários podem submeter conteúdos como texto, links, imagens e vídeos e estas submissões recebem interações na forma de "upvotes" e "downvotes", comentários e compartilhamentos. Uma peculiaridade desse aplicativo é que ele como um todo é dividido em disversas comunidades -chamadas de "subreddits"- as quais discutem tópicos específicos como: automovéis, filmes, séries, jogos e, claro, técnologia. Desse modo, é vasto o contéudo sobre computação na rede social e, portanto, também é vasta a troca de experiência, informções e aprendizados nas comunidades voltadas para assuntos relativos à software no reddit. 

Sob o recorte da área de T.I, encontra-se uma grande lacuna no que diz respeito a parte educacional/ensino desses subreddits e, por conseguinte, o presente trabalho visa caracterizar os posts e, mais especificamente as tags desses posts, de ensino nas comunidades de software para poder melhor compreender o que faz um bom contéudo de ensino na rede social.
### Questões
1. Qual a relação entre upvotes e comentários nas tags principais do subreddit.
2. Qual as linguagens recebem mais interações em seus posts.
3. Os posts com tags de discussão e pedido de ajuda geram engajamento?
## Metodologia
O estudo será feito utilizando a seguinte metodologia:
1. A API gratuita do Reddit será utilizada para coletar uma amostra de dados dos posts no subreddits r/learnprogramming na plataforma. Os dados coletados são: 'tags', 'descrição do post', 'titulo do post', 'upvotes', 'comentários', 'compartilhamentos'.
2. Será criado um script em Python que realiza requisições à API para extrair informações relacionadas aos posts nos subreddits selecionados. O script coletara os dados citados no item 1 e os armazenará em um arquivo .csv.
3. Em seguida, os dados armazenado serão passados para um ferramenta de B.I a fim de tratar e criar visualizações dos dados coletados.
4. Finalmente, com os dados coletados e tratados, será feita a análise do dataset para resposter as perguntas de pesquisa. 
## Resultados
A partir da análise dos dados coletados, fica claro que:
1. Post, em geral, custumam ter muito mais upvotes do que comentários, provando que posts com mais comentários provavelmente tem uma interação mais organica e o topico é relevante.
2. Python é a linguaguem que recebe mais interação, seja no ambito de upvotes quanto de comentários. Isso já era esperado, pois python é uma das linguagens de programação mais utilizadas e com comunidade mais ativas, como mosstra [essa pesquisa da jetbrains](https://www.jetbrains.com/lp/devecosystem-2023/)
3. Definitivamente, observanto o gráfico de barras apresentado no B.I, essas tags são as que mais possuem interação e engajamento na comunidade.
