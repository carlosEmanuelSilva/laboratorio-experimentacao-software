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

**RQ 01:** Para analisar se sistemas populares são maduros, serão analisados o valor mínimo, máximo, quartil inferior, mediana e quartil superior do ano em que os repositórios foram criados

**RQ 02:** Para analisar se sistemas populares recebem muita contribuição externas, serão analisados o valor mínimo, máximo, quartil inferior, mediana e quartil superior do número total de pull requests aceitas junto com um gráfico scatter com todos os resultados.

**RQ 03:** Para analisar se sistemas populares lançam releases com muita frequência, serão analisados o valor mínimo, máximo, quartil inferior, mediana e quartil superior do número total de releases junto com um gráfico scatter com todos os resultados.

**RQ 04:** Para analisar se sistemas populares lançam releases com muita frequência, serão analisados a data mais recente, a data mais antiga, o quartil inferior, superior e a mediana do ano da útlima atualização dos repositórios.

**RQ 05:** Para analisar se sistemas populares utilizam linguagens populares, serão analisados as 5 linguagens mais usadas e ver que posição elas ocupam no ranking de linguagens mais populares de acordo com a pesquisa da jetbrains encontrada nesse link: https://blog.jetbrains.com/research/2024/05/developer-ecosystem-survey-insights-a-comparative-look-at-students-and-professionals/#programming-languages

**RQ 06:** Para analisar se sistemas populares tem alto percentual de issues fechadas, serão analisados o valor mínimo, máximo, quartil inferior, mediana e quartil superior da porcentagem de issues fechadas junto com um gráfico scatter com todos os resultados.

# Resultados

**RQ 01:** Os resultados mostram que os repositórios foram criados de 2008 a 2024. Com o quartil inferior sendo 2014, a mediana sendo 2017 e o quartil superior o ano de 2021.

**RQ 02:** Os resultados mostram que há uma grande variação na quantidade de contribuições externas que os sistemas populares recebem. O número de pull requests aceitas varia de 0 a 73.397, com o quartil inferior sendo 43, a mediana 257,3 e quartil superior de 1391 pull requests.

![total_pull_requests](https://github.com/user-attachments/assets/b2f231b0-9455-43d4-bc3d-22a096907135)

**RQ 03:** Os resultados mostram que há uma grande variação na frequência com que os sistemas populares lançam releases. O número total de releases varia de 0 a 1000, com o quartil inferior sendo 0, a mediana sendo 17 e quartil superior de 60 releases.

![Total_releases](https://github.com/user-attachments/assets/e986af98-9fdb-4bd1-b598-eed5bd445606)

**RQ 04:** Os resultados mostram que há uma certa variação na ultima vez que os repositórios, com o mais antigo sendo em 2014, entretanto, as atualizações mais recentes, a mediana e o quartil superior foram todas em 2024, com o quartil inferior sendo em dezembro de 2023. Vale mencionar ainda, que mais da metade dos sistemas receberam a ultima atualização com menos de 1 mês de diferença da coleta de dados

**RQ 05:** Os resultados mostram que as 5 linguagens mais utilizadas pelos repositórios representam juntas 562 repositórios, sendo a primeira delas Python, com 147 repositórios e ocupa a primeira posição na lista de linguagens mais populares. A segunda é TypeScript com 135 repositórios, ocupando a nona posição da pesquisa. Terceira é C++ com 108 repositórios e ocupa sexto lugar na pesquisa. Quarta é o JavaScript com 102 repositórios e ocupa segundo lugar na pesquisa. Quinto é Go com 70 repositórios e ocupando décima terceira posição de linguagem mais popular

![linguagens](https://github.com/user-attachments/assets/0854b880-b94b-4b2c-9ea9-330d24dbd2cb)

**RQ 06:** Os resultados mostram que há uma certa variação na porcentagem de issues fechadas nos sistemas populares, com o número variando de 0% a 100%, com o quartil inferior sendo de 48,57%, a mediana sendo 81,57% e o quartil superior sendo de 95,52% de issues fechadas.

![Razao](https://github.com/user-attachments/assets/edca5b76-cf8f-4f49-bf68-964d6e8b71fa)


# Discussão sobre hipótese e resultado

**RQ 01:** Em conclusão, enquanto alguns sistemas tendem a ser bastante antigos, existem sistemas populares que são bem recentes. Porém, o quartil inferior e a mediana sugerem que, em geral, sistemas populares tendem sim a serem mais maduros

**RQ 02:** Em conclusão, enquanto alguns sistemas populares recebem um número muito alto de contribuições externas, outros recebem relativamente poucas, as vezes até nenhuma. No entanto, a mediana e o quartil superior sugerem que, em geral, sistemas populares tendem a receber um número significativo de contribuições externas, porém, a popularidade não seria o melhor indicativo de que um sistema recebe muitas contribuições externas.

**RQ 03:** Em conclusão, enquanto alguns sistemas populares lançam um número muito alto de releases, outros não lançam nenhuma. Entretanto, a mediana e o quartil superior sugerem que sistemas populares podem lançar releases com uma frequência moderada. Em geral, a frequência de lançamentos realmente dependem mais da filosofia de gerenciamento do repositório

**RQ 04:** Em conclusão, enquanto alguns sistemas estão a mais de 10 anos sem receber nenhuma atualização, a grande maioria recebeu atualização em menos de um ano, e mais da metade em menos de um mês, o que sugere que sistemas populares estão constantemente fazendo atualizações e mantendo seus sistemas ativos.

**RQ 05:** Em conclusão, a popularidade de uma linguagem de programação tende a influenciar a popularidade de um repositório. Linguagens populares têm grandes comunidades de desenvolvedores, ampla documentação e suporte, o que facilita o desenvolvimento e a manutenção do software.

**RQ 06:** Em conclusão, enquanto alguns sistemas possuem uma taxa de issues fechadas relativamente baixa, podendo chegar a 0%, os dados mostram que sistemas populares tendem a ter um alto percentual de issues fechadas.

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
