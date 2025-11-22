# Arquitetura de Data Warehouse e Data Marts

## Banco de dados relacional
- Criado em 1970 por Edgar Codd;
- Objetivo de compatibilizar os códigos e dados;
- Indenpendência dos dados aos programas;
- Para superar redundâncias e inconsistências;
- Forma simples e fácil de representar os dados e de fazer consultas difíceis;
- Em 1980 começaram a ficar mais usuais e dominantes;
- Empresas se destacaram:
    - **IMB** compactou drasticamento os dados de programação, possibilitando otimização do tempo;
    - **Microsoft** criou interfaces gráficas bidimensionais chamadas *Windows*;
    - **Sybase** ganhou evidência devido à sua robustez e qualidade técnica;
    - **Oracle** se destacou na área de banco de dados por apresentar fatores como desempenho, confiabilidade e segurança.

## Representação de dados
- Relações entre linhas que consiste em um esquema e uma instância;
- Colunas de uma tabela;
- *Esquema* especifica:
    - o nome da relação;
    - o nome e o domínio de uma coluna (Atributo ou campo da relação);
- *Domínio* do atributo:
    - é referenciado pelo nome;
    - serve para restringir valores que este atributo pode atingir;
- *Instância* de uma relação é:
    - Conjunto de linhas (tuplas ou registros) distintas entre si;
    - Compõe a relação em um dado momento;
- *Banco de dados relacional* é:
    - Conjunto de relações com nomenclaturas diferentes;
    - Tem relação com os esquemas.

## Arquitetura de Sistemas
Sistemas de informações é uma ciência que estuda a coleta, armazenamento, processamento, análise e distribuição de dados por meio de tecnologias como softwares, hardwares, banco de dados, sistemas especialistas, sistemas de apoio à gestão.

Deve conter relevância, integração, fluxo independente, controle e diretrizes adequadas.

## Business Intelligence
O sistema de arquitetura de BI pode estar relacionado com dados, bases, documentos, indicadores, informações.

É um conjunto de elementos que que tem o objetivo de apoiar as tomadas de decisões em serviços utilizando dados, informações e conhecimentos.

É usual em diferentes áreas.

## Data warehouse
É um sistema de armazenamento de dados que tem por objetivo auxiliar nas tomadas de decisões.

Principais linguagens de programação:
- Python
- SQL
- Java

Perda da privacidade dos dados aumenta a conscientização da importância da Proteção de Dados.

Torna-se cada vez mais desafiador respeitar a privacidade das pessoas.

## ETL
- **Extract**: extrair
- **Transform**: transformar
- **Load**: carregar

## Banco de dados transacional

Conforme Date (2004), Banco de dados é um grande sistema computadorizado de informações armazenadas, onde usuários podem realizar diferentes processos (inserir, buscar, excluir e alterar dados).

- **Data Warehouse**: 
    - trabalha de forma independente;
    - ideal para pesquisas de grandes volumes;
    - Não armazena dados atuais nem se atualiza em tempo real e rápida;
    - Realiza análises de dados;
    - Centraliza dados de grandes empresas;

- **Banco de dados transacional**: é dependente no que se trata de sistemas de gerenciamento e gestão.

## Modelagem transacional

Técnica de representar dados de forma simples, objetiva e com alto desempenho, além de compreensível.

É uma etapa de implementação de uma Data Warehouse e consolidam dimensões específicas para aumentar a eficácia e rapidez de consultas organizadas.

- **Dimensões regulares**: representam dados descritivos que geram contexto para os dados modelados nas dimensões de medida. É desmembrado em grupos de informações chamados **níveis**.
- **Dimensões de medidas**: Dados quantitativos descritos por dimensões regulares. Conhecida em produtos OLAP - Online Analytical Processing (Processamento Analítico Online). Contém dados de <mark>fatos</mark>.
- **Relações de escopo**: Entre dimensões de medida e regulares para definir o nível em que medidas estarão disponíveis para relatórios.

Com maior quantidade de dados em escala sem precedentes, o valor dos dados também aumentou.

### Técnicas de design de esquema Floco de neve e Estrela

Ambos são multidimensionais.

Os esquemas são concorrentes entre si. A escolha entre eles varia de acordo com a disponibilidade de disco e o poder de processamento computacional.

### Técnicas de design de esquema Floco de neve

- Modelagem com as dimensões da stabelas normalizadas e divididas em hierarquia;
- Menor ocupação do banco de dados;
- Melhor desempenho;
- Inexistência de redundância.

### Técnicas de design de esquema Estrela

- Mais complexo
- Mais comum
- Composto por dois tipos de tabelas:
    - **Tabela de fatos** , no centro do esquema
    - **Tabela com dimensões**, ligada à tabela principal
- Diretamente relacionado com medidas, chaves primárias (PK), chaves estrangeiras (FK), atributos e hierarquias.

## Considerações na escolha da modelagem
- Público-alvo: é necessário uma modelagem para cada atender aos diversos tipos de usuário.

## Tipos de fatos
- Fatos aditivos: Medidas de negócios podem ser agregadas em alguma dimensão;
- Fatos semi-aditivos: podem ser agregados apenas em algumas dimensões;
- Fatos não aditivos: não podem ser agregados em qualquer dimensão

## Tipos de chaves nas tabelas dimensionais
- Primárias: identifica registros exclusivos;
- Substitutivas: será a chave primária para dimensões que mudam lentamente;
- Estrangieras: unem duas tabelas. Geralmente:
    - Unem de fatos e de dimensões;
    - na tabela de fatos, sendo a chave primária na tabela de dimensão;

## Tipos de dimensões
- Tempo
- Produto
- Loja
- Cliente

## Etapas de projeto de um modelo dimensional

- Identificação de processos de negócios
- Identificação de fatos e dimensões em seu modelo de dados dimensionais
- Identificação dos atributos para dimensões
- Definição da granularidade dos fatos comerciais
- Armazenamento de informações históricas (dimensões que modam lentamente)

## Benefícios da modelagem dimensional

- otimização de desempenho;
- recuperação rápida de dados;
- flexibilidade;
- análise multidimensional;
- redução na redundância de dados.

## Hierarquia de modelos dimensionais
Hierarquia é a relação entre as dimensões e os atributos de uma determinada informação.

Ajudam a formar bases primárias sendo alinhadas em uma mesma direção nas tabwlas com bancos de dados.

Os dados são disposrtos dos níveis mais detalhados para os menos detalhados.

##  Níveis de granularidade em modelos dimensionais

Se referem a informações armazenadas em tabeelas, que devem possuir a mesma dimensão (por exemplo, datas anuais).

Esses níveis garantem uma lógica no sistema e evitam resultados confusos e imprecisos que ameacem quais processos.

## Dimensões, fatos e atributos em um Data Warehouse
Para Rocha (2023) estão relacionados aos conceitos gerais dos bancos de dados relacionais, ou seja, ao modelo dimensional onde os dados aparecem em forma de tabelas.

- Colunas = atributos = características dos dados => dimensão ou medição = representam fato.
- Linhas = instâncias.

Dados multidimensionais estão os fatos e as dimensões de um *Data Warehouse* que são relacionados entre si.

**Tabelas de fatos** são caracteriszadas por terem poucas colunas e muitas linhas com informações predominantemente numéricoas.

**Tabelas de dimensões**  armazenam mais elementos textuais com detalhamento de informações que podem ter hierarquias.

**Dimensões** atributos mais relacionados entre si que descrevem coisas organizadas. Pode ser conformada quando compartilhada com duas ou mais tabelas de fatos.

**Tabela de fatos** relação entre diferentes dimensãom onde são armazenados dados numéricos que representam medidas específicas, permitindo análises multidimensionais.

**Atributos** são campos das tabelas que descrevem características de aldo, como propriedades específicas permitindo a organização e análise detalhada de dados.

**Fatos** são uma observação do mercado, normalmente com valor numérico.

**Banco de dados** é um local de armazenamento de informações que variam de acordo com cada tipo de situação emq ue se busca guardar esses dados.

## ETL (*extract*, *transform* e *load*)
É uma ferramenta que identifica dados, os reúne, os traduz e os carrega até uma base de dados.

É a principal etapa na construção, desenvolvimento e manutenção de um *Data Warehouse*.

Por meio desta técnica os dados são otimizados para serem guardados.

Essas etapas têm o objetivo de otimizar e armazenar informações escaláveis, bem como auxiliar nas tomadas de decisões nas organizações.

Está relacionado à tecnpologia de cloud ou armazenamento em nuvem.

### Recomendações
- Fazer um devido planejamento;
- Automatizar etapas sempre que possível;
- Monitorar e validar dados;
- Garantir a segurança das informações.

### Extração
É a primeira etapa.

#### Extração de dados de fontes heterogêneas 
Se dá quando se obtém dados de bancos de dados diferentes, destacando os principais objetivos e características dessa extração.

Fontes de dados podem ser internas ou externas.

Visa a preserver os sistemas existentes e manter a autonomia dos bancos de dados (dentre outros). Citam-se as principais características:
- São analisadas em 3 dimensões: distribuição dos sistemas locais, heterogeneidade e autonomia dos sistemas locais.
- É representado por nós, cada um podendo contar 1 ou mais bancos de dados locais, ligados por redes.
- Os componentes podem ter esquema (Arquitetura) conceitual global, local ou auxiliar.

#### Estudiosos
- Mapeamentos sistemáticos, por Almeida et al. (2020);
- Migração entre bancos de dados, por Rodrigues e Vieira (2019);
- Área da Saúde, por Cruz (2019);
- Área acadêmida Dias e Carvalho-Segundo (2021)

#### SGBDH
Sistema de Gestão de Banco de Dados Heterogêneos.

Também chamados de:
- bancos de dados federados
- sistemas de múltiplos bancos de dados
- multibase

#### Ferramentas
- Apache Nifi
- Talend
- Informatica PowerCenter
- Pentaho Data Integration

### Transformação
São técnicas de préprocessamento a limpeza, a agregação e a derivação. São técnicas de pré-processamento de dados essenciais na engenharia de dados.

Transformam em dados consistentes, deixando-os coerentes para análise.

- São abordados algoritmos e critérios.
- São ajustadas as regras de qualidade de dados

Utiliza algoritmos que trabalham com números e vlaores nominais e, por diferentes tipos de critérios e técnicas empregadas:

- Suavização;
- Agrupamento;
- Generalização;
- Normalização;
- Criação de novos atributos a partir de outros pré-existentes.

#### Limpeza
Visa eliminar problemas como:
- registros incompletos;
- valores errados;
- dados inconsistentes.

As técnicas vão desde remoção de registro com problemas até aplicação de técnicas de agrupamento para auxiliar descoberta de melhores valores.

#### Integração de dados
Com fontes heterogêneas (textos, planilhas, data warehouses, vídeos, imagens), surge a necessidade de integrar os dados em um repositório único sem redundâncias e denpendências entre variáveis/valores conflitantes.
Exemplos:
- categorias difernetes par aos mesmos valores
- chaves divergentes
- regras diferentes para os mesmos dados

#### Redução de dados
Às vezes os volumes de dados são tão grandes que se torna impraticável o processo de análise e de mineiração.

O processo é para redução da massa de dados sem perder a representatividade dos dados originais.

As estratégias adotadas são:
- a criação de estruturas otimizadas para os dados, 
- a seleção de um subconjunto dos atributos
- redução de dimensionalidade
- discretização

#### Ferramentas
- Apache Spark
- Pentaho Data Integration
- Microsoft SQL Server Integration Services (SSIS)

### Carregamento (load)

É a última fase do processo.

Os dados são carregados em um sistema de destino que pode ser de forma completa ou não.

Caregar dados de forma estratégica pomove o ganho de tempo no processamento de dados, além de maior performance.

O carregamento em um *Data Warehouse* pode seguir uma das estratégias

- Estratégias convencionais: carrega de forma individual e sequencial logo após o tratamento deles. Ocorre em tempo real e de forma simples, em algumas etapas.
- *Prepared Statements*: Otimiza o desempenho de carregamento de dados. São estratégias de repetição, por isso são mais eficientes e reutilizam muitos dados, ou
- *Bulk Load*: é mais eficiente na inserção de muitos dados ao mesmo tmepo em um determinado sistema. Sua vantagem está na possibilidade paralela de desativar uma base de daods e ainda carregar registros.
    - Utiliza uma fonte de dados simples, porém se limita ao fato de não permitir o tratamento de dados durante um processo.

#### Considerações:
**Integridade dos dados**: deve-se averiguar devidamente os campos, tabelas e dados.

**Tipo de carga a ser realizada**: 
- incremental: usual em tabelas de fatos.
- total.: usual em tabelas de dimensão. 

**Otimização de processo de carga**: responsável por agilizar o prtocesso por meio de ferramentas de organização de dados.

**Suporte completo ao processo de carga**: avalia o antes e o depois do processo, bem como fases de eliminaçaõ e criação de índices dse necessário.

#### Ferrramentas
- Amazon Redshift
- Google BigQuery (vídeo)
- Microsoft Azure Synapse Analytics

#### Autores
- Área de etiquetagem e rastreio de fontes de daods em Big Data, por Costa (2019);
- Área de vendas por Erba et al (2020);
- Repartição territorial de desmatamentos, por Deus, Almeida e Carvalho (2021)

## Data Marts e Implementação de Soluções Analíticas
**Data Mart** é mais específico que **Data warehouse**, é menor e concentra-se apenas em um determinado assunto ou dado (Schaedler, 2021).

É um subconjunto de Data warehouse, enquanto *Data warehouse* possui um grande repertório.

*Data Mart* possui as seguintes vantagens:

- Diminuição de custos de sistemas para empresas;
- Escopos reduzidos em tamanho;
- Maior apoio à tomada de decisões.

Com a pandemia, foram gerados muitos dados devido à digitalização de serviços públicos e privados, aumentando a importância da preservação digital e dos registros digitais arquivísticos.

### Tipos de Data Marts
- **Dependente**: deriva diretamente de um DAta WArehouse.
    - Possui vantagens como consistência de dados e oferta de dados com qualidade.
    - Exige um alto custo.
- **Independente**: é um pequeno data warehouse projetado de forma estratégica e mais pontual.

Tem como aplicabilidade, para Silva e Silva (2018), a análise de preços de concorrentes, especialmente no e-commerce de material esportivo.

- **Foco**: armazenam um único assunto que é descentralizado.

- **Utilização**: é mais limitado que *data warehouse* e menos longa e complexa

- **Abordagem de projeto**: já se conhecem os detalhes do projeto, melhor planejamento e adoção de escolhas mais eficientes, enquanto Data Warehouses é *top down*.

Está atrelado a pontos de análise, projeto conceitual, ETL e processo analítico. Os resultados geram indicadores que auxiliam os gestores nas tomadas de decisão.

### Projeto e implementação de Data Marts
Abordagens de implementação:
- **Top-down**: modelo relacional e normalização. ETL de forma únida e integrada.
- **Bottom-up**: baseada em um *Data Mart* independente. Implementação rápida e uma das principais vantagens. A Desvantagem é a dificuldade de administrar múltiplas equipes.
- Abordagem de arquitetura BUS - incremental: combinação das abordagens anteriores.

### Integração de Data Marts com Data Warehouse.
Ambos possuem relação com os sistemas de informações (SI). Um serve de base para o outro. Data Mart é um setor do Data Warehouse, como a empresa e seus departamentos.

Mesmo os dados independentes são relacionados entre si.

O processo de ETL deve existir aninda que nõa seja obriga´torio existir ambos no **pipeline**.

Integração só é necessário e importando devido à concorrência de consumidores nas empresas, provocando a necessidade de tomar decisões d emaneira mais precisas e rápidas.

### Tipos (p67)
- [**Integração organizacional**](https://www.astera.com/pt/type/blog/data-mart-vs-data-warehouse): Nesta abordagem, há uma conexão estruturada entre os data marts e o data warehouse, onde os data marts atendem às necessidades específicas de departamentos ou funções, enquanto o data warehouse fornece uma visão unificada da organização.
- [**Integração através de ferramentas**](https://beanalytic.com.br/blog/big-data-e-data-warehouse/): Utiliza ferramentas de tecnologia que facilitam a conexão e sincronização entre os data marts e o data warehouse, como plataformas de ETL (Extract, Transform, Load) e de virtualização de dados, garantindo o fluxo contínuo de informações;
- [**Transferência de dados**]( https://ezly.com.br/integracao-de-dados/): Consiste na movimentação de dados entre data marts e data warehouse, podendo ocorrer por replicação, extração ou carregamento de dados, seja de forma síncrona ou assíncrona para manter os dados atualizados.
- [**Base de dados comum**]( https://www.datacamp.com/pt/blog/data-integration): Refere-se ao uso de uma base de dados centralizada ou um repositório comum que serve de fonte de verdade para tanto os data warehouse quanto os data marts, promovendo consistência e governança.
- [**Integração de programas**]( http://www.fatecead.com.br/tei/semana08-1_bi_cap02.pdf): Envolve a conexão de sistemas e aplicações específicas, permitindo que dados ao nível de programas ou plataformas sejam compartilhados ou sincronizados com o data warehouse e seus data marts, facilitando análises multidimensionais e relatórios integrados.

*Data Marts* tem como objetivo afunilar as características do Data WArehouse e identificar indicadores e sua evolução ao longo do tempo.