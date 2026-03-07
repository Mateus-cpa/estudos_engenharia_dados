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

