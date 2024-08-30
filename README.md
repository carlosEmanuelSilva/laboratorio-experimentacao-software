# Introdução

Os softwares open-source vêm tendo um crescimento significativo nas últimas décadas. Uma infinidade de projetos open-source abrange uma ampla gama de aplicações, desde sistemas operacionais completos até bibliotecas de software especializadas. No entanto, nem todos os projetos open-source são igualmente bem-sucedidos. Alguns projetos atraem grandes comunidades de usuários e desenvolvedores, enquanto outros lutam para ganhar tração.

Este relatório busca explorar as características dos projetos open-source mais populares no GitHub, especificamente sobre as seguintes questões:

* **RQ 01:** Sistemas populares são maduros/antigos?   
* **RQ 02:** Sistemas populares recebem muita contribuição externa?
* **RQ 03:** Sistemas populares lançam releases com frequência? 
* **RQ 04:** Sistemas populares são atualizados com frequência? 
* **RQ 05:** Sistemas populares são escritos nas linguagens mais populares?
* **RQ 06:** Sistemas populares possuem um alto percentual de issues fechadas?

# Hipótese

**RQ 01:** Sistemas populares tendem a ser mais maduros. Porque eles tiveram tempo para desenvolver uma base de usuários e uma comunidade de contribuidores, bem como para refinar e melhorar seu código.

**RQ 02:** Sistemas populares recebem uma quantidade significativa de contribuições externas. A popularidade pode atrair um grande número de desenvolvedores que desejam contribuir com o projeto.

**RQ 03:** Sistemas populares não necessariamente lançam releases com alta frequência. A frequência de lançamentos pode depender mais da filosofia de gerenciamento do projeto ou da aplicação do software.

**RQ 04:** Sistemas populares são atualizados com frequência. Manter o software atualizado é importante para corrigir bugs, melhorar a segurança e adicionar novos recursos.

**RQ 05:** Sistemas populares são frequentemente escritos em linguagens de programação populares. Linguagens populares têm grandes comunidades de desenvolvedores, ampla documentação e suporte, o que facilita o desenvolvimento e a manutenção do software.

**RQ 06:** Sistemas populares têm uma alta porcentagem de issues fechadas. Uma alta taxa de issues fechadas pode indicar que a equipe de desenvolvimento é responsiva e eficaz na resolução de problemas, o que pode contribuir para a popularidade do software.

# Metodologia

**RQ 01:**

**RQ 02:** Para analisar se sistemas populares recebem muita contribuição externas, serão analisados o valor minimo, máximo, quartil inferior, média e quartil superior do número total de pull requests aceitas junto com um gráfico scatter com todos os resultados.

**RQ 03:** Para analisar se sistemas populares lançam releases com muita frequência, serão analisados o valor minimo, máximo, quartil inferior, média e quartil superior do número total de releases junto com um gráfico scatter com todos os resultados.

**RQ 04:**

**RQ 05:** Para analisar se sistemas populares utilizam linguagens populares, serão analisados as 5 linguagens mais usadas e ver que posição elas ocupam no ranking de linguagens mais populares de acordo com a pesquisa da jetbrains encontrada nesse link: https://blog.jetbrains.com/research/2024/05/developer-ecosystem-survey-insights-a-comparative-look-at-students-and-professionals/#programming-languages

**RQ 06:**

# Resultados

**RQ 01:**

**RQ 02:** Os resultados mostram que há uma grande variação na quantidade de contribuições externas que os sistemas populares recebem. O número de pull requests aceitas varia de 0 a 73.397, com o quartil inferior sendo 43, a média 257,3 e quartil superior de 1391 pull requests.

**RQ 03:** Os resultados mostram que há uma grande variação na frequência com que os sistemas populares lançam releases. O número total de releases varia de 0 a 1000, com o quartil inferior sendo 0, a média sendo 17 e quartil superior de 60 releases.

**RQ 04:**

**RQ 05:** Os resultados mostram que as 5 linguagens mais utilizadas pelos repositórios representam juntas 562 repositórios, sendo a primeira delas Python, com 147 repositórios e ocupa a primeira posição na lista de linguagens mais populares. A segunda é TypeScript com 135 repositórios, ocupando a nona posição da pesquisa. Terceira é C++ com 108 repositórios e ocupa sexto lugar na pesquisa. Quarta é o JavaScript com 102 repositórios e ocupa segundo lugar na pesquisa. Quinto é Go com 70 repositórios e ocupando décima terceira posição de linguagem mais popular

**RQ 06:**

# Discussão sobre hipótese e resultado

**RQ 01:**

**RQ 02:** Em conclusão, enquanto alguns sistemas populares recebem um número muito alto de contribuições externas, outros recebem relativamente poucas, as vezes até nenhuma. No entanto, a média e o quartil superior sugerem que, em geral, sistemas populares tendem a receber um número significativo de contribuições externas, porém, a popularidade não seria o melhor indicativo de que um sistema recebe muitas contribuições externas.

**RQ 03:** Em conclusão, enquanto alguns sistemas populares lançam um número muito alto de releases, outros não lançam nenhuma. Entretanto, a média e o quartil superior sugerem que sistemas populares podem lançar releases com uma frequência moderada. Em geral, a frequência de lançamentos realmente dependem mais da filosofia de gerenciamento do repositório

**RQ 04:**

**RQ 05:** Em conclusão, a popularidade de uma linguagem de programação tende a influenciar a popularidade de um repositório. Linguagens populares têm grandes comunidades de desenvolvedores, ampla documentação e suporte, o que facilita o desenvolvimento e a manutenção do software.

**RQ 06:**

# Executando o script para coletar dados
## Instalando o Python
Visite a [página oficial de Download do Python](https://www.python.org/downloads/) e busque instruções de instalação para seu sistema operacional.

## Instale os pacotes necessários
Após instalar o Python, navegue até o diretório do projeto execute os seguintes comandos:

`pip install requests`

`pip install python-dotenv`

## Criar .env
Depois de instalar os pacotes necessários, crie um arquivo .env na raíz do diretório e escreva o seguinte

`TOKEN="<insira aqui seu token de acesso>"`

## Execute o programa
Finalmente, após configurar o ambiente execute o programa da seguinte forma:

`python3 main.py <termo de pesquisa entre aspas> <quantidade de resultados>`

Para obter o mesmo arquivo csv que o presente no trabalho execute:

`python3 main.py "Open Source" 1000`
