# Engenharia de dados

## Introdução ao Data mining
### Apresentação
A Mineração de Dados (Data Mining) tem a função de tratar informações em banco de dados. São informações que, de certa forma, não foram utilizadas e ficaram guardadas como qualquer banco de armazenamento de informações. Foi descoberto que esses dados, não importando a área de atuação, podem ser fundamentais e, então, contribuir para decisões sobre negócios ou pesquisas.

Com a crescente demanda de acessos à Internet, o surgimento de novos dispositivos a todo momento e o avanço nos serviços de cloud computing, cruzar informações que podem ser analisadas em grandes volumes de dados se tornou uma necessidade, principalmente quando se pretende buscar resultados mais rápidos e precisos.

Campos computacionais, como Inteligência Artificial (IA), inteligência computacional, aprendizagem de máquina, processamento de linguagem natural, Big Data, dentre outros, estão ligados diretamente à mineração, pois estão relacionados ao tratamento de dados em suas bases.

Nesta Unidade de Aprendizagem, você aprenderá sobre Data Mining e conhecerá algumas de suas definições, sua serventia, sua importância em tomadas de decisão, bem como os tipos de dados e nomenclaturas usadas.

Bons estudos.

Ao final desta Unidade de Aprendizagem, você deve apresentar os seguintes aprendizados:
- Definir Data Mining.
- Descrever os tipos de dados usados em Data Mining.
- Explicar as nomenclaturas mais comuns em Data Mining.

Introdução
Por meio do avanço da internet e da computação em nuvem, o fluxo de dados aumentou consideravelmente, de forma que muitas organizações tiveram que se preparar mais para o armazenamento e o controle das informações do que para a seleção e a análise destas. Portanto, houve consideráveis investimentos em equipamentos e recursos para o armazenamento seguro de dados. 

Surge, então, a necessidade de tratar esses dados da forma mais eficiente possível, gerando conhecimento e, portanto, vantagem para as organizações. Foi assim que a mineração de dados, ou data mining, ganhou destaque nos últimos anos. De fato, o conhecimento organizacional armazenado é um ativo dos mais valiosos, pois apoia tomadas de decisões estratégicas de negócios.

Trata-se de uma abundância de dados que, se não forem tratados corretamente, podem acabar gerando problemas para a empresa, o que justifica procedimentos e ações que armazenem e analisem todos esses dados com inteligência. Dessa forma, a pedra fundamental de um trabalho de mineração é a definição da estratégia, ou seja, do objetivo do negócio, incluindo metas e expectativas, para alcançar o sucesso.

Tendo clara a estratégia, procede-se à extração de dados que possam ampliar o negócio, tanto em relação a aspectos técnicos quanto comerciais (TORGO, 2017). Porém, diante do volume de informações brutas, são necessárias a coleta entre variáveis relevantes e a definição de parâmetros analíticos que tenham relação direta com o negócio, sempre no intuito de assimilar todos os dados e informações importantes. A esse propósito, servem os modelos preditivos, direcionados, de forma simplificada, ao comportamento dos clientes, prevendo resultados futuros que possibilitarão ações mais eficientes.

Vê-se, portanto, a importância da tarefa de minerar dados, promissora e fundamental para todos os negócios, pois todos possuem clientes de forma direta ou indireta. Continue a leitura e aprofunde seus conhecimentos a respeito desse revolucionário processo.

## 1 Conceitos fundamentais

Conforme Turban e Volonino (2013), a mineração de dados é um processo computadorizado da inteligência de negócios que conduz buscas em grandes quantidades de dados e informações para tentar descobrir relações previamente desconhecidas, mas valiosas, entre eles. Dessa forma, pode fornecer respostas para perguntas organizacionais importantes, ajudando a fazer predições e, por consequência, a tomar decisões operacionais e estratégicas, como comentamos na introdução deste capítulo.

A mineração de dados vem se tornando muito popular no mundo computacional por aplicar técnicas e soluções no tratamento de recuperação da informação sem passar por cima de técnicas de análise de dados. Trata-se de um processo que utiliza inteligência estatística, matemática e artificial,
bem como técnicas de aprendizagem baseadas em computador para extrair e identificar informações úteis e o conhecimento subsequente de grandes bancos de dados, incluindo *data warehouses*.

---
> ### Saiba mais
> Segundo Castro e Ferrari (2016), o termo “mineração de dados” remete ao processo de exploração de minérios. O processo de exploração das bases de dados alude à exploração da mina, e a utilização de algoritmos alude a ferramentas de trabalho utilizadas para a obtenção do conhecimento, ou seja, os minerais preciosos.

---

Com o crescente avanço da tecnologia e o consequente aumento de velocidades de processamento, custos menores de armazenamento e melhorias em pacotes de software tornaram a mineração de dados mais atraente e econômica.

Devido à corrida por desenvolvimento e consumo de software e hardware interligados com computação em nuvem, a quantidade de dados gerados aumentou exponencialmente; com isso, foram criados muitos repositórios para diferentes derivações de dados. O que vem facilitando e incentivando essa demanda aumentada de dados são as plataformas web, veneradas pelos usuários pela praticidade com que podem publicar e compartilhar postagens e notícias, entre outas atividades que levam a gerar muitas informações. Os aplicativos também são grandes responsáveis pelo aumento do volume de dados, pois demandam avanços em projeto de algoritmos para aprendizagemde novos padrões de forma dinâmica e escalável.

Atualmente, as áreas que mais utilizam a mineração de dados são as finanças (em bancos, por exemplo, para identificar que clientes responderão melhor a propostas de empréstimo e financiamento), o varejo (para prever vendas, agendar distribuição de mercadorias, etc.) e a saúde (para correlacionar demografia de pacientes com doenças críticas e obter melhores insights sobre sintomas). Sobretudo, tem sido muito utilizada para (TURBAN; VOLONINO, 2013):
- detectar comportamento fraudulento, especialmente em reclamações de apólices de seguros e no uso de cartões de crédito.
- identificar padrões de compras dos clientes;
- recuperar clientes lucrativos;
- identificar regras de negociação a partir de dados históricos;
- apoiar a análise de carrinhos de compras.

A mineração de dados, assim, ajuda a responder perguntas como estas:
- Como é possível efetuar a segmentação do mercado para identificar
clientes em potencial?
- De que forma se pode efetuar o agrupamento de clientes atuais?
- Como classificar os clientes com maior potencial para o futuro?
- Como saber quais são os clientes com tendências a perder interesse
pelo negócio ou produto?
- Como aplicar os valores corretos para produtos e serviços?

---
>### Fique atento
>Cada vez que você usa seu cartão de crédito, sua compra ou transação fica registrada. A cada solicitação de compra, informações são enviadas para uma base transacional no intuito de verificar se o cartão é válido, se não foi dado como roubado, se o comportamento de compra não é atípico e se o limite não foi ultrapassado. Para a empresa de cartão de crédito, esses dados transacionais podem conter incontáveis entradas anuais para cada cliente. O desafio é encontrar formas de extrair (minerar) essas informações e utilizá-las a favor dos objetivos estratégicos da companhia (SHARPE; DE VEAUX; VELLEMAN, 2011).
---

A mineração de dados também tem sido muito utilizada na área da educação, onde amplia possibilidades para que o conhecimento alcance degraus que contribuam para melhorias dos sistemas de ensino e aprendizagem pela análise de dados que permitam prever como será o desempenho de alunos, professores, instituições, enfim, de todos que possam influenciar o ambiente de aprendizagem. Ajuda, assim, a melhorar as condições escolares como infraestrutura, processo escolar e acadêmico, desempenho dos alunos, entre outros fatores ligados a esses sistemas, incluindo monitoramento mais eficiente de reprovação e evasão escolar.

Seja qual for a área, a utilização de alternativas para análises de dados, reconhecimento de padrões, aplicação de modelagens, análises estatísticas e correlação das informações contribui para o cruzamento das bases de pesquisa, levando a um ponto central de conhecimento que beneficia qualquer campo e, por consequência, impulsionando estratégias para obtenção de lucro, inovação e progresso tecnológico.

De fato, a mineração de dados faz parte de um processo mais complexo: a **descoberta de conhecimento em bases de dados**, ou *knowledge discovery in databases* (KDD). Embora algumas pessoas costumem empregar os termos como sinônimos, não se trata da mesma coisa. A mineração de dados é parte integrante da KDD, processo geral de conversão de dados brutos em informações úteis, como mostrado na Figura 1, que consiste nas etapas a seguir.
1. Seleção de dados.
2. Pré-processamento de dados.
3. Transformação de dados.
4. Mineração de dados.
5. Interpretação/avaliação de dados.

![kdd](https://raw.githubusercontent.com/Mateus-cpa/estudos_engenharia_dados/refs/heads/main/images/engenharia_dados/etapas_dados_kdd.png)

Dessa forma, a mineração de dados é utilizada como refinamento dos resultados das etapas anteriores, pois analisa as informações em cima dos padrões exigidos e, em seguida, conclui com a validação dos dados que passaram pela análise, ou seja, que estavam dentro da classificação exigida de acordo com o modelo do projeto ou negócio, seguindo para etapa de padronização (BUTTLE, 2009).

Tudo começa a partir de um repositório de dados, com os mais variados tipos de informações, que, até então, não possuem valores especificados. Após todo o processo é que se consegue obter modelos ou conjuntos de informações que serão importantes e decisivos para tomadas de decisões,  ou seja, o **conhecimento**, efetivamente. Isto é, a mineração de grandes volumes de dados resulta na descoberta de novos e importantes elementos ou padrões, antes “escondidos”, que contribuirão para alavancar ainda mais o desenvolvimento do ciclo de vida de um estabelecimento (comercial ou não) por meio decisões e estratégias para gerenciamento desses dados. Em outras palavras, a utilização da mineração permite buscar informações do passado, desprezadas pelo seu tempo, e cruzá-las com os acontecimentos recentes, oferecendo soluções que contemplem a base ou pilar do negócio (SFERRA; CORRÊA, 2003).

É importante observar, porém, de acordo com Baskarada e Koronios (2013), que somente dados não são capazes de dizer algo aprofundado sobre alguma pesquisa ou investigação; eles necessitam ser convertidos para informações, conhecimento e, por fim, sabedoria, no intuito de poder, efetivamente, agregar valor a uma organização. Trata-se, fundamentalmente, da ideia disseminada por Russell L. Ackoff no artigo “From data to wisdom”, de 1989, retratada na forma da hierarquia DIKW, ou do inglês *data, information, knowledge and wisdom* (ou dados, informação, conhecimento e sabedoria), na Figura 2.

Pela análise da Figura 2, temos o seguinte (BELLINGER; CASTRO; MILLS, 2003).
- Dados. É a forma “bruta” da informação, sem inter-relação com outras bases e sem resultados significativos além de sua própria existência. Podem existir em qualquer formato, utilizável ou não. Os dados são, porém, o ponto de partida para alcançar um resultado significativo.
- Informações. São dados que possuem algum significado ou classificação de acordo com suas bases, podendo ou não ser utilizados. É aqui que os dados começam a ser processados por meio de análises para encontrar respostas para as perguntas “Quem?”, “O quê?”, “Quando?” e “Onde?”.
- Conhecimento. É o aproveitamento de um conjunto de informações para soluções de problemas ou desenvolvimento de ideias. Essas combinações acontecem de forma determinística para utilizar integração com outros conhecimentos e, assim, conhecer metodologias. Pode-se dizer que, nesse nível, surge o interesse pela informação por meio da resposta para a pergunta “Como?”.
- Sabedoria. Considerado o nível mais alto alcançado na hierarquia da DIKW, responde à pergunta “Por quê?” por meio de um processo extrapolativo, não determinístico e não probabilístico. Ele convoca todos os níveis anteriores de consciência e, especificamente, tipos especiais de programação humana (códigos morais, éticos, etc.). É a essência da investigação filosófica. Ao contrário dos níveis anteriores, faz perguntas para as quais não há resposta (facilmente alcançável). Sabedoria é, portanto, o processo pelo qual também discernimos, ou julgamos, entre certo e errado, bom e ruim. Para que as relação entre os níveis fique mais clara, veja o exemplo abaixo, no Quadro 1.

| Nível da hierarquia DIKW | Exemplo | Descrição |
| :--- | :---: | ---: |
| Dados | “Está chovendo.” | Representa um fato ou uma declaração de evento sem relação com outras coisas. |
|Informação|“A temperatura caiu 8°C e, depois, começou a chover.”|Incorpora o entendimento de relações de algum tipo, possivelmente causa e efeito."|
|Conhecimento|“Se a umidade está muito alta e a temperatura cai consideravelmente, é improvável que a atmosfera seja capaz de reter a umidade; então, chove.”|Representa um padrão que conecta e geralmente fornece um alto nível de previsibilidade como o que está descrito ou o que acontecerá na sequência.|
|Sabedoria|“Chove porque chove. E isso abrange todas as interações que acontecem entre chuva, evaporação, correntes de ar, gradientes de temperatura, mudanças, chuva.”|Abarca uma compreensão dos princípios fundamentais incorporados no conhecimento que são essencialmente a base para o conhecimento ser o que é. A sabedoria é, sobretudo, sistêmica.|

**Fonte**: Adaptado de Bellinger, Castro e Mills (2003).

Mas, a essa altura, você deve estar se perguntando: “Como coloco em prática a mineração de dados em minha empresa?”. Baseados nas melhores práticas, pesquisadores e praticantes da mineração de dados propuseram uma série de processos para maximizar as chances de sucesso de projetos de mineração. Esses esforços resultaram em alguns processos-padrão, alguns bastante populares, como o CRISP-DM, ou Cross-Industry Standard Process for Data Mining, proposto em meados dos anos 1990 por um consórcio de empresas europeias como uma metodologia-padrão sem proprietário para mineração de dados (SHARDA; DELEN; TURBAN, 2019). A Figura 3 ilustra essa metodologia.

![crisp_dm](https://raw.githubusercontent.com/Mateus-cpa/estudos_engenharia_dados/refs/heads/main/images/engenharia_dados/crisp_dm.png)

Na Figura 3, é possível identificar que há uma necessidade de que o algoritmo desenvolvido, responsável pela exploração e análise da base de dados, repita por mais de uma vez todo o processo, tornando a repetição uma regra a ser obedecida. Com isso, caso não tenha obtido sucesso na primeira vez, haverá a segunda e demais vezes até obter o resultado esperado. Essa repetição ajudará a obter maior aprendizado pelas vezes que retornou, tornando o resultado do conhecimento mais preciso e exato.

Obviamente, existem outras metodologias interessantes de aplicação da mineração de dados, que podem ser tão úteis quanto a que descrevemos, dependendo do caso. Neste capítulo, não vamos adiante nesse assunto, então cabe a você pesquisar mais sobre ele. A seguir, serão apresentadas algumas descrições sobre os tipos de dados utilizados em mineração de dados. Vamos lá?

## 2 Tipos de dados usados em mineração de dados

Atualmente, como comentamos na seção anterior, os *data warehouses* são muito grandes e ricos em recursos, de forma que é necessário minerar os dados corporativos a fi m de revelar aqueles que realmente são valiosos para o aprimoramento de práticas e processos empresariais, bem como, em última instância, para a alavancagem estratégica do negócio. Mas quais seriam esses dados? Que informações se deseja obter? Como os usuários podem não saber como aproveitar informações passadas ou antigas, nem como extrair conhecimento a partir delas, cabe utilizar a mineração de dados para encontrar diferentes parâmetros que ajudarão nas decisões.

Segundo Castro e Ferrari (2016), existem algumas funcionalidades da mineração de dados que podem ser aplicadas na especificação do tipo de informações que se deseja obter durante a mineração do banco de dados. Estas estão classificadas em:
- **descritivas**, quando se busca por padrões compreensíveis para que humanos possam descrever os dados, caracterizando suas propriedades gerais;
- **preditivas**, quando, por meio de algumas variáveis, é possível realizar previsões de valores desconhecidos ou futuros pela inferência com outras variáveis a partir dos objetivos pretendidos. 

A análise descritiva de dados se baseia no uso de ferramentas capazes de medir, explorar e descrever características particulares dos dados, além de permitir uma sumarização e compreensão dos objetos da base e de seus atributos. Isso é vantajoso, por exemplo, para uma análise de salários dentro de um grupo de funcionários, identificando se a faixa salarial está abaixo ou acima da média. Porém, em muitos casos, o uso de dados preditivos com algoritmos estatísticos e técnicas de aprendizado de máquina ajuda na identificação e na estimativa para prever resultados futuros.

Para a análise descritiva, existem alguns tratamentos internos, como agrupamento e associação, úteis para quando se deseja encontrar grupos de objetos que possuem objetos iguais ou semelhantes. Por outro lado, para a análise prescritiva, temos a classificação, que serve para avaliar a classe de um objeto não rotulado, como prever se tumor em células é benigno ou maligno, ou classificar transações de cartão de crédito como legítimas ou fraude.

Conforme Castro e Ferrari (2016), é possível definir um tipo de abordagem, na  mineração de dados, de acordo com os rótulos ou a classificação dos dados. Essas abordagens podem ser **supervisionadas**, quando há rótulos que os classificam como normais ou com anomalias, e **não supervisionadas**, quando não há rótulos conhecidos para os objetos da base. Veja a Figura 4, que ilustra todo o processo de detecção de anomalias, incluindo os passos convencionais de predição.

Cada banco de dados possui características que o difere de outros; dessa
forma, os objetivos de cada análise deverão ser diferentes, embora o cruzamento
entre os resultados dessas explorações ajude na formatação de um sistema
com alto grau de confiabilidade. Pela importância da base de dados, então,
vê-se a relevância da mineração de dados, que veio para analisar e organizar
tudo em informações concisas. São diversos os formatos que poderão existir
e, à medida que a compreensão dessas bases vai progredindo, muitas soluções
que estavam programadas poderão mudar de direção.

Apresentamos, a seguir, alguns tipos de dados que fazem parte da mineração de dados, muitos deles ligados ou incorporados ao *data warehouse*, ou
armazém de dados, um tipo de depósito para armazenar informações com
disponibilidade de compartilhamento que geralmente faz parte de uma base
comum de alguma instituição, construído com base no princípio da inteligência
de negócios, ou *business intelligence*.

- **Arquivos simples**. Como o próprio nome diz, são simples por se tratar
de arquivos em formato de texto ou binário em formato “.CSV”, que
podem ser facilmente interpretados por algoritmos de mineração de
dados sem a necessidade de formação de tabelas para a organização
de banco de dados.

- **Bancos de dados relacionais**. Nesse caso, ocorre a definição por meio de tabelas. A coleta de dados é organizada em linhas e colunas, ocorrendo o cruzamento de informações e o relacionamento entre elas. É o método aplicado em padrão API de banco de dados SQL (*structured query language*, ou linguagem de consulta estruturada).

- **Armazém de dados**. Também chamado de *data warehouse*, é a forma de se obter dados que fazem parte de várias fontes de consultas e contribuem para tomadas de decisões. São três os tipos de modelagem de armazém de dados: *enterprise data warehouse, data mart e virtual warehouse*, além de possuir dois tipos de abordagens para atualizações de suas bases como abordagem orientada a consultas e abordagem orientada a atualizações. Geralmente, é aplicado em tomada de decisões de negócios.

- **Bancos de dados transacionais**. Funciona como uma estrutura de coletânea de dados organizados por data e hora, em que a relação é por meio de transações entre os bancos de dados. Possui capacidade de reverter ou desfazer a operação (se ocorrer falhas na conclusão/confirmação da transação), devido a sua flexibilidade, permitindo, ainda, que usuários possam efetuar modificações sem riscos de afetar os bancos de dados. Muito aplicado em sistemas bancários, sistemas distribuídos, bancos de dados de objetos, etc.

- **Bancos de dados multimídia**. Trata-se de dados em formatos de mídias armazenados em bancos de dados orientados a objetos. Aplicados no armazenamento de informações complexas em formatos preestabelecidos e aplicados em bibliotecas digitais, vídeo sob demanda, notícias sob demanda, banco de dados musical, etc.

- Bases de dados espaciais. Tipo de base para armazenamento de dados geográficos ou topográficos em formato de coordenadas, topologia, linhas, polígonos, etc. Sua aplicação está voltada para mapas, posicionamento global, GPS, entre outros.

- **Bancos de dados de séries temporais**. Aplicados no segmento de bolsa de valores, que trabalha com pesquisa de dados temporais e movimentação ou atividades registradas por usuários, com base em matrizes numéricas indexadas por hora, data, etc., por meio de análises em tempo real.

- **World Wide Web (WWW)**. Tratamento de dados por meio da internet. Muito utilizado por compras *on-line*, pesquisas de empregos, consultas científicas, etc. Uma base referenciada por coleção de documentos e recursos, como áudio, vídeo, texto, etc., identificada por URLs (*uniform resource locators*) e utilizada por meio de navegadores como Mozilla, Firefox, Chrome, Internet Explore, etc.

## 3 Nomenclaturas mais comuns em mineração de dados
São inúmeras as técnicas para a mineração de dados. Em geral, a escolha da técnica está relacionada ao tipo de dados de que dispomos e ao tipo de informação que a partir deles pretendemos obter. Algumas das técnicas mais aplicadas em mineração de dados incluem as descritas no Quadro 2.

